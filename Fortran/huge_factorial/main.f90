program main
  implicit none
  integer(2) nLbound, nUbound
  real t1,t2
  call cpu_time(t1)
  nLbound = 1
  nUbound = 2016
  call factorial( nLbound, nUbound )
  call cpu_time(t2)
  print*, 'CPU_Time:',t2-t1
  pause
end program

subroutine factorial( nLbound, nUbound )
Use, Intrinsic :: ISO_FORTRAN_ENV, only : OUTPUT_UNIT
implicit none
integer(2),intent(in) :: nLbound, nUbound
integer(8),parameter  :: pmax = 10**13, length = 10300
integer(8) ires(length), nL, nU
integer(8) i, j, m, n
character ch*24
ires=0; ires(1)=1
nL = 1; nU = 1
do i = nLbound, nUbound
   ires(nL:nU) = ires(nL:nU) * i
   n = 0
 do j = nL, nU
   if( ires(j)/=0 ) then
     m = ires(j) / pmax
     ires(j+1) = ires(j+1) + m
     ires(j) = ires(j) - pmax*m
     n = 1
   else if( n==0 ) then
     nL = j
   end if
 end do
 if( ires(nU+1) > 0 ) nU = nU + 1
end do

! 输出结果：n!
open(output_unit,file='1.txt') !输出到文件

write(ch,*) ires(nU)
ch = adjustl(ch)
m = len_trim(ch)  !首元素中整数值的位数
n = (nU-1)*13+m-1 !指数

!科学计数法
write(OUTPUT_UNIT,'(a)',advance='no') ch(1:1)//'.'//ch(2:m)//'e+'
write(ch,*) n
ch = adjustl(ch)
write(OUTPUT_UNIT,'(a)') trim(ch)
!全部数字
if( nU > 1 ) then
 write(OUTPUT_UNIT,'(i<m>)',advance='no') ires(nU)
 write(OUTPUT_UNIT,'(<nu-1>i13.13)') ires(nU-1:1:-1)
else
 write(OUTPUT_UNIT,'(i<m>)') ires(nU)
end if 
close(OUTPUT_UNIT)
end subroutine factorial