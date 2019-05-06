subroutine XYI4(nx, ny, x, y, nd, ne, xy, I4)
    implicit none
    integer :: nx, ny, nd, ne
    real(kind=8) :: x(nx), y(ny), xy(2,*), I4(4,*)
    integer :: ix, iy
    nd=(nx+1)*(ny+1)
    ne=nx*ny
    do ix = 1, nx+1
        do iy = 1, ny+1
            n = (ix-1)*(ny+1)+iy
            xy(1,n) = x(ix)
            xy(2,n) = y(iy)
        end do
    end do 
    do ix = 1, nx
        do iy = 1, ny
            n = (ix-1)*ny+iy
            n1 = (ix-1)*(ny+1)+iy
            I4(1,n) = n1
            I4(2,n) = n1+1
            I4(3,n) = n1+xy+2
            I4(4,n) = n1+xy+1
        end do 
    end do 
    end subroutine XYI4
        