Summary:	A utility for adjusting kernel time variables
Name:		adjtimex
Version:	1.21
Release:	%mkrel 2
License:	GPL
Group:		System/Kernel and hardware
URL:		ftp://ftp.debian.org/debian/pool/main/a/adjtimex/
Source:		ftp://ftp.debian.org/debian/pool/main/a/adjtimex/adjtimex_%{version}.orig.tar.bz2

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
%configure 
%make

%install
rm -rf $RPM_BUILD_ROOT
install -s -m755 adjtimex -D $RPM_BUILD_ROOT/%{_sbindir}/adjtimex
install -m644 adjtimex.8 -D $RPM_BUILD_ROOT/%{_mandir}/man8/adjtimex.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYRIGHT COPYING README.ru ChangeLog
%{_sbindir}/adjtimex
%{_mandir}/man8/adjtimex.8*

