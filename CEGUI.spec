%define libname %mklibname %{name} %{version}
%define develname %mklibname %{name} -d

Summary:	A free library providing windowing and widgets for graphics APIs / engines 
Name:		CEGUI
Version:	0.7.5
Release:	%mkrel 2
License:	MIT
Group:		Development/C++
URL:		http://www.cegui.org.uk
Source0:	http://prdownloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.gz
Patch1:		cegui-0.7.5-fedora-cstddef.patch
Patch2:		cegui-0.6.2-fedora-new-tinyxml.patch
BuildRequires:	libxml2-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	mesaglut-devel
BuildRequires:	freetype2-devel
BuildRequires:	pcre-devel
BuildRequires:	freeimage-devel
BuildRequires:	libexpat-devel
BuildRequires:	libxerces-c-devel
BuildRequires:	gtk2-devel
BuildRequires:	devil-devel
BuildRequires:	glew-devel
BuildRequires:	tinyxml-devel
BuildRequires:	fribidi-devel
BuildRequires:	irrlicht-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Crazy Eddie's GUI System is a free library providing windowing and widgets for 
graphics APIs / engines where such functionality is not natively available,
or severely lacking. The library is object orientated, written in C++, 
and targeted at games developers who should be spending their time creating 
great games, not building GUI sub-systems!

%package -n %{libname}
Summary:	CEGUI library
Group:		Games/Other
Obsoletes:	%mklibname %{name} 0
Obsoletes:	%mklibname %{name} 1

%description -n %{libname}
This is a library used by CEGUI.

%package -n %{develname}
Summary:	Development files for CEGUI
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname %{name} 0 -d
Conflicts:	%{_lib}CEUI0.6-devel

%description -n  %{develname}
Development file for CEGUI.

%prep
%setup -q
%patch1 -p0
%patch2 -p1

touch NEWS COPYING README AUTHORS ChangeLog

%build
autoreconf -ifv
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
export CPPFLAGS="%{optflags} -fPIC"

%configure2_5x \
	--with-gtk2 \
	--disable-samples \
	--disable-irrlicht-renderer \
	--enable-freeimage \
	--disable-directfb-renderer \
	--enable-bidirectional-text


# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libCEGUI*-%{version}.so

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*la
%{_libdir}/*.so
%exclude %{_libdir}/libCEGUI*-%{version}.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*
%{_datadir}/%{name}
