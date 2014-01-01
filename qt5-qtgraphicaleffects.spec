# TODO:
# - cleanup

%define		orgname		qtgraphicaleffects
Summary:	The Qt5 Graphical Effects
Name:		qt5-%{orgname}
Version:	5.2.0
Release:	0.1
License:	LGPL v2.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.2/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	85e94989bbc624f676102f0ea343b6dd
URL:		http://qt-project.org/
BuildRequires:	qt5-qtbase-devel = %{version}
BuildRequires:	qt5-qtdeclarative-devel = %{version}
BuildRequires:	qt5-qtscript-devel = %{version}
BuildRequires:	qt5-qttools-devel = %{version}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_noautostrip	'.*_debug\\.so*'

%define		specflags	-fno-strict-aliasing
%define		_qtdir		%{_libdir}/qt5

%description
The Qt5 Graphical Effects libraries.

%package devel
Summary:	The Qt5 Graphical Effects - development files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The Qt5 Graphical Effects - development files.

%package doc
Summary:	The Qt5 Graphical Effects - docs
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
The Qt5 Graphical Effects - documentation.

%package examples
Summary:	The Qt5 Graphical Effects examples
Group:		X11/Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description examples
The Qt5 Graphical Effects - examples.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post		-p /sbin/ldconfig
%postun		-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_qtdir}/qml

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc
