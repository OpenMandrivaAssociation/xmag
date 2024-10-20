Name: xmag
Version: 1.0.8
Release: 1
Summary: Magnify parts of the screen
Group: Development/X11
Source0: https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1: xmag.xpm
Source2: xmag.xpm.large
Source3: xmag.xpm.mini
License: MIT

BuildRequires: pkgconfig(xt) >= 1.0.0
BuildRequires: xaw-devel >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.0.1

%description
The xmag program allows you to magnify portions of an X screen.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

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
