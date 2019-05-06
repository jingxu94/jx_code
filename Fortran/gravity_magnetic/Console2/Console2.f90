program foward_3d    
character*80 cmdfile
character*80 Input_file_source,Input_file_coordinate,output_file_gra,output_file_mag,output_file_rtp
real xmin,xmax,ymin,ymax,zmin,zmax
integer N_source,mpoint,nline
real,allocatable::Density(:),x_source(:,:),y_source(:,:),z_source(:,:),mag_source(:),Ax_source(:),Ay_source(:),Az_source(:),Ax_source_rtp(:),Ay_source_rtp(:),Az_source_rtp(:)
real,allocatable::Delt_g(:,:),mag_t(:,:),mag_rtp(:,:)
cmdfile='cmd01.txt'
call read_cmd(cmdfile,Input_file_source,N_source,Input_file_coordinate,output_file_gra,output_file_mag,output_file_rtp)
allocate(Density(1:N_source),x_source(1:N_source,1:2),y_source(1:N_source,1:2),z_source(1:N_source,1:2),mag_source(1:N_source),Ax_source(1:N_source),Ay_source(1:N_source),Az_source(1:N_source),Ax_source_rtp(1:N_source),Ay_source_rtp(1:N_source),Az_source_rtp(1:N_source))
call Input_source(Input_file_source,N_source,Density,mag_source,Ax_source,Ay_source,Az_source,x_source,y_source,z_source)
call Input_xyz(Input_file_coordinate,mpoint,nline,xmin,xmax,ymin,ymax,zmin,zmax)
allocate(Delt_g(1:mpoint,1:nline),mag_t(1:mpoint,1:nline),mag_rtp(1:mpoint,1:nline))
call gra(N_source,Density,x_source,y_source,z_source,Delt_g,mpoint,nline,xmin,xmax,ymin,ymax,zmin,zmax)
call output_GRD(Delt_g,output_file_gra,mpoint,nline,eigval,xmin,xmax,ymin,ymax)
call mag_foward(N_source,mag_source,x_source,y_source,z_source,Ax_source,Ay_source,Az_source,xmin,xmax,ymin,ymax,zmin,zmax,mpoint,nline,mag_t)
call output_GRD(mag_t,output_file_mag,mpoint,nline,eigval,xmin,xmax,ymin,ymax)
call forward_rtp(N_source,Ax_source_rtp,Ay_source_rtp,Az_source_rtp)
call mag_foward(N_source,mag_source,x_source,y_source,z_source,Ax_source_rtp,Ay_source_rtp,Az_source_rtp,xmin,xmax,ymin,ymax,zmin,zmax,mpoint,nline,mag_rtp)
call output_GRD(mag_rtp,output_file_rtp,mpoint,nline,eigval,xmin,xmax,ymin,ymax)
end program

subroutine read_cmd(cmdfile,Input_file_source,N_source,Input_file_coordinate,output_file_gra,output_file_mag,output_file_rtp)
character*(*) cmdfile
integer N_source
character*(*) Input_file_source,Input_file_coordinate,output_file_gra,output_file_mag,output_file_rtp
open(10,file=cmdfile,status='old')
  read(10,*) Input_file_source
  read(10,*) N_source
  read(10,*) Input_file_coordinate
  read(10,*) output_file_gra
  read(10,*) output_file_mag
  read(10,*) output_file_rtp
close(10)
    end subroutine read_cmd
    

subroutine Input_source(Input_file_source,N_source,Density,mag_source,Ax_source,Ay_source,Az_source,x_source,y_source,z_source)
character*(*) Input_file_source
integer N_source
real Density(1:N_source),mag_source(1:N_source),Ax_source(1:N_source),Ay_source(1:N_source),Az_source(1:N_source),x_source(1:N_source,1:2),y_source(1:N_source,1:2),z_source(1:N_source,1:2)
open(10,file=Input_file_source,status='old')
do k=1,N_source,1
  read(10,*) Density(k),mag_source(k),Ax_source(k),Ay_source(k),Az_source(k),x_source(k,1),x_source(k,2),y_source(k,1),y_source(k,2),z_source(k,1),z_source(k,2)
enddo
close(10)
    end subroutine Input_source
    
subroutine Input_xyz(Input_file_coordinate,mpoint,nline,xmin,xmax,ymin,ymax,zmin,zmax)
character*80 Input_file_coordinate
integer mpoint,nline
real xmin,xmax,ymin,ymax
real zmin,zmax
open(10,file=Input_file_coordinate,status='old')
read(10,*)
read(10,*) mpoint,nline
read(10,*) xmin,xmax
read(10,*) ymin,ymax
read(10,*) zmin,zmax
close(10)
    end subroutine Input_xyz
    
subroutine gra(N_source,Density,x_source,y_source,z_source,Delt_g,mpoint,nline,xmin,xmax,ymin,ymax,zmin,zmax)
parameter(G=66.72)
integer N_source,mpoint,nline
real xmin,xmax,ymin,ymax
real zmin,zmax,sum,x,y,z,r
real Delt_g(1:mpoint,1:nline)
real Density(1:N_source),x_source(1:N_source,1:2),y_source(1:N_source,1:2),z_source(1:N_source,1:2)
z=-5.3
do n=1,nline,1
    dy=(ymax-ymin)/(nline-1)
    y=ymin+(n-1)*dy
    do m=1,mpoint,1
        dx=(xmax-xmin)/(mpoint-1)
        x=xmin+(m-1)*dx
        Delt_g(m,n)=0.0
        do l=1,N_source,1
            sum=0.0
            do i=1,2,1
                do j=1,2,1
                    do k=1,2,1
                        r=sqrt((x_source(l,i)-x)**2+(y_source(l,j)-y)**2+(z_source(l,k)-z)**2)
                        sum=sum+(-1)**(i+j+k)*((x_source(l,i)-x)*LOG(y_source(l,j)-y+r)+(y_source(l,j)-y)*LOG(x_source(l,i)-x+r)-(z_source(l,k)-z)*ATAN2((x_source(l,i)-x)*(y_source(l,j)-y),(z_source(l,k)-z)*r))
                    end do
                end do
            end do
            Delt_g(m,n)=Delt_g(m,n)-G*Density(l)*sum
        end do
    end do
end do
    end subroutine gra
    
subroutine output_GRD(A,filename,m,n,eigval,xmin,xmax,ymin,ymax)
integer m,n
real A(1:m,1:n)
character*80 filename
real xmin,xmax,ymin,ymax
real amin,amax
amin=HUGE(amin)
amax=-HUGE(amax)
do j=1,n,1
    do i=1,m,1
            amin=MIN(amin,A(i,j))
            amax=MAX(amax,A(i,j))
    end do
end do
open(10,file=filename,status='unknown')
write(10,'(4A)')'DSAA'
write(10,*) m,n
write(10,*) xmin,xmax
write(10,*) ymin,ymax
write(10,*) amin,amax
do j=1,n
    write(10,*) (A(i,j),i=1,m)
end do
close(10)
    end subroutine output_GRD
    
subroutine mag_foward(N_source,mag_source,x_source,y_source,z_source,Ax_source,Ay_source,Az_source,xmin,xmax,ymin,ymax,zmin,zmax,mpoint,nline,mag_t)
integer N_source,mpoint,nline
real xmin,xmax,ymin,ymax
real zmin,zmax,k1,k2,k3,k4,k5,k6,r,mag_a,mag_b,mag_c
real mag_source(1:N_source),x_source(1:N_source,1:2),y_source(1:N_source,1:2),z_source(1:N_source,1:2)
real Ax_source(1:N_source),Ay_source(1:N_source),Az_source(1:N_source)
real mag_t(1:mpoint,1:nline)
dx=(xmax-xmin)/(mpoint-1)
dy=(ymax-ymin)/(mpoint-1)
z=-5.3
DO t=1,2,1
     CAll Green_second(x_source(r,k),y_source(s,k),z_source(t,k),x_coordinate,y_coordinate,z_coordinate(i,j),Vxx_fun,Vyy_fun,Vzz_fun,Vxy_fun,Vyz_fun,Vxz_fun)
Vxx=Vxx+(-1)**(r+s+t)*Vxx_fun
Vyy=Vyy+(-1)**(r+s+t)*Vyy_fun
Vzz=Vzz+(-1)**(r+s+t)*Vzz_fun
Vxy=Vxy+(-1)**(r+s+t)*Vxy_fun
Vyz=Vyz+(-1)**(r+s+t)*Vyz_fun
Vxz=Vxz+(-1)**(r+s+t)*Vxz_fun
END DO

    end subroutine mag_foward    

subroutine forward_rtp(N_source,Ax_source,Ay_source,Az_source)
integer N_source
real Ax_source(1:N_source),Ay_source(1:N_source),Az_source(1:N_source)
Ax_source=0
Ay_source=90
Az_source=0
    end subroutine forward_rtp
    
subroutine Green_second(x_source,y_source,z_source,x_coordinate,y_coordinate,z_coordinate,Vxx_fun,Vyy_fun,Vzz_fun,Vxy_fun,Vyz_fun,Vxz_fun)
   
    implicit none
    real x_source,y_source,z_source,x_coordinate,y_coordinate,z_coordinate
    real Vxx_fun,Vyy_fun,Vzz_fun,Vxy_fun,Vyz_fun,Vxz_fun

    real dx,dy,dz,r

    dx=x_source-x_coordinate
    dy=y_source-y_coordinate
    dz=z_source-z_coordinate
    r=sqrt(dx**2+dy**2+dz**2)

    Vxx_fun=-atan2((dy*dz),(r*dx))
    Vyy_fun=-atan2((dx*dz),(r*dy))
    Vzz_fun=-atan2((dx*dy),(r*dz))
    Vxy_fun=LOG(r+dz)
    Vyz_fun=LOG(r+dx)
    Vxz_fun=LOG(r+dy)
   
end subroutine Green_second
