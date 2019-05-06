module inv_mat
!  Description : ���������
contains
subroutine inv(A,invA,N)
!  Purpose   :  ���������
!-----------------------------------------------------
!  Input  parameters  :
!       1. A: ��Ҫ����ľ���
!       2. N: �����ά��
!  Output parameters  :
!       1. invA: A�������
    implicit real*8(a-z)
    integer::n
    integer::i
    real*8::A(n,n),invA(n,n),E(n,n)
    E=0
   !����EΪ��λ����
    do i=1,n
    E(i,i)=1
    end do
    call mateq(A,E,invA,N,N)
end subroutine inv

subroutine mateq(A,B,X,N,M)
!  Purpose   :  ��˹����Ԫ��ȥ��������󷽳�
!                 AX=B
    implicit real*8(a-z)
    integer::N,M,i
    real*8::A(N,N),B(N,M),X(N,M)
    real*8::btemp(N),xtemp(N)
    do i=1,M
    btemp=B(:,i)
    call elgauss(A,btemp,xtemp,N)
    X(:,i)=xtemp
    end do
end subroutine mateq
subroutine elgauss(A,b,x,N)
!  Purpose   :  ��˹����Ԫ��ȥ��
!                 Ax=b
     implicit real*8(a-z)
     integer::i,k,N
     integer::id_max  !��Ԫ�ر��
     real*8::A(N,N),b(N),x(N)
     real*8::Aup(N,N),bup(N)
    !AbΪ�������  [Ab]
    real*8::Ab(N,N+1)
    real*8::vtemp1(N+1),vtemp2(N+1)
    Ab(1:N,1:N)=A
    Ab(:,N+1)=b
    do k=1,N-1
    elmax=dabs(Ab(k,k))
    id_max=k
    do i=k+1,n
      if (dabs(Ab(i,k))>elmax) then
         elmax=Ab(i,k)
         id_max=i
      end if          
    end do
    vtemp1=Ab(k,:)
    vtemp2=Ab(id_max,:)
    Ab(k,:)=vtemp2
    Ab(id_max,:)=vtemp1   
!#########################################################
    do i=k+1,N
     temp=Ab(i,k)/Ab(k,k)
     Ab(i,:)=Ab(i,:)-temp*Ab(k,:)
    end do
    end do
    Aup(:,:)=Ab(1:N,1:N)
    bup(:)=Ab(:,N+1)
    call uptri(Aup,bup,x,n)
    end subroutine elgauss
subroutine uptri(A,b,x,N)
!  Purpose   :  �����Ƿ�����Ļش�����
!                 Ax=b
    implicit real*8(a-z)
    integer::i,j,N
    real*8::A(N,N),b(N),x(N)
    x(N)=b(N)/A(N,N)
    !�ش�����
    do i=n-1,1,-1
    x(i)=b(i)
    do j=i+1,N
    x(i)=x(i)-a(i,j)*x(j)
    end do
    x(i)=x(i)/A(i,i)
    end do
end subroutine uptri
end module inv_mat