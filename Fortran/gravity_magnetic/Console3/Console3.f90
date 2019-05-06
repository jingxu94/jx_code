    !  console3.f90 
    !
    !  ����:����Ƶ����λ������
    !  ���ߣ�����
    !  ��λ��������ѧ

    !****************************************************************************
    !����˵����
    !���Ʋ����ļ��ļ�����cmd.txt
    !�����ļ�����a20_mag.grd,a53_mag.grd
    !�����ļ�����expand.grd
    !������ؼ������ļ�����expand_conti.grd
    !elevation:���ظ߲�
    !f0:��ֵʵ��
    !f1:��ֵ�鲿
    !eigval:����ͼ�����
    !fcount_real:���س�ֵʵ��
    !fcount_image:���س�ֵ�鲿
    !u:x�����Ӧ��ԲƵ��          
    !v:y�����Ӧ��ԲƵ��          
    !w:����ԲƵ��
    !mpoint:����
    !nline:����
    !m:����fftʱ����ĵ�����2��n�η�
    !n:����fftʱ�����������2��n�η�
    !****************************************************************************

    program continuation

    integer mpoint,nline,m0,m1,m2,m3,n0,n1,n2,n3,m,n,method_expand,field_deriv_method
    real elevation,eigval,xmin,xmax,ymin,ymax,dx,dy
    character*80 cmdfile,input_filename,output_filename,expand_2d_filename

    real,allocatable::field(:,:),f0(:,:),f1(:,:)
    real,allocatable::u(:),v(:),w(:,:),fcount_real(:,:),fcount_image(:,:)
    real,allocatable::deriv_operator_x(:,:),deriv_operator_y(:,:),deriv_operator_z(:,:),deriv_field(:,:)

    cmdfile='cmd.txt'

    call read_cmd(cmdfile,elevation,input_filename,expand_2d_filename,output_filename,eigval,method_expand,field_deriv_method)

    call read_mn(input_filename,mpoint,nline,xmin,xmax,ymin,ymax)

    call calculate_m1m2_dx(mpoint,m0,m1,m2,m3,m,xmin,xmax,dx)

    call calculate_m1m2_dx(nline,n0,n1,n2,n3,n,ymin,ymax,dy)

    allocate(u(m0:m3),v(n0:n3),w(m0:m3,n0:n3),fcount_real(m0:m3,n0:n3),fcount_image(m0:m3,n0:n3))
    allocate(field(m0:m3,n0:n3),f0(m0:m3,n0:n3),f1(m0:m3,n0:n3),deriv_operator_x(m0:m3,n0:n3),deriv_operator_y(m0:m3,n0:n3),deriv_operator_z(m0:m3,n0:n3),deriv_field(m0:m3,n0:n3))

    call input_grd(input_filename,m0,m1,m2,m3,n0,n1,n2,n3,m,n,field,eigval)

    call expand_cos_2d(field,m0,m1,m2,m3,n0,n1,n2,n3,method_expand)


    f0=field
    f1=0.0

    !���㵼������  
    call deriv_operator_sub(dx,dy,m3,n3,deriv_operator_x,deriv_operator_y,deriv_operator_z)

    !������            
    call field_deriv(f0,f1,deriv_operator_x,deriv_operator_y,deriv_operator_z,m0,m1,m2,m3,n0,n1,n2,n3,field_deriv_method)                 
    deriv_field=f0

    ! output:
    !����󵼺�λ���ļ�

    call output_grd(deriv_field,output_filename,m0,m3,n0,n3,m,n,eigval,xmin,xmax,ymin,ymax)

    deallocate(field,f0,f1,u,v,w,fcount_real,fcount_image)

    end program

    subroutine read_cmd(cmdfile,elevation,input_filename,expand_2d_filename,output_filename,eigval,method_expand,field_deriv_method)
    real elevation,eigval
    character*80 cmdfile,input_filename,expand_2d_filename,output_filename
    integer method_expand,field_deriv_method
    open(10,file=cmdfile,status='old')
    read(10,*) elevation
    read(10,*) input_filename
    read(10,*) expand_2d_filename
    read(10,*) output_filename
    read(10,*) eigval
    read(10,*) method_expand
    read(10,*) field_deriv_method
    close(10)
    end subroutine

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
        mu=int(log(float(mpoint))/0.693147+factor_m)
        m=2**mu
    end if
    m1=1+(m-mpoint)/2
    m2=m1+mpoint-1
    m3=m
    end subroutine

    subroutine input_grd(input_filename,m0,m1,m2,m3,n0,n1,n2,n3,m,n,field,eigval)
    character*80 input_filename
    integer m0,m1,m2,m3,n0,n1,n2,n3,m,n
    real eigval
    real field(m0:m3,n0:n3)
    field=eigval
    open(10,file=input_filename,form='formatted')
    read(10,*)
    read(10,*) m,n
    read(10,*) xmin,xmax
    read(10,*) ymin,ymax
    read(10,*)
    read(10,*) ((field(i,j),i=m1,m2,1),j=n1,n2,1)
    close(10)
    end subroutine

    subroutine expand_2d(field,m0,m1,m2,m3,n0,n1,n2,n3,nline)
    integer m0,m1,m2,m3,n0,n1,n2,n3
    real field(m0:m3,n0:n3)
    real::pai=3.141592654
    do i=n1,n2,1
        field(m0,i)=(field(m1,i)+field(m2,i))/2
        field(m3,i)=field(m0,i)
    end do
    do j=n1,n2,1
        do i=m0+1,m1-1,1
            field(i,j)=field(m0,j)+cos(float(m1-m0)*pai/2.0)*(field(m1,j)-field(m0,j))
        end do
        do i=m2+1,m3-1,1
            field(i,j)=field(m2,j)+cos(float(m3-m2)*pai/2.0)*(field(m3,j)-field(m2,j))
        end do
    end do
    do i=m0,m3,1
        field(i,n0)=(field(i,n1)+field(i,n2))/2
        field(i,n3)=field(i,n0)
    end do
    do i=m0,m3,1
        do j=n0+1,n1-1,1
            field(i,j)=field(i,n0)+cos(pai/2.0*float((n1-j))/float((n1-n0)))*(field(i,n1)-field(i,n0))
        end do
        do j=n2+1,n3-1,1
            field(i,j)=field(i,n2)+cos(pai/2.0*float((n3-j))/float((n3-n2)))*(field(i,n3)-field(i,n2))
        end do
    end do
    end subroutine

    subroutine output_grd(field,filename,m1,m2,n1,n2,m,n,eigval,xmin,xmax,ymin,ymax)
    integer m1,m2,n1,n2,m,n
    real eigval
    real field(m1:m2,n1:n2)
    character*80 filename
    real fmin,fmax
    real xmin,xmax,ymin,ymax
    fmin=huge(fmin)
    fmax=-huge(fmax)
    do j=n1,n2,1
        do i=m1,m2,1
            fmin=min(fmin,field(i,j))
            fmax=max(fmax,field(i,j))
        end do
    end do
    open(10,file=filename,status='unknown')
    write(10,'(a)')'dsaa'
    write(10,*) m,n
    write(10,*) xmin,xmax
    write(10,*) ymin,ymax
    write(10,*) fmin,fmax
    do j=n1,n2,1
        write(10,*) (field(i,j),i=m1,m2,1)
    end do
    close(10)
    end subroutine

    !******************  ��ɢ����fourier�任�ӳ��򼯿�ʼ  *******************

    !******************************************************************c
    !
    !  ���ܣ�������2-d����fourier�任
    !
    !  �������˵����
    !    freal(m,n): ��������ʵ��          
    !   fimage(m,n): ���������鲿     
    !             m: ������m ����Ϊ 2 ���ݴη���
    !             n: ������n ����Ϊ 2 ���ݴη���
    !            nf: �������任��־��(1:���任;2:���任)
    !
    !  �������˵����
    !    freal(m,n): �任��Ƶ��ʵ��          
    !   fimage(m,n): �任��Ƶ���鲿     
    !
    !  ��ӦƵ�ʷֲ�˵����
    !      ����freal(m,n)��fimage(m,n)��Ӧ��Ƶ�ʷֲ�λ��Ϊ:
    !      m ���� 0,1,.......,m/2-1,m/2,-(m/2-1),......,-1
    !      n ���� 0,1,.......,n/2-1,n/2,-(n/2-1),......,-1
    !------------------------------------------------------------------c
    subroutine fft2(freal,fimage,m,n,nf)
    implicit none
    integer m,n,nf
    real freal(1:m,1:n),fimage(1:m,1:n)

    real,allocatable::treal(:),timage(:)
    integer nmmax,ierr,i,j

    nmmax=max(m,n)
    allocate(treal(1:nmmax),timage(1:nmmax),stat=ierr)
    if(ierr.ne.0) stop '����������stop!!'

    do i=1,m,1
        if (n.ne.1) then
            do j=1,n,1
                treal(j)=freal(i,j)
                timage(j)=fimage(i,j)
            end do
            call fft(treal,timage,n,nf)
            do j=1,n,1
                freal(i,j)=treal(j)
                fimage(i,j)=timage(j)
            end do
        end if
    end do

    do j=1,n,1
        if(m.ne.1) then
            do i=1,m,1
                treal(i)=freal(i,j)
                timage(i)=fimage(i,j)
            end do
            call fft(treal,timage,m,nf)
            do i=1,m,1
                freal(i,j)=treal(i)
                fimage(i,j)=timage(i)
            end do
        end if
    end do

    deallocate(treal,timage,stat=ierr)

    end subroutine fft2

    !******************************************************************c
    !                                                                  c
    !  ���ܣ�������1-d����fourier�任
    !
    !  �������˵����
    !      freal(n): ��������ʵ��          
    !     fimage(n): ���������鲿     
    !             n: ������m ����Ϊ 2 ���ݴη���
    !            nf: �������任��־��(1:���任;2:���任)
    !
    !  �������˵����
    !      freal(n): �任��Ƶ��ʵ��          
    !     fimage(n): �任��Ƶ���鲿     
    !
    !  ��ӦƵ�ʷֲ�˵����
    !      ����freal(n)��fimage(n)��Ӧ��Ƶ�ʷֲ�λ��Ϊ:
    !       0,1,.......,n/2-1,n/2,-(n/2-1),......,-1
    !------------------------------------------------------------------c
    subroutine fft(xreal,ximage,n,nf)
    implicit none
    integer n,nf
    real xreal(1:n),ximage(1:n)

    integer nu,n2,nu1,k,k1,k1n2,l,i,ibitr
    real f,p,arg,c,s,treal,timage

    nu=int(log(float(n))/0.693147+0.001)
    n2=n/2
    nu1=nu-1
    f=float((-1)**nf)
    k=0

    do l=1,nu,1
        do while (k.lt.n)
            do i=1,n2,1
                p=ibitr(k/2**nu1,nu)
                arg=6.2831853*p*f/float(n)
                c=cos(arg)
                s=sin(arg)
                k1=k+1
                k1n2=k1+n2
                treal=xreal(k1n2)*c+ximage(k1n2)*s
                timage=ximage(k1n2)*c-xreal(k1n2)*s
                xreal(k1n2)=xreal(k1)-treal
                ximage(k1n2)=ximage(k1)-timage
                xreal(k1)=xreal(k1)+treal
                ximage(k1)=ximage(k1)+timage
                k=k+1
            end do
            k=k+n2
        end do
        k=0
        nu1=nu1-1
        n2=n2/2
    end do

    do k=1,n,1
        i=ibitr(k-1,nu)+1
        if(i.gt.k) then
            treal=xreal(k)
            timage=ximage(k)
            xreal(k)=xreal(i)
            ximage(k)=ximage(i)
            xreal(i)=treal
            ximage(i)=timage
        end if
    end do

    if(nf.ne.1) then
        do i=1,n,1
            xreal(i)=xreal(i)/float(n)
            ximage(i)=ximage(i)/float(n)
        end do
    end if

    end subroutine fft

    function ibitr(j,nu)
    implicit none
    integer ibitr,j,nu
    integer j1,itt,i,j2
    j1=j
    itt=0
    do i=1,nu,1
        j2=j1/2
        itt=itt*2+(j1-2*j2)
        ibitr=itt
        j1=j2
    end do

    end function ibitr    

    !******************************************************************c
    !
    !  ���ܣ�2-dԲƵ��u��v������ԲƵ��w�����ӳ���
    !
    !  �������˵����
    !          dx: x ������          
    !          dy: y �����߾�
    !           m: ������m ����Ϊ 2 ���ݴη���
    !           n: ������n ����Ϊ 2 ���ݴη���
    !
    !  �������˵����
    !        u(m): x �����Ӧ��ԲƵ��          
    !        v(n): y �����Ӧ��ԲƵ��          
    !      w(m,n): ����ԲƵ��     
    !------------------------------------------------------------------c
    subroutine wave2(m,n,dx,dy,u,v,w)
    implicit none
    integer m,n
    real dx,dy
    real w(1:m,1:n),u(1:m),v(1:n)

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

    end subroutine wave2

    subroutine factor_continuation(elevation,m0,m3,n0,n3,u,v,w,fcount_real,fcount_image)
    integer m0,m3,n0,n3
    real elevation
    real u(m0:m3),v(n0:n3),w(m0:m3,n0:n3),fcount_real(m0:m3,n0:n3),fcount_image(m0:m3,n0:n3)
    do j=n0,n3,1
        do i=m0,m3,1
            fcount_real(i,j)=exp(-w(i,j)*elevation)
        end do
    end do
    end subroutine factor_continuation

    subroutine multi_sub(f0,f1,fcount_real,fcount_image,m0,m3,n0,n3)
    integer m0,m3,n0,n3
    real f0(m0:m3,n0:n3),f1(m0:m3,n0:n3),fcount_real(m0:m3,n0:n3),fcount_image(m0:m3,n0:n3)
    do j=n0,n3,1
        do i=m0,m3,1
            f0(i,j)=fcount_real(i,j)*f0(i,j)
            f1(i,j)=fcount_real(i,j)*f1(i,j)
        end do
    end do
    end subroutine multi_sub

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

    !********************   ���ӳ��򼯿�ʼ**************************

    !    **************���ӳ�����ģ�鿪ʼ**********
    subroutine field_deriv(field_real,field_image,deriv_operator_x,deriv_operator_y,deriv_operator_z,m0,m1,m2,m3,n0,n1,n2,n3,field_deriv_method)
    implicit none 
    integer m0,m1,m2,m3,n0,n1,n2,n3
    real field_real(m0:m3,n0:n3),field_image(m0:m3,n0:n3)
    real deriv_operator_x(m0:m3,n0:n3),deriv_operator_y(m0:m3,n0:n3),deriv_operator_z(m0:m3,n0:n3)
    integer field_deriv_method

    if(field_deriv_method==1) then !���㴹����

    call vdr(field_real,field_image,m3,n3,deriv_operator_z)

    else if(field_deriv_method==2) then !������ˮƽ����

    call thdr(field_real,field_image,m3,n3,deriv_operator_x,deriv_operator_y)

    else if(field_deriv_method==3) then !��������ź����

    call asm_meth(field_real,field_image,m3,n3,deriv_operator_x,deriv_operator_y,deriv_operator_z)

    else if(field_deriv_method==4) then !������б��

    call ta(field_real,field_image,m3,n3,deriv_operator_x,deriv_operator_y,deriv_operator_z)

    else if(field_deriv_method==5) then !���㴹����׵���

    call vdr_vdr(field_real,field_image,m3,n3,deriv_operator_z)

    else if(field_deriv_method==6) then !������б����ˮƽ����

    call ta_thdr(field_real,field_image,m3,n3,deriv_operator_x,deriv_operator_y,deriv_operator_z)

    else  !���㴹������ˮƽ����

    call vdr_thdr(field_real,field_image,m3,n3,deriv_operator_x,deriv_operator_y,deriv_operator_z)		 

    end if
    end subroutine field_deriv
    !    ************�����ӳ�����ģ�����**********

    !***************vdr*******************
    subroutine vdr(field_real,field_image,m3,n3,deriv_operator_z)
    integer m3,n3
    real field_real(1:m3,1:n3),field_image(1:m3,1:n3)
    real deriv_operator_z(1:m3,1:n3)

    call fft2(field_real,field_image,m3,n3,2)  
    call multiply_sub(field_real,field_image,m3,n3,deriv_operator_z)
    call fft2(field_real,field_image,m3,n3,1)
    end subroutine vdr
    !*************vdr******************



    !************ ������㿪ʼ**********
    subroutine multiply_sub(field_real,field_image,m3,n3,deriv_operator)
    implicit none
    integer m3,n3,i,j
    real field_real(1:m3,1:n3),field_image(1:m3,1:n3)
    real deriv_operator(1:m3,1:n3)

    do i=1,m3
        do j=1,n3
            field_real(i,j) =field_real(i,j) *deriv_operator(i,j)
            field_image(i,j)=field_image(i,j)*deriv_operator(i,j)
        end do
    end do

    end subroutine multiply_sub
    !********* ����������*************

    !***************thdr**********************
    subroutine thdr(field_real,field_image,m3,n3,deriv_operator_x,deriv_operator_y)

    integer m3,n3,i,j
    real deriv_operator_x(1:m3,1:n3),deriv_operator_y(1:m3,1:n3)
    real field_real(1:m3,1:n3)
    real field_image(1:m3,1:n3)
    real field_real_x(1:m3,1:n3),field_image_x(1:m3,1:n3)
    real field_real_y(1:m3,1:n3),field_image_y(1:m3,1:n3)

    call fft2(field_real,field_image,m3,n3,2)
    do i=1,m3
        do j=1,n3
            field_real_x(i,j)=-deriv_operator_x(i,j)*field_image(i,j)
            field_image_x(i,j)=deriv_operator_x(i,j)*field_real(i,j)
            field_real_y(i,j)=-deriv_operator_y(i,j)*field_image(i,j)
            field_image_y(i,j)=deriv_operator_y(i,j)*field_real(i,j)		
        end do
    end do  
    call fft2(field_real_x,field_image_x,m3,n3,1)
    call fft2(field_real_y,field_image_y,m3,n3,1)

    do i=1,m3
        do j=1,n3
            field_real(i,j)=sqrt(field_real_x(i,j)**2+field_real_y(i,j)**2)
        end do
    end do
    end subroutine thdr
    !*****************thdr*********************

    !************************asm_meth********************************
    subroutine asm_meth(field_real,field_image,m3,n3,deriv_operator_x,deriv_operator_y,deriv_operator_z)
    integer m3,n3
    real field_real(1:m3,1:n3),field_image(1:m3,1:n3)
    real field_real_thdr(1:m3,1:n3),field_image_thdr(1:m3,1:n3)
    real field_real_vdr(1:m3,1:n3),field_image_vdr(1:m3,1:n3)
    real deriv_operator_z(1:m3,1:n3)
    real deriv_operator_x(1:m3,1:n3),deriv_operator_y(1:m3,1:n3)

    field_real_thdr=field_real
    field_image_thdr=field_image
    call thdr(field_real_thdr,field_image_thdr,m3,n3,deriv_operator_x,deriv_operator_y)

    field_real_vdr=field_real
    field_image_vdr=field_image 
    call vdr(field_real_vdr,field_image_vdr,m3,n3,deriv_operator_z)

    do i=1,m3
        do j=1,n3
            field_real(i,j)=sqrt(field_real_thdr(i,j)**2+field_real_vdr(i,j)**2)
        end do
    end do

    end subroutine asm_meth
    !**************************asm_meth**********************************

    !************************ta******************************************
    subroutine ta(field_real,field_image,m3,n3,deriv_operator_x,deriv_operator_y,deriv_operator_z)
    integer m3,n3
    real field_real(1:m3,1:n3),field_image(1:m3,1:n3)
    real deriv_operator_z(1:m3,1:n3)
    real deriv_operator_x(1:m3,1:n3),deriv_operator_y(1:m3,1:n3)
    real field_real_thdr(1:m3,1:n3),field_image_thdr(1:m3,1:n3)
    real field_real_vdr(1:m3,1:n3),field_image_vdr(1:m3,1:n3)

    field_real_thdr=field_real
    field_image_thdr=field_image
    call thdr(field_real_thdr,field_image_thdr,m3,n3,deriv_operator_x,deriv_operator_y)

    field_real_vdr=field_real
    field_image_vdr=field_image 
    call vdr(field_real_vdr,field_image_vdr,m3,n3,deriv_operator_z)

    do i=1,m3
        do j=1,n3
            field_real(i,j)=atand(field_real_vdr(i,j)/field_real_thdr(i,j))
        end do
    end do
    end subroutine ta
    !************************ta******************************************

    !**********************vdr_vdr***************************************
    subroutine vdr_vdr(field_real,field_image,m3,n3,deriv_operator_z)
    integer m3,n3
    real field_real(1:m3,1:n3),field_image(1:m3,1:n3)
    real deriv_operator_z(1:m3,1:n3)

    call fft2(field_real,field_image,m3,n3,2)  
    call multiply_sub(field_real,field_image,m3,n3,deriv_operator_z)
    call multiply_sub(field_real,field_image,m3,n3,deriv_operator_z)
    call fft2(field_real,field_image,m3,n3,1)
    end subroutine vdr_vdr
    !*********************vdr_vdr****************************************

    !********************ta_thdr***************************************
    subroutine ta_thdr(field_real,field_image,m3,n3,deriv_operator_x,deriv_operator_y,deriv_operator_z)
    integer m3,n3
    real field_real(1:m3,1:n3),field_image(1:m3,1:n3)
    real deriv_operator_z(1:m3,1:n3)
    real deriv_operator_x(1:m3,1:n3),deriv_operator_y(1:m3,1:n3)
    real field_real_thdr(1:m3,1:n3),field_image_thdr(1:m3,1:n3)
    real field_real_ta(1:m3,1:n3),field_image_ta(1:m3,1:n3)

    field_real_ta=field_real
    field_image_ta=field_image 
    call ta(field_real_ta,field_image_ta,m3,n3,deriv_operator_x,deriv_operator_y,deriv_operator_z)

    field_real_thdr=field_real_ta
    field_image_thdr=field_image
    call thdr(field_real_thdr,field_image_thdr,m3,n3,deriv_operator_x,deriv_operator_y)
    field_real=field_real_thdr

    end subroutine ta_thdr
    !*******************ta_thdr*****************************************

    !********************vdr_thdr***************************************
    subroutine vdr_thdr(field_real,field_image,m3,n3,deriv_operator_x,deriv_operator_y,deriv_operator_z)
    integer m3,n3
    real field_real(1:m3,1:n3),field_image(1:m3,1:n3)
    real deriv_operator_z(1:m3,1:n3)
    real deriv_operator_x(1:m3,1:n3),deriv_operator_y(1:m3,1:n3)
    real field_real_thdr(1:m3,1:n3),field_image_thdr(1:m3,1:n3)
    real field_real_vdr(1:m3,1:n3),field_image_vdr(1:m3,1:n3)

    field_real_vdr=field_real
    field_image_vdr=field_image 
    call vdr(field_real_vdr,field_image_vdr,m3,n3,deriv_operator_z)

    field_real_thdr=field_real_vdr
    field_image_thdr=field_image
    call thdr(field_real_thdr,field_image_thdr,m3,n3,deriv_operator_x,deriv_operator_y)
    field_real=field_real_thdr

    end subroutine vdr_thdr
    !*******************vdr_thdr*****************************************

    subroutine deriv_operator_sub(dx,dy,m,n,deriv_operator_x,deriv_operator_y,deriv_operator_z) 
    implicit none
    real dx,dy
    real dz
    integer m,n,i,j
    real w(1:m,1:n),u(1:m),v(1:n)
    real deriv_operator_z(1:m,1:n)
    real deriv_operator_x(1:m,1:n)
    real deriv_operator_y(1:m,1:n)

    call wave2(m,n,dx,dy,u,v,w)
    !���㴹��������,ʵ��
    deriv_operator_z=w
    !����x��y�������ӣ�����
    do j=1,n
        do i=1,m
            deriv_operator_x(i,j)=u(i)
            deriv_operator_y(i,j)=v(j)
        end do 
    end do

    end subroutine deriv_operator_sub
    !************���㵼�������ӳ������*****************


