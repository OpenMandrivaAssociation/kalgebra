#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%bcond_without opengl

Summary:	MathML-based graph calculator
Name:		kalgebra
Version:	25.08.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+ and LGPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		https://userbase.kde.org/KAlgebra
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/kalgebra/-/archive/%{gitbranch}/kalgebra-%{gitbranchd}.tar.bz2#/kalgebra-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kalgebra-%{version}.tar.xz
%endif
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(Plasma) >= 5.27.90
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	cmake(Qt6)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Analitza6)
BuildRequires:	cmake(ECM)
BuildRequires:	readline-devel
BuildRequires:	qt6-qtimageformats-devel
%if %{with opengl}
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
%endif
# add SHOULD_BUILD_OPENGL option, to be able to disable support
# on arm because plotter3d assumes qreal=double all over the place
#Patch0:		kalgebra-4.13.2-opengl_optional.patch

%rename plasma6-kalgebra

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
%if %{with opengl}
BuildOption:	-DHAVE_OPENGL=1
%else
BuildOption:	-DHAVE_OPENGL=0
%endif

%description
KAlgebra is a mathematical calculator based content markup MathML
language. Nowadays it is capable to make simple MathML operations
(arithmetic and logical) and representate 2D and 3D graphs. It is
actually not necessary to know MathML to use KAlgebra.

%files -f %{name}.lang
%doc COPYING COPYING.LIB COPYING.DOC
%{_bindir}/calgebra
%{_bindir}/kalgebra
%{_bindir}/kalgebramobile
%{_datadir}/applications/*.desktop
%{_datadir}/plasma/plasmoids/org.kde.graphsplasmoid
%{_datadir}/metainfo/org.kde.kalgebra.appdata.xml
%{_datadir}/metainfo/org.kde.kalgebramobile.appdata.xml
%{_datadir}/metainfo/org.kde.graphsplasmoid.appdata.xml
%{_iconsdir}/*/*/apps/kalgebra.*
%{_datadir}/katepart5/syntax/kalgebra.xml
