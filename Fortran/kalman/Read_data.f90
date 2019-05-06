module subject       !B�������
    implicit none
    real(kind=8),parameter::pi=3.1414926
    integer,save::imax    !��������С
    
    type position 
        real(kind=8)::dist,beta,epsi,t       !���룬��λ�ǣ������ǣ�ʱ��
        real(kind=8)::x,y,z         !λ��
        real(kind=8)::xt,yt,zt      !�ٶ�
        real(kind=8)::xtt,ytt,ztt   !���ٶ�
        real(kind=8)::acce          !�ϼ��ٶ�
        integer::num                !�״���
    end type
      
    type(position),save::state(2000)         !1000��ǰ������������̨�״���յ�����������ȡ�״���յ�����
    character(len=80),save::distance,azimuth,pitch,time,number     !���룬��λ�ǣ������ǣ�ʱ�䣬���
    
contains

subroutine Read_data 
    implicit none
    integer,parameter::fileid=10  !�ļ����
    character(len=80)::filename   !�ļ���
    
    integer::error                !��ȡ�����Ƿ�ɹ��ж�
    logical::alive                !��ѯ�ļ��Ƿ�����ж�
    integer::i                    
    
    write(*,* )   "Read_data"
    
    !��ȡX����λ�ã��ٶȣ����ٶ���Ϣ
    filename="X.dat" 
    !��ѯ�ļ��Ƿ����
    inquire(file=filename,exist=alive)     
    if(.not.alive) then
        write(*,*) trim(filename),"Does't exist!"   
        stop
    end if
    !���ļ���ȡ��ʼ
    open(fileid,file=filename,action='read',status='old')
    i=1
    do while(.true.)
        read(fileid,"(2X,F15.7,3X,F15.7,3X,F15.7,3X,F15.7,3X,I3)",iostat=error)  state(i)%x,state(i)%xt,state(i)%xtt,state(i)%t,state(i)%num  
         if(error/=0) then
           write(*,*) "   ......finish..."
           exit
        end if 
        i=i+1
    end do
    
    !������������λ����Ϣ
    filename="P.dat" 
    !��ѯ�ļ��Ƿ����
    inquire(file=filename,exist=alive)     
    if(.not.alive) then
        write(*,*) trim(filename),"Does't exist!"   
        stop
    end if
    !���ļ�����ȡ��ʼ
    open(fileid,file=filename,action='read',status='old')
    i=1
    do while(.true.)
        read(fileid,"(2X,F15.7,3X,F15.7,3X,F15.7,3X,F15.7,3X,I3)",iostat=error)  state(i)%dist,state(i)%beta,state(i)%epsi,state(i)%t,state(i)%num  
         if(error/=0) then
           write(*,*) "   ......finish..."
           exit
        end if 
        i=i+1
    end do
    close(fileid)
    
    !��������������С
    imax=i-1

end subroutine

end module
 




