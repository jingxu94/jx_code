program main
    use Trace
    implicit none 
    
    do i=1,10
      write(*,*) i
      call Read_data       !¶ÁÈ¡Êý¾Ý
      call Kalman          !º½¼£×·×Ù
    end do
    call Output
end program