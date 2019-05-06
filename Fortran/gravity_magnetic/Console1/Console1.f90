!*****************************************����ֱ���������ݳ���****************************************************
!                                                                         ����������
!                                                                         ѧ�ţ�201326020105
!                                                                         ���ʱ�䣺2016.11.07
!                                                                         ָ����ʦ���������������֡������ա�������
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

!********************************************����ֱ�����峡�����ӳ���**********************************************
!����˵����
!N_source:��Դ�ĸ���
!x_source:��Դ��x����
!z_source:��Դ��z����
!N_coordinate:�����ĸ���
!x_coordinate:������x����
!z_coordinate:������z����
!field:����ĳ�ֵ
!Density:��Դ��ʣ���ܶ�
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

!*****************************���㵥����Դ�ڵ������������������쳣�ⲿ����****************************************
!����˵����
!Density:��Դ��ʣ���ܶ�
!*******************************************************************************************************************
real function Delt_g(Density,x12,z12,x,z)
real Density,x12,z12,x,z
parameter(G=6.672E-3)
Delt_g=G*Density*((x12-x)*LOG((x12-x)**2+(z12-z)**2)+2.0*(z12-z)*ATAN2(x12-x,z12-z))
end function Delt_g

!*******************************************���볡Դ�����ӳ���******************************************************
!����˵����
!Input_file_source:���볡Դ�����ļ���
!N_source:��Դ�ĸ���
!x_source:��Դ��x����
!z_source:��Դ��z����
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

!*********************************************������������ӳ���**************************************************
!����˵����
!Input_file_coordinate:������������ļ���
!N_coordinate:�����ĸ���
!x_coordinate:������x����
!z_coordinate:������z����
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

!********************************************�����ֵ�ӳ���*********************************************************
!����˵����
!output_file_field:�����ֵ�ļ���
!N_coordinate:�����ĸ���
!x_coordinate:������x����
!z_coordinate:������z����
!field:����ĳ�ֵ
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

!*********************************************����ȫ�ֿ��Ʋ����ӳ���************************************************
!����˵����
!cmdfile:����ȫ�ֿ��Ʋ������ļ���
!N_source:��Դ�ĸ���
!Input_file_source:���볡Դ�����ļ���
!N_coordinate:�����ĸ���
!Input_file_coordinate:������������ļ���
!output_file_field:�����ֵ�ļ���
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


