#
# Conditional build:
%bcond_without	doc	# Documentation

%define		orgname		qtgraphicaleffects
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qttools_ver		%{version}
Summary:	The Qt5 Graphical Effects module
Summary(pl.UTF-8):	Moduł Qt5 Graphical Effects
Name:		qt5-%{orgname}
Version:	5.8.0
Release:	1
# pngdumper is LGPL+exception/GPL, all the qml code is BSD
License:	BSD
Group:		X11/Libraries
Source0:	http://download.qt.io/official_releases/qt/5.8/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	0f74145f0fbb3db8d2f9711b83531fcf
URL:		http://www.qt.io/
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 Graphical Effects module.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera moduł Qt5 Graphical Effects.

%package -n Qt5Quick-graphicaleffects
Summary:	Qt5 Graphical Effects module for Qt5Quick library
Summary(pl.UTF-8):	Moduł Qt5 Graphical Effects dla biblioteki Qt5Quick
Group:		X11/Libraries
Requires:	Qt5Quick >= %{qtdeclarative_ver}
Obsoletes:	qt5-qtgraphicaleffects

%description -n Qt5Quick-graphicaleffects
The Qt Graphical Effects module for Qt5Quick provides a set of QML
types for adding visually impressive and configurable effects to user
interfaces. Effects are visual items that can be added to Qt Quick
user interface as UI components.

%description -n Qt5Quick-graphicaleffects -l pl.UTF-8
Moduł Qt Graphical Effects dla biblioteki Qt5Quick udostępnia zbiór
typów QML do dodawania robiących wrażenie, konfigurowalnych efektów
wizualnych do interfejsów użytkownika. Efekty to elementy wizualne,
które można dodać do interfejsu użytkownika jako komponenty UI.

%package doc
Summary:	Qt5 Graphical Effects documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do modułów Qt5 Graphical Effects w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 Graphical Effects documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do modułów Qt5 Graphical Effects w formacie HTML.

%package doc-qch
Summary:	Qt5 Graphical Effects documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do modułów Qt5 Graphical Effects w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-qch
Qt5 Graphical Effects documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do modułów Qt5 Graphical Effects w formacie QCH.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n Qt5Quick-graphicaleffects
%defattr(644,root,root,755)
%doc dist/changes-*
%{qt5dir}/qml/QtGraphicalEffects

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtgraphicaleffects

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtgraphicaleffects.qch
%endif
