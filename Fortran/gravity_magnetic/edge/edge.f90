PROGRAM Fre_PoteField_Deriv

    implicit none
    CHARACTER *(80) input_field_filename
    CHARACTER *(80) output_field_filename
    INTEGER  expan_2D__method,num_area,Field_Deriv_method
    INTEGER mpoint,nline
    INTEGER m0,m1,m2,m3
    INTEGER n0,n1,n2,n3
    REAL Xmin,Xmax
    REAL ymin,Ymax
    REAL dx,dy
    REAL,ALLOCATABLE:: Ori_Field(:,:) 
    REAL,ALLOCATABLE:: Field_Real(:,:)
    REAL,ALLOCATABLE:: Field_Image(:,:)    
    REAL,ALLOCATABLE:: Deriv_Field(:,:)  
    REAL,ALLOCATABLE:: Deriv_operator_x(:,:) 
    REAL,ALLOCATABLE:: Deriv_operator_y(:,:) 
    REAL,ALLOCATABLE:: Deriv_operator_z(:,:) !z方向导数因子
!INPUT: 
    !读取文件参数  
    CALL read_cmdinfo(input_field_filename,output_field_filename,expan_2D__method,Field_Deriv_method,num_area)
	!读取点数线数及测区范围
    CALL get_mpoint_and_nline(input_field_filename,mpoint,nline,Xmin,Xmax,&
          Ymin,Ymax)
	!计算扩边端点
    CALL get_expan_num(mpoint,m0,m1,m2,m3,num_area) 
    CALL get_expan_num(nline, n0,n1,n2,n3,num_area) 
    
    ALLOCATE(Ori_Field(m0:m3,n0:n3))
    ALLOCATE(Field_Real(m0:m3,n0:n3))
    ALLOCATE(Field_Image(m0:m3,n0:n3))
    ALLOCATE(Deriv_Field(m0:m3,n0:n3))
    ALLOCATE(Deriv_operator_x(m0:m3,n0:n3))
    ALLOCATE(Deriv_operator_y(m0:m3,n0:n3))
    ALLOCATE(Deriv_operator_z(m0:m3,n0:n3))
    !从网格化文件读入初始场值
    CALL Read_field(input_field_filename,m0,m1,m2,m3,n0,n1,n2,n3,Ori_Field) 

!PROCESS:
    !扩边
    dx=(Xmax-Xmin)/(mpoint-1)
    dy=(Ymax-ymin)/(nline -1)
	CALL expan_2D(m0,m1,m2,m3,n0,n1,n2,n3,Ori_Field,dx,dy,&
          expan_2D__method) !expan_2D__method:扩边方法选择
	!计算导数因子  
    CALL Deriv_operator_sub(dx,dy,m3,n3,Deriv_operator_x,&
          Deriv_operator_y,Deriv_operator_z)

    !求导运算
	Field_Real=Ori_Field
    Field_Image=0.0              
    CALL field_Deriv(Field_Real,Field_Image,Deriv_operator_x,Deriv_operator_y,&
          Deriv_operator_z,m0,m1,m2,m3,n0,n1,n2,n3,Field_Deriv_method)                 
	Deriv_Field=Field_Real

! OUTPUT:
    !输出求导后位场文件
    CALL output_grd(output_field_filename,m0,m1,m2,m3,n0,n1,n2,n3,&
          mpoint,nline,Deriv_Field,Xmin,Xmax,Ymin,Ymax)

    DEALLOCATE (Ori_Field)
    DEALLOCATE (Field_Real)
    DEALLOCATE (Field_Image)
    DEALLOCATE (Deriv_Field)
    DEALLOCATE (Deriv_operator_x)
    DEALLOCATE (Deriv_operator_y)
    DEALLOCATE (Deriv_operator_z)
    END PROGRAM Fre_PoteField_Deriv


!********************************开始****************

!   *********得到输入参数子程序开始***********

SUBROUTINE read_cmdinfo(input_field_filename,output_field_filename,expan_2D__method,Field_Deriv_method,num_area)
    CHARACTER *80 input_field_filename
    CHARACTER *80 output_field_filename
    INTEGER  expan_2D__method,Field_Deriv_method,num_area
    OPEN(10,file='cmd.txt',status='old')
    READ(10,*) input_field_filename
    READ(10,*) output_field_filename
	READ(10,*) num_area
    READ(10,*) expan_2D__method
    READ(10,*) Field_Deriv_method
    CLOSE(10)
END SUBROUTINE read_cmdinfo

!   ******得到输入参数子程序结束******


!****读入grd格式文件中点数和线数及范围开始*****

SUBROUTINE get_mpoint_and_nline(filename,mpoint,nline,&
              Xmin,Xmax,Ymin,Ymax) 
    CHARACTER*(*) filename
	INTEGER mpoint,nline
	REAL Xmin,Xmax,Ymin,Ymax
	INTEGER unit
	CALL get_unit(unit)
    open(unit,file=filename,status='old')
	READ(unit,*)
	READ(unit,*) mpoint,nline
	READ(unit,*) Xmin,Xmax
	READ(unit,*) Ymin,Ymax  
	close(unit)
ENDSUBROUTINE get_mpoint_and_nline

!****读入grd格式文件中点数和线数及范围结束********


!**********得到扩边端点子程序开始************
SUBROUTINE get_expan_num(mpoint,m0,m1,m2,m3,flag)
    IMPLICIT NONE
    INTEGER  mtemp,factor_m,mu
	INTEGER  mpoint,m0,m1,m2,m3
	INTEGER  flag
	mtemp=mpoint
	factor_m=1
	DO WHILE ((mod(mtemp,2).eq.0).and.(mtemp.ne.0))
	    mtemp=mtemp/2
	End do
	IF (mtemp.eq.1) THEN
	    m3=mpoint*2
	ELSE
        mu=int(log(float(mpoint))/0.693147+factor_m)
        m3=2**mu
		
		if(flag==1) then
		     m3=m3*2   !计算区域为原来倍
	    else 
	    
		endif
	END IF
	m1=1+(m3-mpoint)/2
	m2=m1+mpoint-1
	m0=1

END SUBROUTINE get_expan_num

!*******得到扩边端点子程序结束*************


!*****读入grd格式文件中场值子程序开始********

SUBROUTINE Read_field(filename,m0,m1,m2,m3,n0,n1,n2,n3,G)
    PARAMETER (vial=1.701411e+38)
    CHARACTER*(*) filename
	INTEGER m0,m1,m2,m3,n0,n1,n2,n3
	REAL  G(m0:m3,n0:n3)
	INTEGER unit
	
	CALL get_unit(unit)
	G=vial
	open(unit,file=filename)
    DO i=1,5
	   READ(unit,*)
	ENDDO
	READ(unit,*) ((G(i,j),i=m1,m2),j=n1,n2)
	CLOSE(unit)
ENDSUBROUTINE Read_field
!*****读入grd格式文件中场值子程序结束********


!**************扩边子程序集开始********************************

!*****扩边子程序调用主子程序开始*****
SUBROUTINE expan_2D(m0,m1,m2,m3,n0,n1,n2,n3,&
              Ori_Field,dx,dy,expan_2D__method)
    INTEGER m0,m1,m2,m3
    INTEGER n0,n1,n2,n3
    REAL Ori_Field(m0:m3,n0:n3)
    INTEGER expan_2D__method
    REAL dx,dy
    
    IF(expan_2D__method<=3) THEN
        CALL expan_cos2(m0,m1,m2,m3,n0,n1,n2,n3,&
              Ori_Field,expan_2D__method)
    ELSE
        CALL MinCurv(Ori_Field,m0,m1,m2,m3,n0,n1,n2,n3,&
              dx,dy,expan_2D__method)        
    END IF
END SUBROUTINE expan_2D
!*****扩边子程序调用主子程序结束*****

!*********2D最小曲率扩边子程序开始***********
SUBROUTINE MinCurv(Ori_Field,m0,m1,m2,m3,n0,n1,n2,n3,dx,dy,flag)
    INTEGER m0,m1,m2,m3,n0,n1,n2,n3
    REAL Ori_Field(m0:m3,n0:n3) 
    REAL dx,dy
    INTEGER num !空白点点数
    INTEGER ,ALLOCATABLE::P_POINT(:),P_LINE(:)
    INTEGER  flag
    REAL eigval
        eigval=1.701411e+38  
        CALL Blank_Point_number(Ori_Field,m3,n3,num,eigval)

        ALLOCATE(P_POINT(1:num))
		ALLOCATE(P_LINE(1:num))
        CALL Blank_Point_position(Ori_Field,m3,n3,num,eigval,P_POINT,P_LINE)  
        CALL expan_cos2(m0,m1,m2,m3,n0,n1,n2,n3,Ori_Field,flag-3) 
        !余弦扩边作为空白部分初值及端点值
        !****2D网格数据无约束最小曲率迭代
        CALL  MinCurV_2D_net_sub(1E-4,10000,dx,dy,m3,n3,&
                Ori_Field,num,P_POINT,P_LINE)
        

END SUBROUTINE MinCurv
!*********2D最小曲率扩边子程序结束***********

!****获得数据中的空白点数开始*****************
SUBROUTINE Blank_Point_number(FIELD,mpoint,line,bpn,eigval)
	IMPLICIT NONE
	INTEGER mpoint,line,bpn,i,j
	REAL FIELD(1:mpoint,1:line),eigval
	bpn=0
	DO i=1,mpoint,1
	 DO j=1,line,1
	  IF(FIELD(i,j)>=0.9*eigval) bpn=bpn+1
	 ENDDO
	ENDDO
ENDSUBROUTINE
!****获得数据中的空白点数结束*****************

!****获得数据中的空白点位置开始********************
SUBROUTINE Blank_Point_position(FIELD,mpoint,line,bpn,eigval,P_POINT,P_LINE)
	IMPLICIT NONE
	INTEGER mpoint,line,bpn,i,j,k
	INTEGER P_POINT(1:bpn),P_LINE(1:bpn)
	REAL FIELD(1:mpoint,1:line),eigval
	k=1
	DO i=1,mpoint,1
	 DO j=1,line,1
	  IF(FIELD(i,j)>=0.9*eigval.AND.j<bpn) THEN
	   P_POINT(k)=i
	   P_LINE(k)=j
	   k=k+1
	  ENDIF
	 ENDDO
	ENDDO
	ENDSUBROUTINE
!****获得数据中的空白点位置结束********************

!****2D无约束最小曲率迭代边界处理开始******
SUBROUTINE MinCurV_2D_boundary(U,mpoint,line,alph)
	REAL U(1-2:mpoint+2,1-2:line+2)

	DO j=1,line,1
	 U(1-1,j)=2*U(1,j)-U(1+1,j)
	 U(mpoint+1,j)=2*U(mpoint,j)-U(mpoint-1,j)
	ENDDO

	DO i=1,mpoint,1
	 U(i,1-1)=2*U(i,1)-U(i,1+1)
	 U(i,line+1)=2*U(i,line)-U(i,mpoint-1)
	ENDDO

	U(1-1,1-1)=U(1+1,1-1)+U(1-1,1+1)-U(1+1,1+1)
	U(mpoint+1,1-1)=U(mpoint+1,1+1)+U(mpoint-1,1-1)-U(mpoint-1,1+1)
	U(1-1,line+1)=U(1+1,line+1)+U(1-1,line-1)-U(1+1,line-1)
	U(mpoint+1,line+1)=U(mpoint+1,line-1)+U(mpoint-1,line+1)-U(mpoint-1,line-1)

	i=1
	alph1=alph**2
	alph2=-2*(1+alph1)
	DO j=1,line
	 pij=alph1*(U(i+1,j+1)-U(i-1,j+1)+U(i+1,j-1)-U(i-1,j-1))+alph2*(U(i+1,j)-U(i-1,j))
	 U(i-2,j)=U(i+2,j)+pij
	ENDDO

	i=mpoint
	DO j=1,line
	 pij=alph1*(U(i+1,j+1)-U(i-1,j+1)+U(i+1,j-1)-U(i-1,j-1))+alph2*(U(i+1,j)-U(i-1,j))
	 U(i+2,j)=U(i-2,j)-pij
	ENDDO

	j=1
	beta=1./alph
	beta1=beta*beta
	beta2=-2*(1+beta1)
	DO i=1,mpoint,1
	 qij=beta1*(U(i+1,j+1)-U(i+1,j-1)+U(i-1,j+1)-U(i-1,j-1))+beta2*(U(i,j+1)-U(i,j-1))
	 U(i,j-2)=U(i,j+2)+qij
	ENDDO
	j=line
	DO i=1,mpoint,1
	 qij=beta1*(U(i+1,j+1)-U(i+1,j-1)+U(i-1,j+1)-U(i-1,j-1))+beta2*(U(i,j+1)-U(i,j-1))
	 U(i,j+2)=U(i,j-2)-qij
	ENDDO
ENDSUBROUTINE MinCurV_2D_boundary
!****2D无约束最小曲率迭代边界处理结束******


!****2D网格数据无约束最小曲率迭代开始**************
SUBROUTINE MinCurV_2D_net_sub(eps_abs,iteration_max,dx,dy,&
                mpoint,line,FIELD,number_eigval,M_eigval,N_eigval)
	REAL eps_abs,dx,dy
	INTEGER iteration_max,mpoint,line,number_eigval
	REAL FIELD(1:mpoint,1:line)
	INTEGER M_eigval(1:number_eigval),N_eigval(1:number_eigval)
	REAL,ALLOCATABLE::U(:,:)

	ALLOCATE(U(1-2:mpoint+2,1-2:line+2))

	DO j=1,line,1
	 DO i=1,mpoint,1
	     U(i,j)=FIELD(i,j)
	  ENDDO
	ENDDO
	
	eps_error=2*ABS(eps_abs)
	iteration=0
	
	alph=dx/dy
	alph0=-1./(2*(3+4*alph**2+3*alph**2)) 
	alph1=alph**4
	alph2=2*alph**2
	alph3=-4*(1+alph**2)
	alph4=-4*(1+alph**2)*alph**2

	DO WHILE((eps_error>eps_abs).and.(iteration<iteration_max))
	 eps_error=0.
	 CALL MinCurV_2D_boundary(U,mpoint,line,alph)
	 DO k=1,number_eigval,1
	  i=M_eigval(k)
	  j=N_eigval(k)
	  temp=(U(i+2,j)+U(i-2,j))+alph1*(U(i,j+2)+U(i,j-2))+ &
         alph2*(U(i+1,j+1)+U(i-1,j+1)+U(i+1,j-1)+U(i-1,j-1))+ &
         alph3*(U(i+1,j)+U(i-1,j))+alph4*(U(i,j+1)+U(i,j-1))
	  temp=temp*alph0
	  eps_error=MAX(ABS(temp-U(i,j)),eps_error)
	  U(i,j)=temp
	 ENDDO
	 iteration=iteration+1
	ENDDO
	print*,iteration,eps_error

	DO j=1,line,1
	 DO i=1,mpoint,1
	   FIELD(i,j)=U(i,j)
	  ENDDO
	ENDDO
	deALLOCATE(U,STAT=ierr)
ENDSUBROUTINE


!**2D网格数据无约束最小曲率迭代结束********


!***************2D余弦扩边开始*******
SUBROUTINE  expan_cos2(m1,m2,m3,m4,n1,n2,n3,n4,G,flag)
    PARAMETER (pi=3.141592654)
    INTEGER flag
    INTEGER m1,m2,m3,m4
    INTEGER n1,n2,n3,n4
    REAL G(m1:m4,n1:n4)
    REAL G1(m1:m4,n1:n4)
    REAL G2(m1:m4,n1:n4)
    REAL sum
    INTEGER num
    sum=0.0
    num=0
    IF(flag==1) then   !扩边端点值取边界平均值
        DO i=m2,m3
            sum=sum+G(i,n2)+G(i,n3) 
            num=num+2          
        END DO
        DO i=n2+1,n3-1
            sum=sum+G(m2,i)+G(m3,i)
            num=num+2
        END DO        
        DO i=m1,m4
            G(i,n1)=sum/num
            G(i,n4)=sum/num
        END DO
        DO i=n1+1,n4-1
            G(m1,i)=sum/num
            G(m4,i)=sum/num
        END DO
   
    ELSE IF(flag==2) then !扩边端点值取全部数据平均值
        DO i=m2,m3
           DO j=n2,n3
               sum=sum+G(i,j)
               num=num+1           
           END DO
        END DO
        DO i=m1,m4
            G(i,n1)=sum/num
            G(i,n4)=sum/num
        END DO
        DO i=n1+1,n4-1
            G(m1,i)=sum/num
            G(m4,i)=sum/num
        END DO
        
    
    ELSE IF(flag==3) then !扩边端点值取常数，
         DO i=m1,m4
            G(i,n1)=0
            G(i,n4)=0
        END DO
        DO i=n1+1,n4-1
            G(m1,i)=0
            G(m4,i)=0
        END DO
    END IF
!扩边
    G1=G
    G2=G    
    DO j=n2,n3
         DO i=m1+1,m2-1
            G1(i,j)=(G1(m2,j)-G1(m1,j))*cos((m2-i)*1.0/(m2-m1)*pi/2.0)+G1(m1,j)
         END DO
         DO i=m3+1,m4-1
            G1(i,j)=(G1(m4,j)-G1(m3,j))*cos((m4-i)*1.0/(m4-m3)*pi/2.0)+G1(m3,j)
         END DO
    END DO
    
    DO i=m1,m4
         DO j=n1+1,n2-1
            G1(i,j)=(G1(i,n2)-G1(i,n1))*cos((n2-j)*1.0/(n2-n1)*pi/2.0)+G1(i,n1)
         END DO
         DO j=n3+1,n4-1
            G1(i,j)=(G1(i,n4)-G1(i,n3))*cos((n4-j)*1.0/(n4-n3)*pi/2.0)+G1(i,n3)
         END DO
    END DO
    
    DO i=m2,m3
         DO j=n1+1,n2-1
            G2(i,j)=(G2(i,n2)-G2(i,n1))*cos((n2-j)*1.0/(n2-n1)*pi/2.0)+G2(i,n1)
         END DO
         DO j=n3+1,n4-1
            G2(i,j)=(G2(i,n4)-G2(i,n3))*cos((n4-j)*1.0/(n4-n3)*pi/2.0)+G2(i,n3)
         END DO
    END DO  
    
    DO j=n1,n4
         DO i=m1+1,m2-1
            G2(i,j)=(G2(m2,j)-G2(m1,j))*cos((m2-i)*1.0/(m2-m1)*pi/2.0)+G2(m1,j)
         END DO
         DO i=m3+1,m4-1
            G2(i,j)=(G2(m4,j)-G2(m3,j))*cos((m4-i)*1.0/(m4-m3)*pi/2.0)+G2(m3,j)
         END DO
    END DO
    
    G=(G1+G2)/2.0

END SUBROUTINE expan_cos2
!***************2D余弦扩边开始*******

!**************扩边子程序集结束*******************************

!************计算导数因子开始*****************
SUBROUTINE Deriv_operator_sub(dx,dy,m,n,Deriv_operator_x,Deriv_operator_y,Deriv_operator_z) 
	IMPLICIT NONE
	REAL dx,dy
	REAL dz
	INTEGER m,n,i,j
	REAL W(1:m,1:n),U(1:m),V(1:n)
	REAL Deriv_operator_Z(1:m,1:n)
	REAL Deriv_operator_x(1:m,1:n)
	REAL Deriv_operator_y(1:m,1:n)
	
	CALL WAVE2D_sub(U,V,W,m,n,dx,dy)
                         !计算垂向导数因子,实数
	Deriv_operator_z=W
                         !计算X和y导数因子，虚数
     do j=1,n
        do i=1,m
        Deriv_operator_x(i,j)=U(i)
        Deriv_operator_y(i,j)=V(j)
        end do 
     end do
 
END SUBROUTINE Deriv_operator_sub
	
SUBROUTINE WAVE2D_sub(U,V,W,m,n,dx,dy)
      REAL W(1:m,1:n),U(1:m),V(1:n)
      INTEGER m,n
      REAL dx,dy
      REAL i,j
      
      CALL Wave1D_sub(n,dy,V)
      CALL Wave1D_sub(m,dx,U)
      DO j=1,n   !计算园频率
            DO i=1,m
                 W(i,j)=SQRT(U(i)*U(i)+V(j)*V(j))
            END DO
      END DO
END SUBROUTINE WAVE2D_sub

Subroutine Wave1D_sub(N,dy,V)
     REAL dy
     INTEGER N
     REAL V(0:N-1) 
     REAL deltf
     deltf=(2.0*3.141592654)/(N*dy)
     Do j=0,N/2,1
          V(j)=j*deltf
     End do
     Do j=N/2+1,N-1,1
          V(j)=(j-n)*deltf
     End do
END subroutine Wave1D_sub
!************计算导数因子子程序结束*****************


!********************   求导子程序集开始**************************

!    **************求导子程序总模块开始**********
SUBROUTINE field_Deriv(Field_Real,Field_Image,Deriv_operator_x,Deriv_operator_y,Deriv_operator_z,m0,m1,m2,m3,n0,n1,n2,n3,Field_Deriv_method)
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
END SUBROUTINE field_Deriv
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
SUBROUTINE THDR(Field_Real,Field_Image,m3,n3,Deriv_operator_x,Deriv_operator_y)

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
SUBROUTINE ASM_meth(Field_Real,Field_Image,m3,n3,Deriv_operator_x,Deriv_operator_y,Deriv_operator_z)
	 INTEGER m3,n3
	 REAL Field_Real(1:m3,1:n3),Field_Image(1:m3,1:n3)
	 REAL Field_Real_THDR(1:m3,1:n3),Field_Image_THDR(1:m3,1:n3)
	 REAL Field_Real_VDR(1:m3,1:n3),Field_Image_VDR(1:m3,1:n3)
   	 REAL Deriv_operator_z(1:m3,1:n3)
   	 REAL Deriv_operator_X(1:m3,1:n3),Deriv_operator_y(1:m3,1:n3)
     
     Field_Real_THDR=Field_Real
	 Field_Image_THDR=Field_Image
     CALL THDR(Field_Real_THDR,Field_Image_THDR,m3,n3,Deriv_operator_x,Deriv_operator_y)

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
SUBROUTINE TA(Field_Real,Field_Image,m3,n3,Deriv_operator_x,Deriv_operator_y,Deriv_operator_z)
	 INTEGER m3,n3
	 REAL Field_Real(1:m3,1:n3),Field_Image(1:m3,1:n3)
   	 REAL Deriv_operator_z(1:m3,1:n3)
   	 REAL Deriv_operator_x(1:m3,1:n3),Deriv_operator_y(1:m3,1:n3)
	 REAL Field_Real_THDR(1:m3,1:n3),Field_Image_THDR(1:m3,1:n3)
	 REAL Field_Real_VDR(1:m3,1:n3),Field_Image_VDR(1:m3,1:n3)

     Field_Real_THDR=Field_Real
	 Field_Image_THDR=Field_Image
     CALL THDR(Field_Real_THDR,Field_Image_THDR,m3,n3,Deriv_operator_x,Deriv_operator_y)

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
SUBROUTINE TA_THDR(Field_Real,Field_Image,m3,n3,Deriv_operator_x,Deriv_operator_y,Deriv_operator_z)
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
   	 REAL Deriv_operator_x(1:m3,1:n3),Deriv_operator_y(1:m3,1:n3)
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
!*******************VDR_THDR*****************************************


!*******************************************************************

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
SUBROUTINE output_grd(outputfilename,m0,m1,m2,m3,n0,n1,n2,n3,&
              mpoint,nline,G,Xmin,Xmax,Ymin,Ymax)
    INTEGER m0,m1,m2,m3
    INTEGER n0,n1,n2,n3
    INTEGER mpoint,nline
	CHARACTER*(*) outputfilename
	REAL Xmin,Xmax,Ymin,Ymax
	REAL Gmin,Gmax,G(m0:m3,n0:n3)
    INTEGER unit
    Gmin=G(m1,n1)
    Gmax=G(m1,n1)
    DO i=m1,m2
       DO j= n1,n2
          Gmin=min(Gmin,G(i,j))
          Gmax=max(Gmax,G(i,j))
       END DO
    END DO
    
    CALL get_unit(unit)
	open(unit,file=outputfilename,status='unknown')
	WRITE(unit,"(a)")'DSAA'
	WRITE(unit,*) mpoint,nline
    WRITE(unit,*) Xmin,Xmax
	WRITE(unit,*) Ymin,Ymax
	WRITE(unit,*) Gmin,Gmax
	WRITE(unit,100) ((G(i,j),i=m1,m2),j=n1,n2)
100 format(<4>f15.6)
    CLOSE(unit)
END SUBROUTINE output_grd

!**********输出部分数据形成grd文件子程序结束********


!**********辅助子程序获得空闲文件号子程序开始*******
subroutine get_unit ( iunit )

  implicit none
  integer  i
  integer  ios
  integer  iunit
  logical  lopen

  iunit = 0
  do i = 1, 99

    if ( i /= 5 .and. i /= 6 .and. i /= 9 ) then
      inquire ( unit = i, opened = lopen, iostat = ios )
      if ( ios == 0 ) then
        if ( .not. lopen ) then
          iunit = i
          return
        end if
      end if
    end if
  end do
  return
end