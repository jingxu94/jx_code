program SelectionSortDemo
    implicit none
    integer,parameter :: N=10
    integer :: A(N)=(/6,2,8,4,0,9,3,5,1,7/)
    write(*,"('Source=>',10I3)") A
    call SELECTION_SORT(A,N)
    write(*,"('Sort=>',10I3)") A
    stop
end program
    
subroutine SELECTION_SORT(A,N)
    implicit none
    integer :: N,A(N)
    integer i,j
    integer min
    integer temp
    do i=1,N
        min=A(i)
        do j=i+1,N
            if(min>A(j)) then
                temp=A(j)
                A(j)=A(i)
                A(i)=temp
                min=A(i)
            end if
        end do
    end do
    return
end subroutine