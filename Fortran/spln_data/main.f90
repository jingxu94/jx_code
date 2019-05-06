program splndata
    implicit none
    integer,parameter :: data_lines=604445
    integer :: num_xcoord, start_point, end_point, n_old, n_spln
    real(kind=8),allocatable :: x_coordinate(:), new_x(:), old_field(:), x_spln(:), new_field(:,:), new_field1(:)
    real(kind=8) :: time(data_lines)
    !real(kind=8),parameter :: dy1=0d0, dyn=0d0
    character(len=80) :: filename, outname
    integer :: i, j, k
    
    write(*,*) "请输入x网格节点总数："
    read(*,*) num_xcoord
    write(*,*) "请输入插值原始数据起止x网格节点号："
    read(*,*) start_point, end_point
    
    n_old = end_point-start_point+1
    
    allocate( x_coordinate(num_xcoord), old_field(n_old), x_spln(n_old) )
    
    open(10,file="xyz.txt")
        read(10,*)
        read(10,*)
        read(10,*) x_coordinate
    close(10)
    
    do i = 1, n_old
        x_spln(i) = x_coordinate(start_point+i-1)
    end do
    
    n_spln = aint(aint((x_coordinate(end_point)-x_coordinate(start_point))/0.4))+1
    
    allocate( new_x(n_spln), new_field(n_spln,data_lines), new_field1(n_spln) )
    
    do i = 1, n_spln
        new_x(i) = x_coordinate(start_point) + (i-1) * 0.4
    end do
    
    do i = 1, data_lines
        do j = 1, n_old
            write(filename,'(g0)') start_point+j-1
            filename = trim("30us-300-"//trim(filename)//"相关结果.dat")
            open(10,file=filename)
                if (i /= 1) then
                    do k = 1, i-1
                        read(10,*)
                    end do
                end if
                read(10,*) time(i), old_field(j)
            close(10)
        end do
        call spln( x_spln, old_field, n_old, 0d0, 0d0, new_x, new_field1, n_spln )
        !write(*,*) "pass"
        do j = 1, n_spln
            new_field(j,i) = new_field1(j)
        end do
    end do
    do i = 1, n_spln
        write(outname,'(g0)') new_x(i)
        outname = trim("spln-"//trim(outname)//".dat")
        open(10,file=outname)
        do j = 1, data_lines
            write(10,*) time(j), new_field(i,j)
        end do
        close(10)
    end do 
    
    deallocate(x_coordinate, new_x, old_field, x_spln, new_field, new_field1)
end program