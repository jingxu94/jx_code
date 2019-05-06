module MA
    implicit none
    
    interface show
        module procedure show_int
        module procedure show_character
    end interface
    
    contains
    
    subroutine show_int(n)
        implicit none
        integer,intent(IN) :: n
        write(*,"('n=',I3)") n
        return
    end subroutine show_int
    
    subroutine show_character(str)
        implicit none
        character(len=*),intent(IN) :: str
        write(*,"('str=',A)") str
        return
    end subroutine show_character
    
end module MA
    
program ex1104
    use MA
    implicit none
    call show_int(1)
    call show(1)
    call show_character("Fortran 95")
    call show("Fortran 95")
    stop
end program ex1104