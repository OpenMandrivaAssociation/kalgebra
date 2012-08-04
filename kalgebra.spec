Name:		kalgebra
Summary:	MathML-based graph calculator
Version: 4.9.0
Release: 1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
URL:		http://userbase.kde.org/KAlgebra
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	libkdeedu-devel >= %{version}
BuildRequires:	readline-devel
BuildRequires:	analitza-devel

%description
KAlgebra is a mathematical calculator based content markup MathML
language. Nowadays it is capable to make simple MathML operations
(arithmetic and logical) and representate 2D and 3D graphs. It is
actually not necessary to know MathML to use KAlgebra.

%files
%doc COPYING COPYING.LIB COPYING.DOC
%doc %{_kde_docdir}/HTML/en/kalgebra
%{_kde_bindir}/kalgebra
%{_kde_bindir}/kalgebramobile
%{_kde_iconsdir}/*/*/apps/kalgebra.*
%{_kde_applicationsdir}/kalgebra.desktop
%{_kde_applicationsdir}/kalgebramobile.desktop
%{_kde_libdir}/kde4/plasma_applet_kalgebra.so
%{_kde_appsdir}/katepart/syntax/kalgebra.xml
%{_kde_appsdir}/kalgebramobile
%{_kde_services}/kalgebra*.desktop

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

