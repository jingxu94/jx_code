program BUBBLE_SORT_DEMO
    implicit none
    integer,parameter :: N=10
    integer :: A(N)=(/6,2,8,4,0,9,3,5,1,7/)
    write(*,"('Source=>',10I3)") A
    call BUBBLE_SORT(A,N)
    write(*,"('Sort=>',10I3)") A
    stop
end program
    
subroutine BUBBLE_SORT(A,N)
    implicit none
    integer :: N,A(N)
    integer i,j,temp
    do i=N-1,1,-1
        do j=1,i
            if(A(j)>A(j+1)) then
                temp=A(j)
                A(j)=A(j+1)
                A(j+1)=temp
            end if
        end do
    end do
    return
end subroutine