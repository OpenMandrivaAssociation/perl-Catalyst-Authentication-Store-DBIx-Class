%define upstream_name    Catalyst-Authentication-Store-DBIx-Class
%define upstream_version 0.1506

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Catalyst Auth storage using DBIx::Class


License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(strictures)
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

# %check
# %make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*





