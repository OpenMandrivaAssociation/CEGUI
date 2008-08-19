%define _disable_ld_no_undefined 1

%define realver 0.6.1
%define major 1
%define minor 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	A free library providing windowing and widgets for graphics APIs / engines 
Name:		CEGUI
Version:	%{realver}
Release:	%mkrel 1
License:	MIT 
Group:		Development/C++
Url:		http://www.cegui.org.uk
Source0:	http://prdownloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.gz
Patch0:		cegui-0.6.0-userverso.patch
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

%description -n %{libname}
This is a library used by CEGUI.

%package -n %{develname}
Summary:	Development files for CEGUI
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname %{name} 0 -d

%description -n  %{develname}
Development file for CEGUI.

%prep
%setup -q -n %{name}-%{realver}
%patch0 -p1
touch NEWS

%build
%configure2_5x \
	--with-gtk2

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
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.%{minor}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*la
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*
%{_datadir}/%{name}
