module Trace                !Ŀ�꺽������ģ��
    use subject             !�̳����ݶ�ȡģ�飬��ȡ��ȡ������
    implicit none
    integer::i,j
    integer,parameter::kmax=3000
    !�������˲�����Ӧ�㷨�еľ���
    real(kind=8),save::X(3,kmax),X1(3,kmax),phi(3,3,kmax),F(3,3,kmax),F_T(3,3,kmax),H(1,3),H_T(3,1),P(3,3,kmax),Q(3,3,kmax)
    real(kind=8),save::Z(kmax),Z1(kmax),S(kmax),S_T(kmax),S_1(kmax),d(kmax),Kk(3,1,kmax),Kk_T(1,3,kmax),U(3,kmax)
    real(kind=8),save::V(kmax),V_d,omg_V(kmax),R(kmax)
    real(kind=8),save::T(kmax)
    real(kind=8),save::temp(1,3),amax,amin
    real(kind=8),parameter::alpha=1.0/60.0
    
     data ((P(i,j,1),i=1,3),j=1,3) / 1.0,0.0,0.0, 0.0 ,1.0,0.0, 0.0,0.0,1.0/ 
     data (H(1,i),i=1,3) /1.0,0.0,0.0 /
contains

subroutine  Kalman               !��ǰ����ģ�͵Ŀ���������Ӧ�˲��㷨
    implicit none
    integer::i,j,k
    write(*,*) "Kalman"
    X(1,1)=state(1)%x             !�����ֵ����Ϊ�״�۲��һ������
    X(2,1)=state(1)%xt
    X(3,1)=state(1)%xtt
    X1(1,1)=state(1)%x             !�����ֵ����Ϊ�����ֵ
    X1(2,1)=state(1)%xt
    X1(3,1)=state(1)%xtt
    
    amax=maxval(state(3:imax-2)%xtt)
    amin=minval(state(3:imax-2)%xtt)
   
    !Z�ĳ�ʼ�����۲�����
    do k=1,imax
      Z(k)=state(k)%x
    end do
    !T���ʼ��
    T(1)=state(2)%t-state(1)%t
    T(imax)=state(imax)%t-state(imax-1)%t 
    do k=2,imax-1  
       T(k)=state(k)%t-state(k-1)%t
    end do 
    !phi��ʼ������ǰ����ģ������Ӧ�㷨��״̬ת�ƾ���
    do k=1,imax  
    do j=1,2
        do i=j+1,3
            phi(i,j,k)=0.0   
        end do
    end do 
      phi(1,1,k)=1.0
      phi(2,2,k)=1.0
      phi(3,3,k)=1.0
      phi(1,2,k)=T(k)
      phi(1,3,k)=T(k)**2/2
      phi(2,3,k)=T(k)
    end do
    !F��ʼ������ǰ����ģ�ͷ�����Ӧ�㷨��״̬ת�ƾ���
    do k=1,imax   !imax������
    do j=1,2
        do i=j+1,3
            F(i,j,k)=0.0   
        end do
    end do 
      F(1,1,k)=1.0
      F(2,2,k)=1.0
      F(3,3,k)=exp(-alpha*T(k))
      F(1,2,k)=T(k)
      F(1,3,k)=(-1.0+alpha*T(k)+exp(-alpha*T(k)))/alpha**2
      F(2,3,k)=(1.0-exp(-alpha*T(k)))/alpha 
    end do 
    !U��ʼ��
    do k=1,imax
       U(1,k)=1/alpha*abs(-T(k)+alpha*T(k)**2/2+(1-exp(-alpha*T(k)))/alpha)
       U(2,k)=T(k)-(1-exp(-alpha*T(k)))
       U(3,k)=1-exp(-alpha*T(k))
    end do
     !��ǰ����ģ�ͣ�Q�����ʼ����QΪϵͳ״̬����Э�������  
     do k=1,imax   
      Q(1,1,k)=1.0/(2*alpha**5)*( 1-exp(-2*alpha*T(k))+2*alpha*T(k)+2*alpha**3*T(k)**3/3-2*alpha**2*T(k)**2-4*alpha*T(k)*exp(-alpha*T(k)))
      Q(1,2,k)=1.0/(2*alpha**4)*( exp(-2*alpha*T(k))+1-2*exp(-alpha*T(k))+2*alpha*T(k)*exp(-alpha*T(k))-2*alpha*T(k)+alpha**2*T(k)**2)
      Q(2,1,k)=Q(1,2,k)
      Q(1,3,k)=1.0/(2*alpha**3)*(1-exp(-2*alpha*T(k))-2*alpha*T(k)*exp(-alpha*T(k)) )
      Q(3,1,k)=Q(1,3,k)
      Q(2,2,k)=1.0/(2*alpha**3)*(4*exp(-alpha*T(k))-3.0-exp(-2*alpha*T(k))+2*alpha*T(k) )
      Q(2,3,k)=1.0/(2*alpha**2)*(1+exp(-2*alpha*T(k))-2*exp(-alpha*T(k)) )
      Q(3,2,k)=Q(2,3,k)
      Q(3,3,k)=1.0/(2*alpha)*(1-exp(-2*alpha*T(k)) )      
     end do
     !����ת�þ���
     call Trans(H,H_T,1,3)
    
     do k=2,imax   !�ӵڶ�����ʼԤ��
        call Trans(F(:,:,k-1),F_T(:,:,k-1),3,3)
        !X(:,k-1)=matmul(F(:,:,k-1),X(:,k-1) )+U(:,k)*X(3,k-1)
        X(:,k-1)=matmul(phi(:,:,k-1),X1(:,k-1) )
     
        !״̬����Э�������ϵ�����뵱ǰ���ٶ������¹�ϵ
        if( X(3,k-1)>0)  then  
             Q(:,:,k-1)=2*alpha*(4-pi)/pi*(amax-X(3,k-1))**2 * Q(:,:,k-1)
        else
             Q(:,:,k-1)=2*alpha*(4-pi)/pi*(amin+X(3,k-1))**2 * Q(:,:,k-1)
        end if
        P(:,:,k-1)=matmul(matmul(F(:,:,k-1),P(:,:,k-1)),F_T(:,:,k-1))+Q(:,:,k-1)
        Z(k-1)=dot_product(H(1,:),X(:,k-1))
        d(k)=Z(k)-Z(k-1)
        
     
         V_d=100*cos(state(k)%epsi/180*pi)*sin(state(i)%beta)-state(k)%dist*sin(0.5/180*pi)*sin(state(i)%beta/180*pi)+state(k)%dist*cos(state(k)%epsi/180*pi)*cos(0.5/180*pi)
        !V_d=100*cos(state(k)%epsi/180*pi)*cos(state(i)%beta)-state(k)%dist*sin(0.5/180*pi)*cos(state(i)%beta/180*pi)-state(k)%dist*cos(state(k)%epsi/180*pi)*sin(0.5/180*pi)
        !V_d=100*sin(state(k)%epsi/180*pi)-state(k)%dist*cos(0.5/180*pi)
        !����α�����
        call Rand(omg_V(k))
        R(k)=V_d**2*omg_V(k)**2
        temp=matmul(H,P(:,:,k-1))
        S(k)=dot_product(temp(1,:),H_T(:,1))+R(k) 
        S_1(k)=1/S(k)
        Kk(:,:,k)=matmul(P(:,:,k-1),H_T)*S_1(k)
         
        call Trans(Kk(:,:,k),Kk_T(:,:,k),3,1) 
   
        X(:,k)=X(:,k-1)+Kk(:,1,k)*d(k)
        P(:,:,k)=P(:,:,k-1)-matmul(matmul(Kk(:,:,k),H),P(:,:,k-1))
        !ÿ�ι������ݷŵ�X1�ļ���
        X1(:,k)=X(:,k)
     end do
     write(*,*) "   ......finish..."
end subroutine
        
subroutine Trans(A,A_T,m,n)    !����ת�ó���
    implicit none
    real(kind=8)::A(m,n)
    real(kind=8)::A_T(n,m) 
    integer::m,n              !����ά��
    integer::i,j
    
    do j=1,n
     do i=1,m
            A_T(j,i)=A(i,j)
        end do
    end do
    
end subroutine

subroutine  Output
    implicit none
    integer::i,j,k
    integer,parameter::fileid=7
    
    write(*,* )   "Output"
   
    open(fileid,file="X.dat")
    write(fileid,"(2X,F15.4,3X,F15.4,3X,F15.4,3X,F15.4,3X,I3)") (X1(1,i),X1(2,i),X1(3,i),state(i)%t,state(i)%num,i=1,imax)
    close(fileid)
    write(*,*) "   ......finish..."
end subroutine 

end module
