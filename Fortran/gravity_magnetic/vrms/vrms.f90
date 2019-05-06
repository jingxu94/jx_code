program vaverage
    implicit none
    integer n,i,k,m,j
    real x(38,17),t(38,17),vrms(38,17),v(38,17)
    real sum
    m=38
    n=17
    open(10,file='vrms1.txt')
    do i=1,m,1
        do j=1,n,1
            read(10,*) x(i,j),t(i,j),vrms(i,j)
        enddo
    enddo
    close(10)
    open(20,file='vave1.txt')
    do j=1,m,1
        do k=1,n,1
            sum=0.0
            sum=t(j,1)*vrms(j,1)
            do i=2,k,1
                sum=sum+sqrt((t(j,i)*vrms(j,i)**2-t(j,i-1)*vrms(j,i-1)**2)*(t(j,i)-t(j,i-1)))
            enddo
            v(j,k)=sum/t(j,k)
            write(20,*) x(j,k),-t(j,k),v(j,k)
        enddo
    enddo
    close(20)
    end
    
    
