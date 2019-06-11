
Name:       sunxi-mali-r6p2-drm

Summary:    Mali OpenGL ES userspace libraries for Allwinner SoCs
Version:    0.0.1
Release:    0
Group:      System/Libraries
License:    MIT
URL:        https://github.com/bootlin/mali-blobs
Source0:    %{name}-%{version}.tar.bz2
Patch1:     egl-no-x11-headers.patch
Provides:   libgbm
Provides:   libEGL
Provides:   libGLESv1
Provides:   libGLESv2
Provides:   libwayland-egl

Provides:   libEGL.so.1
Provides:   libEGL.so.1.4
Provides:   libgbm.so.1
Provides:   libGLESv1_CM.so.1
Provides:   libGLESv1_CM.so.1.1
Provides:   libGLESv2.so.2
Provides:   libGLESv2.so.2.0

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
Mali OpenGL ES userspace libraries for Allwinner SoCs


%package devel
Summary:    Mali OpenGL ES userspace development package
Group:      System/Libraries
Requires:   %{name}
Provides:   libgbm-devel
Provides:   libEGL-devel
Provides:   libGLESv1-devel
Provides:   libGLESv2-devel

%description devel
Mali libgbm development package.



%prep
%setup -q -n %{name}-%{version}/mali-blobs

%patch1 -p1

%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_includedir}
cp -af r6p2/arm/wayland/lib* %{buildroot}%{_libdir}
cp -rf include/wayland/* %{buildroot}%{_includedir}
cp ../pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libEGL.so.*
%{_libdir}/libgbm.so.*
%{_libdir}/libGLESv1_CM.so.*
%{_libdir}/libGLESv2.so.*
%{_libdir}/libwayland-egl.so
%{_libdir}/libMali.so


%files devel
%defattr(-,root,root,-)
%{_libdir}/libEGL.so
%{_libdir}/libgbm.so
%{_libdir}/libGLESv1_CM.so
%{_libdir}/libGLESv2.so
%{_libdir}/pkgconfig
%{_includedir}


