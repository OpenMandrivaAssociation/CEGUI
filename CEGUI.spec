%define libname %mklibname %{name} %{version}
%define develname %mklibname %{name} -d

Summary:	A free library providing windowing and widgets for graphics APIs / engines 
Name:		CEGUI
Version:	0.6.1
Release:	%mkrel 5
License:	MIT 
Group:		Development/C++
URL:		http://www.cegui.org.uk
Source0:	http://prdownloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.gz
# From Fedora, slightly modified, now adopted upstream: version
# libraries based on cegui version - AdamW 2008/10
Patch0:		cegui-0.6.1-release-as-so-ver.patch
# From Fedora, now adopted upstream: adjust dlopen logic to match
# release-as-so-ver.patch - AdamW 2008/10
Patch1:		cegui-0.6.0-userverso.patch
Patch2:		CEGUI-0.6.1-fix-underlinking.patch
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
#BuildRequires:	devil-devel
BuildRequires:	glew-devel
BuildRequires:	tinyxml-devel
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
%patch1 -p1
%patch2 -p1

touch NEWS

%build
autoreconf -i
%configure2_5x \
	--with-gtk2 \
	--disable-samples \
	--disable-irrlicht-renderer \
	--enable-freeimage
	

# We do not want to get linked against a system copy of ourselves!
sed -i 's|-L%{_libdir}||g' RendererModules/OpenGLGUIRenderer/Makefile
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
