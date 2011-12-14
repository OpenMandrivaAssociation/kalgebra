Name: kalgebra
Summary: MathML-based graph calculator
Version: 4.7.90
Release: 1
Group: Graphical desktop/KDE
License: GPLv2 LGPLv2 GFDL
URL: http://userbase.kde.org/KAlgebra
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%version
BuildRequires: libkdeedu-devel >= %version
BuildRequires: libreadline-devel
BuildRequires: analitza-devel

%description
KAlgebra is a mathematical calculator based content markup MathML
language. Nowadays it is capable to make simple MathML operations
(arithmetic and logical) and representate 2D and 3D graphs. It is
actually not necessary to know MathML to use KAlgebra.

%files
%_kde_bindir/kalgebra
%_kde_bindir/kalgebramobile
%_kde_bindir/calgebra
%_kde_iconsdir/*/*/apps/kalgebra.*
%_kde_datadir/applications/kde4/kalgebra.desktop
%_kde_datadir/applications/kde4/kalgebramobile.desktop
%_kde_libdir/kde4/plasma_applet_kalgebra.so
%_kde_appsdir/katepart/syntax/kalgebra.xml
%_kde_appsdir/kalgebra
%_kde_services/kalgebra*.desktop
%_kde_servicetypes/kalgebra*.desktop
%doc COPYING COPYING.LIB COPYING.DOC
%doc %_kde_docdir/HTML/en/kalgebra

#---------------------------------------------

%define analitza_major 4
%define libanalitza %mklibname analitza %{analitza_major}

%package -n %libanalitza
Summary: Runtime library for kalgebra
Group: System/Libraries

%description -n %libanalitza
Runtime library for kalgebra

%files -n %libanalitza
%_kde_libdir/libanalitza.so.%{analitza_major}*

#---------------------------------------------

%define analitzagui_major 4
%define libanalitzagui %mklibname analitzagui %{analitzagui_major}

%package -n %libanalitzagui
Summary: Runtime library for Kalgebra
Group: System/Libraries

%description -n %libanalitzagui
Runtime library for Kalgebra.

%files -n %libanalitzagui
%_kde_libdir/libanalitzagui.so.%{analitzagui_major}*

#---------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: %libanalitza = %version
Requires: %libanalitzagui = %version
Conflicts: kdeedu4-devel < 4.6.90

%description  devel
Files needed to build applications based on %{name}.

%files devel
%_kde_libdir/libanalitza.so
%_kde_libdir/libanalitzagui.so

#----------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

