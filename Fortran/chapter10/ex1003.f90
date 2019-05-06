program ex1003
    implicit none
    integer,pointer :: a=>null()
    integer,target :: b=1,c=2
    
    write(*,*) associated(a)
    a=>c
    write(*,*) associated(a)
    write(*,*) associated(a,c)
    write(*,*) associated(a,b)
    nullify(a)
    write(*,*) associated(a)
    
    stop
end