%define upstream_name    Catalyst-Authentication-Store-DBIx-Class
%define upstream_version 0.1401

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Catalyst Auth storage using DBIx::Class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Model::DBIC::Schema)
BuildRequires:	perl(Catalyst::Plugin::Authentication)
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
The Catalyst::Authentication::Realm::SimpleDB provides a simple way to
configure Catalyst Authentication when using the most common configuration
of a password protected user retrieved from an SQL database.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*




%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.140.100-2mdv2011.0
+ Revision: 657393
- rebuild for updated spec-helper

* Fri Mar 04 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.140.100-1
+ Revision: 641693
- new version

* Sat Sep 04 2010 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 575733
- update to 0.1400

* Thu Jul 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 553575
- update to 0.1300

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 536129
- update to 0.1200

* Fri Mar 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.108.300-1mdv2010.1
+ Revision: 514400
- update to 0.1083

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.108.200-1mdv2010.1
+ Revision: 471402
- import perl-Catalyst-Authentication-Store-DBIx-Class


* Sun Nov 29 2009 cpan2dist 0.1082-1mdv
- initial mdv release, generated with cpan2dist
