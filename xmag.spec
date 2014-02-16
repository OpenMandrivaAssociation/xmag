Name: xmag
Version: 1.0.5
Release: 2
Summary: Magnify parts of the screen
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1: xmag.xpm
Source2: xmag.xpm.large
Source3: xmag.xpm.mini
License: MIT

BuildRequires: libxt-devel >= 1.0.0
BuildRequires: pkgconfig(xaw7)
BuildRequires: x11-util-macros >= 1.0.1

%description
The xmag program allows you to magnify portions of an X screen.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

# install icons
mkdir -p %{buildroot}%{_datadir}/icons/large
mkdir -p %{buildroot}%{_datadir}/icons/mini

install -m0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/xmag.xpm
install -m0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/large/xmag.xpm
install -m0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/mini/xmag.xpm

%files
%{_bindir}/xmag
%{_datadir}/X11/app-defaults/Xmag
%{_mandir}/man1/xmag.1*
%{_datadir}/icons/xmag.xpm
%{_datadir}/icons/*/xmag.xpm


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2011.0
+ Revision: 671340
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 592499
- new release

* Thu Nov 12 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.3-1mdv2010.1
+ Revision: 465414
- Remove patch1 (already integrated)

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.2-5mdv2009.1
+ Revision: 366702
- no more autoconf needed

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2009.0
+ Revision: 266117
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-3mdv2009.0
+ Revision: 194811
- Properly handle multiple depth windows.
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-2mdv2008.1
+ Revision: 154426
- Updated BuildRequires and resubmit package.
- Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.2-1mdv2008.0
+ Revision: 64267
- new upstream release: 1.0.4


* Fri Nov 17 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.1-6mdv2007.0
+ Revision: 85372
- added missing icons

* Sat Sep 02 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.1-5mdv2007.0
+ Revision: 59482
- rebuild to fix libXaw.so.8 dependency
- rebuild to fix cooker uploading
- Rebuild against new libXaw packages
- increment release
- Adding X.org 7.0 to the repository

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fill in missing description & summaries

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

