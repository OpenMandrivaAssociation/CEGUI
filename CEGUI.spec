%define realver 0.5.0
%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	A free library providing windowing and widgets for graphics APIs / engines 
Name:		CEGUI
Version:	%{realver}b
Release:	%mkrel 2
License:	MIT 
Group:		Development/C++
Url:		http://www.cegui.org.uk
Source0:	http://prdownloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.bz2
BuildRequires:	libxml2-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	mesaglut-devel
BuildRequires:	freetype2-devel
BuildRequires:	pcre-devel
BuildRequires:	FreeImage-devel
BuildRequires:	libexpat-devel
BuildRequires:	libxerces-c0-devel
BuildRequires:	gtk2-devel
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

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*la
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*
