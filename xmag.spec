Name: xmag
Version: 1.0.2
Release: %mkrel 1
Summary: Magnify parts of the screen
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1: xmag.xpm
Source2: xmag.xpm.large
Source3: xmag.xpm.mini
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
The xmag program allows you to magnify portions of an X screen.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# install icons
mkdir -p %{buildroot}%{_datadir}/icons/large
mkdir -p %{buildroot}%{_datadir}/icons/mini

install -m0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/xmag.xpm
install -m0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/large/xmag.xpm
install -m0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/mini/xmag.xpm
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xmag
%{_datadir}/X11/app-defaults/Xmag
%{_mandir}/man1/xmag.1*
%{_datadir}/icons/xmag.xpm
%{_datadir}/icons/*/xmag.xpm


