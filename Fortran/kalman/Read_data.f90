module subject       !B题第三问
    implicit none
    real(kind=8),parameter::pi=3.1414926
    integer,save::imax    !数据量大小
    
    type position 
        real(kind=8)::dist,beta,epsi,t       !距离，方位角，俯仰角，时间
        real(kind=8)::x,y,z         !位置
        real(kind=8)::xt,yt,zt      !速度
        real(kind=8)::xtt,ytt,ztt   !加速度
        real(kind=8)::acce          !合加速度
        integer::num                !雷达标号
    end type
      
    type(position),save::state(2000)         !1000提前给定，大于三台雷达接收的数据量，存取雷达接收的数据
    character(len=80),save::distance,azimuth,pitch,time,number     !距离，方位角，俯仰角，时间，标号
    
contains

subroutine Read_data 
    implicit none
    integer,parameter::fileid=10  !文件编号
    character(len=80)::filename   !文件名
    
    integer::error                !读取数据是否成功判定
    logical::alive                !查询文件是否存在判定
    integer::i                    
    
    write(*,* )   "Read_data"
    
    !读取X方向位置，速度，加速度信息
    filename="X.dat" 
    !查询文件是否存在
    inquire(file=filename,exist=alive)     
    if(.not.alive) then
        write(*,*) trim(filename),"Does't exist!"   
        stop
    end if
    !打开文件读取开始
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
    
    !读入球坐标下位置信息
    filename="P.dat" 
    !查询文件是否存在
    inquire(file=filename,exist=alive)     
    if(.not.alive) then
        write(*,*) trim(filename),"Does't exist!"   
        stop
    end if
    !打开文件，读取开始
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
    
    !测量的数据量大小
    imax=i-1

end subroutine

end module
 




