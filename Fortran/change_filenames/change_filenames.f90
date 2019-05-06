program ChangeFilenames
    implicit none
    character(len=20) :: filename,outname
    integer i
    do i=1,100
        write(filename,*) i
        write(outname,*) i+100
        write(*,*) outname
        call system("rename "//trim(filename)//".txt "//trim(outname)//".txt")
    end do
    end program