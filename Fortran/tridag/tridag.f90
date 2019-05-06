!           追赶法LU分解程序
!                   作者：景旭
!                   时间：2017.01.16
!参数说明：
!TRIDAG(A,B,C,R,U,N)
!N 实型变量，输入参数，方程的阶数
!A 实型数组，输入参数，存放(a2,...,an)
!B 实型数组，输入参数，存放(b1,...,bn)
!C 实型数组，输入参数，存放(c1,...,cn-1)
!R 实型数组，输入参数，存放(r1,...,rn)
!U 实型数组，输出参数，输出解向量

SUBROUTINE tridag(a,b,c,r,u,n)
PARAMETER(nmax=100)
INTEGER j,n
REAL gam(nmax),a(n),b(n),c(n),u(n),r(n)
if(b(1)==0.) pause'b(1)=0 in tridag'
bet=b(1)
u(1)=r(1)/bet
do j=2,n
    gam(j-1)=c(j-1)/bet
    bet=b(j)-a(j)*gam(j-1)
    if(bet==0.) pause'bet=0 in tridag'
    u(j)=(r(j)-a(j)*u(j-1))/bet
end do
do j=n-1,1,-1
    u(j)=u(j)-gam(j)*u(j+1)
end do
    END SUBROUTINE tridag
    
PROGRAM D1R3
!Driver program for routine TRIDAG
PARAMETER(N=3)
DIMENSION A1(N,N),A(N),B(N),C(N),R(N),U(N),X(N)
DATA A1/1.,2.,0.,2.,2.,3.,0.,3.,3./
DATA R/1.,2.,3./
PRINT*,'已知方程组的右端向量'
DO I=1,N
    WRITE(*,'(1X,3F12.6)') R(I)
END DO
DO I=2,N
    A(I)=A1(I,I-1)
END DO
DO I=1,N-1
    C(I)=A1(I+1,I)
END DO
DO I=1,N
    B(I)=A1(I,I)
END DO
CALL TRIDAG(A,B,C,R,U,N)
WRITE(*,*)
PRINT*,'计算出的方程组的解'
DO I=1,N
    WRITE(*,'(1X,3F12.6)') U(I)
END DO
!将计算出的解B乘以系数矩阵，以验证计算结果正确
DO L=1,N
    X(L)=0.
    DO J=1,N
        X(L)=X(L)+A1(L,J)*U(J)
    END DO
END DO
WRITE(*,*)
PRINT*,'计算出的解乘以系数矩阵的结果'
DO I=1,N
    WRITE(*,'(1X,3F12.6)') X(I)
END DO
END