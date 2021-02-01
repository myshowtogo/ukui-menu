%define debug_package %{nil}

Name:           ukui-menu
Version:        3.0.2
Release:        3
Summary:        Advanced ukui menu
License:        GPL-3.0
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires: qt5-qtbase-devel
BuildRequires: libqtxdg-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: glib2-devel >= 2.36
BuildRequires: gsettings-qt-devel
BuildRequires: bamf-devel
BuildRequires: libXrandr-devel
BuildRequires: libXtst-devel
BuildRequires: libX11-devel
BuildRequires: qt5-qttools-devel
BuildRequires: kf5-kwindowsystem-devel

Requires: gsettings-qt
Requires: qt5-qtx11extras
Requires: bamf-daemon
Requires: libXrandr
Requires: libXtst
Requires: libX11
Requires: accountsservice

%description
 UKUI menu provides start menu development library and advanced
 graphical user interface.
 .
 The package contains executable file.

%prep
%setup -q

%build
mkdir build && cd build
qmake-qt5 ..
make

%install
rm -rf $RPM_BUILD_ROOT 
cd %{_builddir}/%{name}-%{version}/build
make INSTALL_ROOT=%{buildroot} install

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_bindir}/ukui-menu
%{_sysconfdir}/xdg/autostart/ukui-menu.desktop
%{_datadir}/ukui-menu/translations/

%changelog
* Mon Feb 1 2021 lvhan <lvhan@kylinos.cn> - 3.0.2-3
- update to upstream version 3.0.1-1

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.2-2
- fix uninstalled failed issue

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.2-1
- update to upstream version 3.0.1-1+1026

* Wed Sep 23 2020 douyan <douyan@kylinos.cn> - 2.0.6-2
- fix uninstall issue

* Mon Jul 20 2020 douyan <douyan@kylinos.cn> - 2.0.6-1
- Init package for openEuler
