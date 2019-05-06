subroutine Rand(X)       !���ɷ���N��0,1����α�����
    implicit none
    real(kind=8),parameter::pi=3.1415926
    real(kind=8)::U1,U2,X
    
    call RANDOM_SEED()
    call RANDOM_NUMBER(U1)
    call RANDOM_NUMBER(U2)
    X=sqrt(-2*log(U1))*cos(-2*pi*U2)
     
end subroutine


    
        