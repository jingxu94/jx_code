program main
    use Trace
    implicit none 
    
    do i=1,10
      write(*,*) i
      call Read_data       !��ȡ����
      call Kalman          !����׷��
    end do
    call Output
end program