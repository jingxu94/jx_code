program EDGE_2D
    
    character*80 cmdfilename,input_field_filename,output_field_filename
    
    integer method_expand,method_deriv,num_area
    
    integer mpoint,nline
    
    integer m0,m1,m2,m3
    
    integer n0,n1,n2,n3
    
    integer m,n
    
    real xmin,xmax,ymin,ymax,dx,dy
    
    real,allocatable::field(:,:),field_real(:,:),field_image(:,:),field_deriv(:,:)
    
    real,allocatable::deriv_operator_x(:,:),deriv_operator_y(:,:),deriv_operator_z(:,:)
    
    cmdfilename='cmd.txt'
    
    call read_cmd(cmdfilename,input_field_filename,output_field_filename,method_expand,method_deriv,num_area)
    
    call read_mn(input_field_filename,mpoint,nline,xmin,xmax,ymin,ymax)
    
    dx=(xmax-xmin)/(mpoint-1)
    dy=(ymax-ymin)/(nline-1)
    
    call calculate_m1m2_dx(mpoint,m0,m1,m2,m3,m,xmin,xmax,dx)
    
    call calculate_m1m2_dx(nline,n0,n1,n2,n3,n,ymin,ymax,dy)
    
    allocate(field(m0:m3,n0:n3),field_real(m0:m3,n0:n3),field_image(m0:m3,n0:n3),field_deriv(m0:m3,n0:n3),deriv_operator_x(m0:m3,n0:n3),deriv_operator_y(m0:m3,n0:n3),deriv_operator_z(m0:m3,n0:n3))
    
    call input_GRD(input_field_filename,m0,m1,m2,m3,n0,n1,n2,n3,field,eigval)
    
    call expand_cos_2d(field,m0,m1,m2,m3,n0,n1,n2,n3,method_expand)
    
    call deriv_operator_sub(dx,dy,m3,n3,deriv_operator_x,deriv_operator_y,deriv_operator_z)
    
    field_real=field
    
    field_image=0.0
    
    call deriv(field_real,field_image,deriv_operator_x,deriv_operator_y,deriv_operator_z,m0,m1,m2,m3,n0,n1,n2,n3,method_deriv)
    
    field_deriv=field_real
    
    call output_grd(field_deriv,output_field_filename,m0,m3,n0,n3,eigval)
    
    deallocate(field,field_real,field_image,field_deriv,deriv_operator_x,deriv_operator_y,deriv_operator_z)
    
    end program EDGE_2D
    
    
    
    subroutine read_cmd(cmdfilename,input_field_filename,output_field_filename,method_expand,method_deriv,num_area)
    character*80 cmdfilename,input_field_filename,output_field_filename
    integer method_expand,method_deriv,num_area
    open(10,file=cmdfilename,status='old')
    read(10,*) input_field_filename
    read(10,*) output_field_filename
    read(10,*) method_expand
    read(10,*) method_deriv
    read(10,*) num_area
    close(10)
    end subroutine read_cmd
    
    
subroutine read_mn(input_filename,mpoint,nline,xmin,xmax,ymin,ymax)
integer mpoint,nline
real xmin,xmax,ymin,ymax
character*80 input_filename
open(10,file=input_filename,status='old')
read(10,*)
read(10,*) mpoint,nline
read(10,*) xmin,xmax
read(10,*) ymin,ymax
close(10)
    end subroutine
    
subroutine calculate_m1m2_dx(mpoint,m0,m1,m2,m3,m,xmin,xmax,dx)
integer mpoint,mtemp,m0,m1,m2,m3,m
real xmin,xmax,dx,factor_m,mu
m0=1
factor_m=1.5
dx=(xmax-xmin)/(mpoint-1)
mtemp=mpoint
do while((mod(mtemp,2).eq.0).and.(mtemp.ne.0))
    mtemp=mtemp/2
end do
if(mtemp.eq.1) then
    m=mpoint*2
else
    mu=int(LOG(float(mpoint))/0.693147+factor_m)
    m=2**mu
end if
m1=1+(m-mpoint)/2
m2=m1+mpoint-1
m3=m
    end subroutine
    
subroutine input_GRD(input_filename,m0,m1,m2,m3,n0,n1,n2,n3,field,eigval)
character*80 input_filename
integer m0,m1,m2,m3,n0,n1,n2,n3
real eigval
real field(m0:m3,n0:n3)
field=eigval
open(10,file=input_filename,form='formatted')
read(10,*)
read(10,*)
read(10,*) xmin,xmax
read(10,*) ymin,ymax
read(10,*)
read(10,*) ((field(i,j),i=m1,m2,1),j=n1,n2,1)
close(10)
    end subroutine
    
subroutine expand_cos_2d(u,i0,i1,i2,i3,j0,j1,j2,j3,method_expand)
integer i0,i1,i2,i3,j0,j1,j2,j3
real u(i0:i3,j0:j3)
real,allocatable::u1(:)
integer method_expand
integer j,i
allocate(u1(i0:i3))
do j=j1,j2,1
    do i=i0,i3,1
        u1(i)=u(i,j)
    end do
    call expand_cos_1d(i0,i1,i2,i3,u1,method_expand)
    do k=i0,i3,1
        u(k,j)=u1(k)
    end do
end do
deallocate(u1)
allocate(u1(j0:j3))
do i=i0,i3,1
    do j=j0,j3,1
        u1(j)=u(i,j)
    end do
    call expand_cos_1d(j0,j1,j2,j3,u1,method_expand)
    do k=j0,j3,1
        u(i,k)=u1(k)
    end do
end do
deallocate(u1)
    end subroutine expand_cos_2d
    
subroutine expand_cos_1d(i0,i1,i2,i3,u,method_expand)
integer i0,i1,i2,i3
real u(i0:i3)
integer method_expand
integer i
if(method_expand.eq.1) then
    u(i0)=0.0
else if(method_expand.eq.2) then
    u(i0)=(u(i1)+u(i2))/2.0
else
    u(i0)=0.0
    do i=i1,i2,1
        u(i0)=u(i0)+u(i)
    end do
    u(i0)=u(i0)/(i2-i1+1)
end if
u(i3)=u(i0)
call cos_1d(i0,i1,u(i0))
call cos_1d(i2,i3,u(i2))
    end subroutine expand_cos_1d
    
subroutine cos_1d(i1,i2,u)
integer i1,i2
real u(min(i1,i2):max(i1,i2))
integer i
pai=4.0*atan(1.0)
i1=min(i1,i2)
i2=max(i1,i2)
do i=i1+1,i2-1,1
    u(i)=u(i1)*cos((float((i-i1))/float((i2-i1)))*(pai/2.0))+u(i2)*cos((float((i2-i))/float((i2-i1)))*(pai/2.0))
end do
    end subroutine cos_1d
    
subroutine deriv_operator_sub(dx,dy,m,n,deriv_operator_x,deriv_operator_y,deriv_operator_z)
implicit none
real dx,dy
real dz
integer m,n,i,j
real w(1:m,1:n),u(1:m),v(1:n)
real deriv_operator_x(1:m,1:n)
real deriv_operator_y(1:m,1:n)
real deriv_operator_z(1:m,1:n)
call WAVE2(m,n,dx,dy,u,v,w)
deriv_operator_z=w
do j=1,n,1
    do i=1,m,1
        deriv_operator_x(i,j)=u(i)
        deriv_operator_y(i,j)=v(j)
    end do
end do
    end subroutine deriv_operator_sub
    
!******************************************************************c
!
!  功能：2-D圆频率U和V、径向圆频率W产生子程序
!
!  输入参数说明：
!          dx: x 方向点距          
!          dy: y 方向线距
!           m: 点数（M 必须为 2 的幂次方）
!           n: 线数（N 必须为 2 的幂次方）
!
!  输出参数说明：
!        U(m): x 方向对应的圆频率          
!        V(n): y 方向对应的圆频率          
!      W(m,n): 径向圆频率     
!------------------------------------------------------------------c
    SUBROUTINE WAVE2(m,n,dx,dy,U,V,W)
    implicit none
    INTEGER m,n
    REAL dx,dy
    REAL W(1:m,1:n),U(1:m),V(1:n)
    
    real pi,sx,sy
    integer msh,nsh,i,j,kkx,kky

	pi=3.141592654
	msh=m/2+1
	nsh=n/2+1
	sx=pi*2.0/float(m)/dx
	sy=pi*2.0/float(n)/dy
	do j=1,n,1
	  kky=j
	  if(kky.gt.nsh) kky=kky-n
	  v(j)=sy*(kky-1)
	end do
	do i=1,m,1
	  kkx=i
	  if(kkx.gt.msh) kkx=kkx-m
	  u(i)=sx*(kkx-1)
	end do
	do j=1,n,1
	  do i=1,m,1
	    w(i,j)=sqrt(u(i)*u(i)+v(j)*v(j))
	  end do
	end do

    END SUBROUTINE WAVE2
    
!********************   求导子程序集开始**************************

!    **************求导子程序总模块开始**********
SUBROUTINE deriv(Field_Real,Field_Image,Deriv_operator_x,Deriv_operator_y,Deriv_operator_z,m0,m1,m2,m3,n0,n1,n2,n3,Field_Deriv_method)
    IMPLICIT NONE 
	INTEGER m0,m1,m2,m3,n0,n1,n2,n3
	REAL Field_Real(m0:m3,n0:n3),Field_Image(m0:m3,n0:n3)
	REAL Deriv_operator_x(m0:m3,n0:n3),Deriv_operator_y(m0:m3,n0:n3),Deriv_operator_z(m0:m3,n0:n3)
	INTEGER Field_Deriv_method

	IF(Field_Deriv_method==1) THEN !计算垂向导数

         CALL VDR(Field_Real,Field_Image,m3,n3,Deriv_operator_z)

	ELSE IF(Field_Deriv_method==2) THEN !计算总水平导数

		 call THDR(Field_Real,Field_Image,m3,n3,Deriv_operator_x,Deriv_operator_y)

    ELSE IF(Field_Deriv_method==3) THEN !计算解析信号振幅

	     call ASM_meth(Field_Real,Field_Image,m3,n3,Deriv_operator_x,Deriv_operator_y,Deriv_operator_z)

    ELSE IF(Field_Deriv_method==4) THEN !计算倾斜角

	     CALL TA(Field_Real,Field_Image,m3,n3,Deriv_operator_x,Deriv_operator_y,Deriv_operator_z)

    ELSE IF(Field_Deriv_method==5) THEN !计算垂向二阶导数

	     call VDR_VDR(Field_Real,Field_Image,m3,n3,Deriv_operator_z)

    ELSE IF(Field_Deriv_method==6) THEN !计算倾斜角总水平导数

         CALL TA_THDR(Field_Real,Field_Image,m3,n3,Deriv_operator_x,Deriv_operator_y,Deriv_operator_z)

    ELSE  !计算垂向导数总水平导数
	     
	     call VDR_THDR(Field_Real,Field_Image,m3,n3,Deriv_operator_x,Deriv_operator_y,Deriv_operator_z)		 
	     
    END IF
END SUBROUTINE deriv
!    ************延拓子程序总模块结束**********

!***************VDR*******************
SUBROUTINE VDR(Field_Real,Field_Image,m3,n3,Deriv_operator_z)
	 INTEGER m3,n3
	 REAL Field_Real(1:m3,1:n3),Field_Image(1:m3,1:n3)
   	 REAL Deriv_operator_z(1:m3,1:n3)

	 CALL FFT2(Field_Real,Field_Image,m3,n3,2)  
     CALL multiply_sub(Field_Real,Field_Image,m3,n3,Deriv_operator_z)
	 CALL FFT2(Field_Real,Field_Image,m3,n3,1)
END SUBROUTINE VDR
!*************VDR******************



!************ 相乘运算开始**********
SUBROUTINE multiply_sub(Field_Real,Field_Image,m3,n3,Deriv_operator)
     IMPLICIT NONE
     INTEGER m3,n3,i,j
     REAL Field_Real(1:m3,1:n3),Field_Image(1:m3,1:n3)
     REAL Deriv_operator(1:m3,1:n3)
     
     DO i=1,m3
        DO j=1,n3
           Field_Real(i,j) =Field_Real(i,j) *Deriv_operator(i,j)
           Field_Image(i,j)=Field_Image(i,j)*Deriv_operator(i,j)
        END DO
     END DO

END SUBROUTINE multiply_sub
!********* 相乘运算结束*************

!***************THDR**********************
SUBROUTINE THDR(Field_Real,Field_Image,m3,n3,&
                  Deriv_operator_x,Deriv_operator_y)

	 INTEGER m3,n3,I,J
   	 REAL Deriv_operator_X(1:m3,1:n3),Deriv_operator_y(1:m3,1:n3)
	 REAL Field_Real(1:m3,1:n3)
	 REAL Field_Image(1:m3,1:n3)
	 REAL Field_Real_x(1:m3,1:n3),Field_Image_x(1:m3,1:n3)
	 REAL Field_Real_y(1:m3,1:n3),Field_Image_y(1:m3,1:n3)

 	 CALL FFT2(Field_Real,Field_Image,m3,n3,2)
	 do i=1,m3
	    do j=1,n3
		Field_Real_x(i,j)=-Deriv_operator_X(i,j)*Field_Image(i,j)
        Field_Image_x(i,j)=Deriv_operator_X(i,j)*Field_Real(i,j)
		Field_Real_y(i,j)=-Deriv_operator_y(i,j)*Field_Image(i,j)
        Field_Image_y(i,j)=Deriv_operator_y(i,j)*Field_Real(i,j)		
		end do
     end do  
	 CALL FFT2(Field_Real_x,Field_Image_x,m3,n3,1)
	 CALL FFT2(Field_Real_y,Field_Image_y,m3,n3,1)
     
	 do i=1,m3
	    do j=1,n3
            Field_Real(i,j)=sqrt(Field_Real_x(i,j)**2+Field_Real_y(i,j)**2)
		end do
     end do
END SUBROUTINE THDR
!*****************THDR*********************

!************************ASM_meth********************************
SUBROUTINE ASM_meth(Field_Real,Field_Image,m3,n3,Deriv_operator_x,&
             Deriv_operator_y,Deriv_operator_z)
	 INTEGER m3,n3
	 REAL Field_Real(1:m3,1:n3),Field_Image(1:m3,1:n3)
	 REAL Field_Real_THDR(1:m3,1:n3),Field_Image_THDR(1:m3,1:n3)
	 REAL Field_Real_VDR(1:m3,1:n3),Field_Image_VDR(1:m3,1:n3)
   	 REAL Deriv_operator_z(1:m3,1:n3)
   	 REAL Deriv_operator_X(1:m3,1:n3),Deriv_operator_y(1:m3,1:n3)
     
     Field_Real_THDR=Field_Real
	 Field_Image_THDR=Field_Image
     CALL THDR(Field_Real_THDR,Field_Image_THDR,m3,n3,&
           Deriv_operator_x,Deriv_operator_y)

     Field_Real_VDR=Field_Real
	 Field_Image_VDR=Field_Image 
	 CALL VDR(Field_Real_VDR,Field_Image_VDR,m3,n3,Deriv_operator_z)
     
	 DO i=1,m3
	    do j=1,n3
           Field_Real(i,j)=sqrt(Field_Real_THDR(i,j)**2+Field_Real_VDR(i,j)**2)
	    end do
    end do

END SUBROUTINE ASM_meth
!**************************ASM_meth**********************************

!************************TA******************************************
SUBROUTINE TA(Field_Real,Field_Image,m3,n3,Deriv_operator_x,&
              Deriv_operator_y,Deriv_operator_z)
	 INTEGER m3,n3
	 REAL Field_Real(1:m3,1:n3),Field_Image(1:m3,1:n3)
   	 REAL Deriv_operator_z(1:m3,1:n3)
   	 REAL Deriv_operator_X(1:m3,1:n3),Deriv_operator_y(1:m3,1:n3)
	 REAL Field_Real_THDR(1:m3,1:n3),Field_Image_THDR(1:m3,1:n3)
	 REAL Field_Real_VDR(1:m3,1:n3),Field_Image_VDR(1:m3,1:n3)

     Field_Real_THDR=Field_Real
	 Field_Image_THDR=Field_Image
     CALL THDR(Field_Real_THDR,Field_Image_THDR,m3,n3,&
           Deriv_operator_x,Deriv_operator_y)

     Field_Real_VDR=Field_Real
	 Field_Image_VDR=Field_Image 
	 CALL VDR(Field_Real_VDR,Field_Image_VDR,m3,n3,Deriv_operator_z)

	 DO i=1,m3
	    do j=1,n3
           Field_Real(i,j)=atand(Field_Real_VDR(i,j)/Field_Real_THDR(i,j))
	    end do
     end do
END SUBROUTINE TA
!************************TA******************************************

!**********************VDR_VDR***************************************
SUBROUTINE VDR_VDR(Field_Real,Field_Image,m3,n3,Deriv_operator_z)
     INTEGER m3,n3
	 REAL Field_Real(1:m3,1:n3),Field_Image(1:m3,1:n3)
   	 REAL Deriv_operator_z(1:m3,1:n3)

	 CALL FFT2(Field_Real,Field_Image,m3,n3,2)  
     CALL multiply_sub(Field_Real,Field_Image,m3,n3,Deriv_operator_z)
     CALL multiply_sub(Field_Real,Field_Image,m3,n3,Deriv_operator_z)
	 CALL FFT2(Field_Real,Field_Image,m3,n3,1)
END SUBROUTINE VDR_VDR
!*********************VDR_VDR****************************************

!********************TA_THDR***************************************
SUBROUTINE TA_THDR(Field_Real,Field_Image,m3,n3,Deriv_operator_x,&
              Deriv_operator_y,Deriv_operator_z)
	 INTEGER m3,n3
	 REAL Field_Real(1:m3,1:n3),Field_Image(1:m3,1:n3)
   	 REAL Deriv_operator_z(1:m3,1:n3)
   	 REAL Deriv_operator_X(1:m3,1:n3),Deriv_operator_y(1:m3,1:n3)
	 REAL Field_Real_THDR(1:m3,1:n3),Field_Image_THDR(1:m3,1:n3)
	 REAL Field_Real_TA(1:m3,1:n3),Field_Image_TA(1:m3,1:n3)
     
     Field_Real_TA=Field_Real
	 Field_Image_TA=Field_Image 
	 CALL TA(Field_Real_TA,Field_Image_TA,m3,n3,Deriv_operator_x,Deriv_operator_y,Deriv_operator_z)
     
     Field_Real_THDR=Field_Real_TA
	 Field_Image_THDR=Field_Image
     CALL THDR(Field_Real_THDR,Field_Image_THDR,m3,n3,Deriv_operator_x,Deriv_operator_y)
     Field_Real=Field_Real_THDR

END SUBROUTINE TA_THDR
!*******************TA_THDR*****************************************

!********************VDR_THDR***************************************
SUBROUTINE VDR_THDR(Field_Real,Field_Image,m3,n3,Deriv_operator_x,Deriv_operator_y,Deriv_operator_z)
	 INTEGER m3,n3
	 REAL Field_Real(1:m3,1:n3),Field_Image(1:m3,1:n3)
   	 REAL Deriv_operator_z(1:m3,1:n3)
   	 REAL Deriv_operator_X(1:m3,1:n3),Deriv_operator_y(1:m3,1:n3)
	 REAL Field_Real_THDR(1:m3,1:n3),Field_Image_THDR(1:m3,1:n3)
	 REAL Field_Real_VDR(1:m3,1:n3),Field_Image_VDR(1:m3,1:n3)
     
     Field_Real_VDR=Field_Real
	 Field_Image_VDR=Field_Image 
	 CALL VDR(Field_Real_VDR,Field_Image_VDR,m3,n3,Deriv_operator_z)
     
     Field_Real_THDR=Field_Real_VDR
	 Field_Image_THDR=Field_Image
     CALL THDR(Field_Real_THDR,Field_Image_THDR,m3,n3,Deriv_operator_x,Deriv_operator_y)
     Field_Real=Field_Real_THDR

END SUBROUTINE VDR_THDR
    
!**********************离散Fourier变换子程序集开始 *********

!c******************************************************************c
!c                                                                  c
!c        2-D  FAST FOURIER TRANSFORM FOR COMPLEX FUNCTION          c
!c------------------------------------------------------------------c
!c      DREAL: The real part of the function to be transformed
!c     DIMAGE: The imaginary part of the function to be transformed
!c          M: The number of points. M must be the nu-th power of 2
!c          N: The number of points. N must be the nu-th power of 2
!c         NF: (=1,reverse transform
!c             (=2, normal transform
!c
!c  Author: gesang 
!c    TREAL -- Real part of the working array
!c    TIMAG -- Imaginary part of the working array
!c------------------------------------------------------------------c
        SUBROUTINE FFT2(DREAL,DIMAG,M,N,NF)
        real dreal(m,n),dimag(m,n)
        real,ALLOCATABLE::treal(:),timag(:)

        nmmax=max(m,n)
        allocate(treal(nmmax),timag(nmmax),STAT=ierr)

        DO i=1,m
          IF (n.ne.1) THEN
            do j=1,n
              treal(j)=dreal(i,j)
              timag(j)=dimag(i,j)
            end do
            call fft(treal,timag,n,nf)
            do j=1,n
              dreal(i,j)=treal(j)
              dimag(i,j)=timag(j)
            end do
          END IF
        END DO

        DO j=1,n
          IF(m.ne.1) THEN
            do i=1,m
              treal(i)=dreal(i,j)
              timag(i)=dimag(i,j)
            end do
            call fft(treal,timag,m,nf)
            do i=1,m
              dreal(i,j)=treal(i)
              dimag(i,j)=timag(i)
            end do
          END IF
        END DO

        deallocate(treal,timag,STAT=ierr)

        END SUBROUTINE



!c******************************************************************c
!c                                                                  c
!c        1-D FAST FOURIER TRANSFORM FOR COMPLEX FUNCTION   c
!c------------------------------------------------------------------c
!c    XREAL -- Real part of the function to be transformed          c
!c    XIMAG -- Imaginary part of the function to be transformed     c
!c    N ------ The number of points. N must be the nu-th power of 2 c
!c    NF ----- (=1,reverse transform                                c
!c             (=2, normal transform                                c
!c         (0, 1, ......, n/2-1, n/2, -n/2+1, ......,-1)            c
!c------------------------------------------------------------------c
	SUBROUTINE FFT(XREAL,XIMAG,N,NF)
        real xreal(n),ximag(n)

        nu=int(log(float(n))/0.693147+0.001)
	n2=n/2
	nu1=nu-1
	f=float((-1)**nf)
	k=0

        DO l=1,nu
          DO while (k.lt.n)
            do i=1,n2
              p=ibitr(k/2**nu1,nu)
              arg=6.2831853*p*f/float(n)
              c=cos(arg)
              s=sin(arg)
              k1=k+1
              k1n2=k1+n2
              treal=xreal(k1n2)*c+ximag(k1n2)*s
              timag=ximag(k1n2)*c-xreal(k1n2)*s
              xreal(k1n2)=xreal(k1)-treal
              ximag(k1n2)=ximag(k1)-timag
              xreal(k1)=xreal(k1)+treal
              ximag(k1)=ximag(k1)+timag
              k=k+1
            end do
            k=k+n2
          END DO
          k=0
          nu1=nu1-1
          n2=n2/2
        END DO

        DO k=1,n
          i=ibitr(k-1,nu)+1
          if(i.gt.k) then
            treal=xreal(k)
            timag=ximag(k)
            xreal(k)=xreal(i)
            ximag(k)=ximag(i)
            xreal(i)=treal
            ximag(i)=timag
          end if
        END DO

        IF(nf.ne.1) THEN
          do i=1,n
            xreal(i)=xreal(i)/float(n)
            ximag(i)=ximag(i)/float(n)
          end do
        END IF

        END SUBROUTINE

        FUNCTION IBITR(J,NU)
	j1=j
	itt=0
        do i=1,nu
          j2=j1/2
          itt=itt*2+(j1-2*j2)
          ibitr=itt
          j1=j2
        end do

        end function

!*******  离散Fourier变换子程序集结束 **********

!*******************求导子程序集结束**************************



!**************输出部分数据形成grd文件子程序开始*****
subroutine output_GRD(field,expand_2D_filename,m0,m3,n0,n3,eigval)
integer m0,m3,n0,n3
real eigval
real field(m0:m3,n0:n3)
character*80 expand_2D_filename
real fmin,fmax
fmin=HUGE(fmin)
fmax=-HUGE(fmax)
do j=n0,n3,1
    do i=m0,m3,1
        fmin=min(fmin,field(i,j))
        fmax=max(fmax,field(i,j))
    end do
end do
open(10,file=expand_2D_filename,status='unknown')
write(10,'(A)')'DSAA'
write(10,*) m3-m0+1,n3-n0+1
write(10,*) -(m3-m0),m3-m0
write(10,*) -(n3-n0),n3-n0
write(10,*) fmin,fmax
do j=n0,n3
    write(10,*) (field(i,j),i=m0,m3)
end do
close(10)
    end subroutine

!**********输出部分数据形成grd文件子程序结束********