%define libname %mklibname %{name} %{version}
%define develname %mklibname %{name} -d

Summary:	A free library providing windowing and widgets for graphics APIs / engines 
Name:		CEGUI
Version:	0.7.7
Release:	2
License:	MIT
Group:		Development/C++
URL:		http://www.cegui.org.uk
Source0:	http://prdownloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	freeimage-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(xerces-c)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	devil-devel
BuildRequires:	tinyxml-devel
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	irrlicht-devel

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
Conflicts:	%{_lib}CEUI0.6-devel

%description -n  %{develname}
Development file for CEGUI.

%prep
%setup -q

touch NEWS COPYING README AUTHORS ChangeLog

%build
%configure2_5x \
	--with-gtk2 \
	--disable-samples \
	--disable-static \
	--disable-corona \
	--disable-directfb-renderer \
	--disable-irrlicht-renderer \
	--enable-freeimage \
	--enable-bidirectional-text \
	--with-default-xml-parser=ExpatParser \
	--with-pic

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libCEGUI*-%{version}.so

%files -n %{develname}
%{_libdir}/*.so
%exclude %{_libdir}/libCEGUI*-%{version}.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*
%{_datadir}/%{name}

%changelog
* Mon Oct 03 2011 Andrey Bondrov <abondrov@mandriva.org> 0.7.5-2mdv2012.0
+ Revision: 702579
- Add patch to fix build with new TinyXML
- Rebuild
- New version: 0.7.5

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Fri Feb 05 2010 Funda Wang <fwang@mandriva.org> 0.7.1-3mdv2010.1
+ Revision: 501069
- conflicts with CEGUI 0.6

* Tue Feb 02 2010 Funda Wang <fwang@mandriva.org> 0.7.1-2mdv2010.1
+ Revision: 499666
- rebuild

* Sat Jan 30 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.1-1mdv2010.1
+ Revision: 498492
- update to new version 0.7.1
- drop patches 1 and 3, fixed upstream
- rediff patch2
- enable support for devil and fribidi

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Dec 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.2-3mdv2009.1
+ Revision: 321148
- Patch3: reintroduce this patch, changes library naming to %%{libname}-%%{version}.so
- Patch1: reintroduce this too
- use %%define _default_patch_fuzz 3 because patch 3 fails in one line in src/Makefile.am

* Wed Dec 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.2-2mdv2009.1
+ Revision: 318212
- drop patch1, since upstream has switched to use major number in libraries name (smc works again#44445)

* Wed Dec 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.2-1mdv2009.1
+ Revision: 309824
- drop patch 0, as it was merged by upstream
- Patch2: rediff
- obsolete old library
- fix file list
- update to new version 0.6.2

* Sat Oct 11 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.1-5mdv2009.1
+ Revision: 291763
- missed one use of the old %%realver
- adjust file list
- just use %%version for the library versioning
- adjust file list
- use autoreconf not bootstrap
- drop Makefile.in mods from fix-underlinking.patch (not needed)
- rediff fix-underlinking.patch
- add release-as-so-ver.patch: bases lib version on CEGUI version not spurious
  major, which was not respected in code (upstream has this in current CVS)

* Tue Sep 02 2008 Emmanuel Andry <eandry@mandriva.org> 0.6.1-4mdv2009.0
+ Revision: 279319
- rebuild for fixed freeimage

* Tue Sep 02 2008 Emmanuel Andry <eandry@mandriva.org> 0.6.1-3mdv2009.0
+ Revision: 279202
- disable devil, latest devil version doesn't build

* Mon Aug 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.1-2mdv2009.0
+ Revision: 275925
- Patch1: fix underlinking
- add buildrequires on glew-devel and tinyxml-devel
- kill rpath

  + Emmanuel Andry <eandry@mandriva.org>
    - remove the disable underlinking define (without doing anything special, strange)

* Tue Aug 19 2008 Emmanuel Andry <eandry@mandriva.org> 0.6.1-1mdv2009.0
+ Revision: 274077
- set define _disable_ld_no_undefined
- update file list
- add P1950 from fedora

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Apr 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0b-4mdv2009.0
+ Revision: 197222
- obsolete older library

* Thu Apr 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0b-3mdv2009.0
+ Revision: 197194
- fix file list

* Fri Apr 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0b-2mdv2009.0
+ Revision: 195622
- new devel library policy
- add missing buildrequires

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Apr 25 2007 Erwan Velu <erwan@mandriva.org> 0.5.0-2mdv2008.0
+ Revision: 18233
- Fixing buildrequires
  Fixing .so includes

* Wed Apr 25 2007 Erwan Velu <erwan@mandriva.org> 0.5.0-1mdv2008.0
+ Revision: 18217
- New buildrequires
- freetype2 was missing
- Import CEGUI

