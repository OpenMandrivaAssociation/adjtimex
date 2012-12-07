Summary:	A utility for adjusting kernel time variables
Name:		adjtimex
Version:	1.29
Release:	%mkrel 4
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		ftp://ftp.debian.org/debian/pool/main/a/adjtimex/
Source0:	ftp://ftp.debian.org/debian/pool/main/a/adjtimex/adjtimex_%{version}.orig.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
Adjtimex is a kernel clock management program, which the
superuser may use to correct any drift in the system's clock.  Users can
use adjtimex to view the time variables.

%description -l fr
Adjtimex est un programme de gestion de l'horloge du kernel, que le
superutilisateur peut utiliser pour corriger l'horloge système. Les
utilisateurs peuvent utiliser adjtimex pour afficher les variables
temporelles.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

install -m755 adjtimex -D %{buildroot}/%{_sbindir}/adjtimex
install -m644 adjtimex.8 -D %{buildroot}/%{_mandir}/man8/adjtimex.8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYRIGHT COPYING README.ru ChangeLog
%{_sbindir}/adjtimex
%{_mandir}/man8/adjtimex.8*


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.29-3mdv2011.0
+ Revision: 662755
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1.29-2mdv2011.0
+ Revision: 603172
- rebuild

* Sun Apr 25 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.29-1mdv2010.1
+ Revision: 538721
- update to 1.29
- use configure2_5x

* Fri Feb 12 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.28-1mdv2010.1
+ Revision: 505118
- update to 1.28

* Wed May 27 2009 Frederik Himpe <fhimpe@mandriva.org> 1.27.1-1mdv2010.0
+ Revision: 380253
- update to new version 1.27.1

* Sat Mar 21 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.26-1mdv2009.1
+ Revision: 359676
- Updated to version 1.26
- Dropped following obsolete/merged patches:
  adjtimex-1.13-glibc.patch
  adjtimex-1.21-optstring.patch

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.21-6mdv2009.1
+ Revision: 349988
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.21-5mdv2009.0
+ Revision: 220345
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.21-4mdv2008.1
+ Revision: 179988
- added two patches from fc9 that madde it compile
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 09:06:12 (55876)
- rebuild

* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 09:05:09 (55875)
Import adjtimex

* Thu Jul 20 2006 Jerome Soyer <saispo@mandriva.org> 1.21-1mdv2007.0
- New version 1.21

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.20-2mdk
- Rebuild

* Wed Aug 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.20-1mdk
- New release 1.20

* Fri Jul 09 2004 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 1.16-1mdk
- New release 1.16

