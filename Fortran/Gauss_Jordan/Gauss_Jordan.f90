!ȫ��Ԫ��˹��Լ��(Gauss-Jordan)��ȥ��
!                      ���ߣ�����
!                      ʱ�䣺2017.01.14
!����˵����
!N ���ͱ������������������A�Ľ���
!A ʵ�����飬���롢�������������ʱ���д��ʵ����A���������ʱ��������A-1
!B ʵ�����飬���롢�������������ʱ���д��ʵ����B���������ʱ�����A-1B
SUBROUTINE gaussj(a,n,b)
    INTEGER n,NMAX
    REAL a(n,n),b(n)
    PARAMETER(NMAX=50)
    INTEGER i,icol,irow,j,k,l,ll,indxc(NMAX),indxr(NMAX),ipiv(NMAX)
    REAL big,dum,pivinv
    do j=1,n
        ipiv(j)=0
    end do
    do i=1,n
        big=0
        do j=1,n
            if(ipiv(j)/=1) then
                do k=1,n
                    if(ipiv(k)==0) then
                        if(abs(a(j,k))>=big) then
                            big=abs(a(j,k))
                            irow=j
                            icol=k
                        endif
                    else if(ipiv(k)>1) then
                        pause'singular matrix in gaussj'
                    endif
                end do
            endif
        end do
        ipiv(icol)=ipiv(icol)+1
        if(irow/=icol) then
            do l=1,n
                dum=a(irow,l)
                a(irow,l)=a(icol,l)
                a(icol,l)=dum
            end do
            dum=b(irow)
            b(irow)=b(icol)
            b(icol)=dum
        endif
        indxr(i)=irow
        indxc(i)=icol
        if(a(icol,icol)==0.) pause'singular matrix in gaussj'
        pivinv=1./a(icol,icol)
        a(icol,icol)=1.
        do l=1,n
            a(icol,l)=a(icol,l)*pivinv
        end do
        b(icol)=b(icol)*pivinv
        do ll=1,n
            if(ll/=icol) then
                dum=a(ll,icol)
                a(ll,icol)=0.
                do l=1,n
                    a(ll,l)=a(ll,l)-a(icol,l)*dum
                end do
                b(ll)=b(ll)-b(icol)*dum
            endif
        end do
    end do
    do l=n,1,-1
        if(indxr(l)/=indxc(l)) then
            do k=1,n
                dum=a(k,indxr(l))
                a(k,indxr(l))=a(k,indxc(l))
                a(k,indxc(l))=dum
            end do
        endif
    end do
    END SUBROUTINE gaussj
    
PROGRAM D1R1
!Driver program for routine gaussj
PARAMETER(N=3)
DIMENSION A(3,3),B(3),A1(3,3),B1(3)
DATA A/2.,5.,1.,1.,-1.,-3.,2.,1.,-4./
DATA B/5.,8.,-4./
PRINT*,'��֪��������Ҷ�����'
DO I=1,N
    WRITE(*,'(1X,3F12.6)') B(I)
END DO
DO I=1,N
    DO J=1,3
        A1(I,J)=A(I,J)
    END DO
END DO
CALL gaussj(A,N,B)
WRITE(*,*)
PRINT*,'�����������Ľ�'
DO I=1,N
    WRITE(*,'(1X,3F12.6)') B(I)
END DO
!��������Ľ�B����ϵ����������֤�������Ƿ���ȷ
DO L=1,N
    B1(L)=0.
    DO J=1,N
        B1(L)=B1(L)+A1(L,J)*B(J)
    END DO
END DO
WRITE(*,*)
PRINT*,'������Ľ����ϵ������Ľ��'
DO I=1,N
    WRITE(*,'(1X,3F12.6)') B1(I)
END DO
END

