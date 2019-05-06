!*****************************************二度直立柱体正演程序****************************************************
!                                                                         姓名：景旭
!                                                                         学号：201326020105
!                                                                         完成时间：2016.11.07
!                                                                         指导老师：王万银、纪新林、纪晓琳、邱世灿
!*****************************************************************************************************************
Program foward_2d
character*80 cmdfile
character*80 Input_file_source,Input_file_coordinate,output_file_field
real,allocatable::x_source(:,:),z_source(:,:),x_coordinate(:),z_coordinate(:),Density(:),field(:)
cmdfile='cmd.dat'
call read_cmd(cmdfile,N_source,Input_file_source,N_coordinate,Input_file_coordinate,output_file_field)
allocate (Density(1:N_source),x_source(1:N_source,1:2),z_source(1:N_source,1:2))
call Input_source_2d_vertical(Input_file_source,N_source,Density,x_source,z_source)
allocate(x_coordinate(1:N_coordinate),z_coordinate(1:N_coordinate))
call Input_coordinate_2d_vertical(Input_file_coordinate,N_coordinate,x_coordinate,z_coordinate)
allocate(field(1:N_coordinate))
call foward_2d_vertical(N_source,x_source,z_source,Density,N_coordinate,x_coordinate,z_coordinate,field)
call output_field_2d_vertical(output_file_field,N_coordinate,x_coordinate,z_coordinate,field)
deallocate(Density,x_source,z_source,x_coordinate,z_coordinate,field)
end

!********************************************二度直立柱体场计算子程序**********************************************
!参数说明：
!N_source:场源的个数
!x_source:场源的x坐标
!z_source:场源的z坐标
!N_coordinate:计算点的个数
!x_coordinate:计算点的x坐标
!z_coordinate:计算点的z坐标
!field:计算的场值
!Density:场源的剩余密度
!******************************************************************************************************************
subroutine foward_2d_vertical(N_source,x_source,z_source,Density,N_coordinate,x_coordinate,z_coordinate,field)
integer N_source
real x_source(1:N_source,1:2),z_source(1:N_source,1:2),Density(1:N_source)
integer N_coordinate
real x_coordinate(1:N_coordinate),z_coordinate(1:N_coordinate)
real field(1:N_coordinate)
do k=1,N_coordinate,1
  field(k)=0.0
  do N=1,N_source,1
    do i=1,2,1
      do j=1,2,1
      field(k)=field(k)+(-1)**(i+j)*Delt_g(Density(N),x_source(N,i),z_source(N,j),x_coordinate(k),z_coordinate(k))
      enddo
    enddo
  enddo
enddo
end subroutine

!*****************************计算单个场源在单个计算点产生的重力异常外部函数****************************************
!参数说明：
!Density:场源的剩余密度
!*******************************************************************************************************************
real function Delt_g(Density,x12,z12,x,z)
real Density,x12,z12,x,z
parameter(G=6.672E-3)
Delt_g=G*Density*((x12-x)*LOG((x12-x)**2+(z12-z)**2)+2.0*(z12-z)*ATAN2(x12-x,z12-z))
end function Delt_g

!*******************************************输入场源参数子程序******************************************************
!参数说明：
!Input_file_source:输入场源参数文件名
!N_source:场源的个数
!x_source:场源的x坐标
!z_source:场源的z坐标
!*******************************************************************************************************************
subroutine Input_source_2d_vertical(Input_file_source,N_source,Density,x_source,z_source)
character*(*) Input_file_source
integer N_source
real Density(1:N_source),x_source(1:N_source,1:2),z_source(1:N_source,1:2)
open(10,file=Input_file_source,status='old')
do k=1,N_source,1
  read(10,*) Density(k),x_source(k,1),x_source(k,2),z_source(k,1),z_source(k,2)
enddo
close(10)
end subroutine Input_source_2d_vertical

!*********************************************输入计算点参数子程序**************************************************
!参数说明：
!Input_file_coordinate:输入计算点参数文件名
!N_coordinate:计算点的个数
!x_coordinate:计算点的x坐标
!z_coordinate:计算点的z坐标
!*******************************************************************************************************************
subroutine Input_coordinate_2d_vertical(Input_file_coordinate,N_coordinate,x_coordinate,z_coordinate)
character*(*) Input_file_coordinate
integer N_coordinate
real x_coordinate(1:N_coordinate),z_coordinate(1:N_coordinate)
open(10,file=Input_file_coordinate,status='old')
do k=1,N_coordinate,1
  read(10,*) x_coordinate(k),z_coordinate(k)
enddo
close(10)
end subroutine Input_coordinate_2d_vertical

!********************************************输出场值子程序*********************************************************
!参数说明：
!output_file_field:输出场值文件名
!N_coordinate:计算点的个数
!x_coordinate:计算点的x坐标
!z_coordinate:计算点的z坐标
!field:计算的场值
!*******************************************************************************************************************
subroutine output_field_2d_vertical(output_file_field,N_coordinate,x_coordinate,z_coordinate,field)
character*(*) output_file_field
integer N_coordinate
real x_coordinate(1:N_coordinate),z_coordinate(1:N_coordinate),field(1:N_coordinate)
open(10,file=output_file_field,status='unknown')
do k=1,N_coordinate,1
  write(10,*) x_coordinate(k),z_coordinate(k),field(k)
enddo
close(10)
end subroutine output_field_2d_vertical

!*********************************************输入全局控制参数子程序************************************************
!参数说明：
!cmdfile:保存全局控制参数的文件名
!N_source:场源的个数
!Input_file_source:输入场源参数文件名
!N_coordinate:计算点的个数
!Input_file_coordinate:输入计算点参数文件名
!output_file_field:输出场值文件名
!*******************************************************************************************************************
subroutine read_cmd(cmdfile,N_source,Input_file_source,N_coordinate,Input_file_coordinate,output_file_field)
character*(*) cmdfile
integer N_source,N_coordinate
character*(*) Input_file_source,Input_file_coordinate,output_file_field
open(10,file=cmdfile,status='old')
  read(10,*) N_source
  read(10,*) Input_file_source
  read(10,*) N_coordinate
  read(10,*) Input_file_coordinate
  read(10,*) output_file_field
close(10)
end subroutine read_cmd


