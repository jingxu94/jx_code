program ex1005
    implicit none
    integer,pointer :: a(:)
    allocate(a(5))
    a=(/1,2,3,4,5/)
    write(*,*) a
    deallocate(a)
    stop
    end
    