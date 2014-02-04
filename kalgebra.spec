%ifarch %{arm}
%bcond_with opengl
%else
%bcond_without opengl
%endif

Summary:	MathML-based graph calculator
Name:		kalgebra
Version:	4.12.2
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
Url:		http://userbase.kde.org/KAlgebra
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	libkdeedu-devel >= %{version}
BuildRequires:	readline-devel
BuildRequires:	analitza-devel
%if %{with opengl}
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
%endif
# add SHOULD_BUILD_OPENGL option, to be able to disable support
# on arm because plotter3d assumes qreal=double all over the place
Patch1:		kalgebra-4.10.1-opengl_optional.patch

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
%{_kde_libdir}/kde4/imports/org/kde/analitza/
%{_kde_appsdir}/katepart/syntax/kalgebra.xml
%{_kde_appsdir}/kalgebramobile
%{_kde_appsdir}/plasma/plasmoids/org.kde.graphsplasmoid
%{_kde_services}/kalgebra*.desktop
%{_kde_services}/graphsplasmoid.desktop

#----------------------------------------------------------------------

%prep
%setup -q
%patch1 -p1 -b .opengl_optional

%build
%cmake_kde4 \
%if %{with opengl}
	-DSHOULD_BUILD_OPENGL:BOOL=ON
%else
	-DSHOULD_BUILD_OPENGL:BOOL=OFF
%endif

%make

%install
%makeinstall_std -C build

%changelog
* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.4-1
- New version 4.10.4
- Fix conditions for OpenGL support
- Update BuildRequires

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.3-1
- New version 4.10.3

* Fri Apr 26 2013 Alexander Khryukin <alexander@mezon.ru> 4.10.2-2
- Make OpenGL support optional and disable it for arm by default

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0
- Update files

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0

* Thu Jul 19 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.97-1
- New version 4.8.97

* Tue Jul 03 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95
- Update file list

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.0-69.1mib2010.2
+ Revision: 762447
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.8.0-1
+ Revision: 762447
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758038
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744522
- New upstream tarball

* Wed Dec 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.90-1
+ Revision: 741350
- Fix filelist
- Fix filelist
- Fix BR
- New upstream tarball
- New upstream tarball 4.7.80

* Mon Nov 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.41-1
+ Revision: 730547
- Fix typo in URL
- Import package

