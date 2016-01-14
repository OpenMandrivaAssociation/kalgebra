%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%bcond_without opengl

Summary:	MathML-based graph calculator
Name:		kalgebra
Version:	15.12.1
Release:	1
License:	GPLv2+ and LGPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KAlgebra
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)

BuildRequires:  cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5OpenGL)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5WebKitWidgets)

BuildRequires:	cmake(ECM)

BuildRequires:	libkdeedu-devel >= %{version}
BuildRequires:	readline-devel
BuildRequires:	analitza-devel
BuildRequires:	qt5-qtimageformats-devel
%if %{with opengl}
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
%endif
# add SHOULD_BUILD_OPENGL option, to be able to disable support
# on arm because plotter3d assumes qreal=double all over the place
Patch0:		kalgebra-4.13.2-opengl_optional.patch

%description
KAlgebra is a mathematical calculator based content markup MathML
language. Nowadays it is capable to make simple MathML operations
(arithmetic and logical) and representate 2D and 3D graphs. It is
actually not necessary to know MathML to use KAlgebra.

%files
%doc COPYING COPYING.LIB COPYING.DOC
%doc %{_kde_docdir}/HTML/en/kalgebra
%{_kde_bindir}/calgebra
%{_kde_bindir}/kalgebra
%{_kde_bindir}/kalgebramobile
%{_datadir}/applications/*.desktop
%{_datadir}/katepart5/syntax/kalgebra.xml
%{_datadir}/kalgebramobile
%{_datadir}/kservices5/graphsplasmoid.desktop
%{_datadir}/plasma/plasmoids/org.kde.graphsplasmoid
%{_kde_datadir}/appdata/org.kde.kalgebra.appdata.xml
%{_kde_iconsdir}/*/*/apps/kalgebra.*

#----------------------------------------------------------------------

%prep
%setup -q

%cmake_kde5 \
%if %{with opengl}
	-DHAVE_OPENGL=1
%else
	-DHAVE_OPENGL=0
%endif

%build
%ninja -C build

%install
%ninja_install -C build

