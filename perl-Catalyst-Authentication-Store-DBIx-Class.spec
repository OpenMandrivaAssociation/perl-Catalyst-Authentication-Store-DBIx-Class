%define upstream_name    Catalyst-Authentication-Store-DBIx-Class
Name:		perl-%{upstream_name}
Version:	0.1506
Release:	6

Summary:	Catalyst Auth storage using DBIx::Class


License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://git.shadowcat.co.uk/catagits/Catalyst-Authentication-Store-DBIx-Class
Source0:	https://cpan.metacpan.org/authors/id/I/IL/ILMARI/Catalyst-Authentication-Store-DBIx-Class-%{version}.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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





