%define name CEGUI
%define version 0.5.0
%define subversion b
%define release %mkrel 2
%define libname %mklibname %name 0

Summary: A free library providing windowing and widgets for graphics APIs / engines 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}%{subversion}.tar.bz2
License: MIT 
Group: Development/C++
Url: http://www.cegui.org.uk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxml2-devel mesagl-devel mesaglu-devel mesaglut-devel freetype2-devel pcre-devel
BuildRequires: FreeImage-devel

%description
Crazy Eddie's GUI System is a free library providing windowing and widgets for 
graphics APIs / engines where such functionality is not natively available,
or severely lacking. The library is object orientated, written in C++, 
and targeted at games developers who should be spending their time creating 
great games, not building GUI sub-systems!

%package -n %{libname}
Summary:        CEGUI library
Group:          Games/Other
%description -n %{libname}
This is a library used by CEGUI

%package -n %{libname}-devel
Summary:        Development files for CEGUI
Group:          Development/C++
Requires:    %{libname} = %{version}
Provides:    libCEGUI-devel CEGUI-devel
%description -n  %{libname}-devel
Development file for CEGUI

%prep
%setup -q
touch NEWS
aclocal
libtoolize --copy --force --ltdl
autoheader
automake -a -c
autoconf
%configure

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*so*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/*la
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*
