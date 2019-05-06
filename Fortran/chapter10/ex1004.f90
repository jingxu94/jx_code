program ex1004
    implicit none
    integer,pointer :: a(:)
    integer,target :: b(5)=(/1,2,3,4,5/)
    !把指针数组a指向数组b
    a=>b
    !a(1~5)=>b(1~5)
    write(*,*) a
    a=>b(1:3)
    write(*,*) a
    a=>b(1:5:2)
    write(*,*) a
    a=>b(5:1:-1)
    write(*,*) a
    stop
end