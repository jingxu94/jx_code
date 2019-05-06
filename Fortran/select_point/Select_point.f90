program select
    implicit none
    integer :: nx
    integer :: x(226)
    real :: xx(226)
    real,allocatable :: gridx(:)
    character(len=80) :: strx, strxx
    integer :: i,j
    write(*,*) "number of x-coordinate:"
    read(*,*) nx
    allocate(gridx(nx))
    open(10,file="xyz.txt")
    read(10,*)
    read(10,*)
    read(10,*) gridx(:)
    close(10)
    !write(*,*) gridx
    do i = 1, 226
        xx(i)=10.0+(i-1)*0.4
    enddo
    !write(*,*) xx
    open(20,file="standard.txt")
    do i = 1,226
        do j = 1,nx-1
            if (xx(i)>gridx(j).and.xx(i)<=gridx(j+1)) then
                x(i)=j+1
                write(20,*) x(i)
            end if
        end do
    end do
    close(20)

    open(30,file="standard.txt")
    do i = 1, 226
        read(30,*) x(i)
        write(strx,'(g0)') x(i)
        write(*,*) trim(strx)
        write(strxx,'(g0)') xx(i)
        write(*,*) "Decay-Curve-"//trim(trim(strx))//"-37.DAT"
        call EXECUTE_COMMAND_LINE("copy /y Decay-Curve-"//trim(strx)//"-37.DAT Decay-Curve-"//trim(strxx)//"-37.DAT")
    end do
    close(30)
    deallocate(gridx)
    end program 