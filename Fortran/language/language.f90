PROGRAM language
    REAL t(81),y(81),t1(43),y1(43),y2(43),u(43)
    REAL yklk,lk
    INTEGER i,k,j
    
    OPEN(101,file='filter.dat',status='old')
    DO i=1,81
        READ(101,*) t(i),y(i)
    END DO
    CLOSE(101)
    OPEN(102,file='FPM.dat',status='old')
    DO i=1,43
        READ(102,*) t1(i),y1(i)
    END DO
    CLOSE(102)
    DO i=1,43
        t1(i)=LOG10(t1(i))
        y1(i)=LOG10(y1(i))
    END DO
    DO i=1,81
        t(i)=LOG10(t(i))
        y(i)=LOG10(y(i))
    END DO
    DO i=1,43
        yklk=0
        DO k=1,81
            lk=1
            DO j=1,81
                IF(j.eq.k) THEN
                    CONTINUE
                ELSE
                    lk=lk*(t1(i)-t(j))/(t(k)-t(j))
                END IF
            END DO
            yklk=yklk+y(k)*lk
        END DO
        y2(i)=yklk
        u(i)=(y2(i)-y1(i))/(y2(i))
    END DO
    OPEN(103,file='u.dat')
    DO i=1,43
        WRITE(*,*) t1(i),100*abs(u(i))
        WRITE(103,*) t1(i),100*abs(u(i))
    END DO
    CLOSE(103)
    DO i=1,43
        WRITE(*,*) t1(i),y1(i),y2(i)
    END DO
    END PROGRAM
    
    