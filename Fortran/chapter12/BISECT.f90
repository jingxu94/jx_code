!���ַ����
module NUMERICAL
    implicit none
    real,parameter :: zero=0.00001
    contains
    real function bisect(A,B,func)
    implicit none
    real A,B
    real C
    real FA,FB,FC
    real,external :: func
    
!����C��F(C)��ֵ
    C=(A+B)/2.0
    FC=func(C)
    do while(abs(FC)>zero)
        FA=func(A)
        FB=func(B)
        if(FA*FC<0) then
            B=C
            C=(A+B)/2.0
        else
            A=C
            C=(A+B)/2.0
        end if
        FC=func(C)
    end do
    bisect=C
    return
    end function
    
    real function f1(X)
        implicit none
        real X
        f1=(X+3)*(X-3)
        return
    end function
    
    real function f2(X)
        implicit none
        real X
        f2=(X+4)*(X-5)
        return
    end function
    
end module
    
program main
    use NUMERICAL
    implicit none
    real A,B
    real ANS
    do while(.true.)
        write(*,*) "���������²��ֵ"
        read(*,*) A,B
        if(f1(A)*f1(B)<0) exit
        write(*,*) "����ȷ��ֵ"
    end do
    ANS=bisect(A,B,f1)
    write(*,"('x=',F6.3)") ANS
    
    do while(.true.)
        write(*,*) "���������²��ֵ"
        read(*,*) A,B
        if(f2(A)*f2(B)<0) exit
        write(*,*) "����ȷ��ֵ"
    end do
    ANS=bisect(A,B,f1)
    write(*,"('x=',F6.3)") ANS
    
    stop
end program 