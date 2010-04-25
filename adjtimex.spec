Summary:	A utility for adjusting kernel time variables
Name:		adjtimex
Version:	1.29
Release:	%mkrel 1
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
