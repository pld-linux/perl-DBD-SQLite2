#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	DBD
%define		pnam	SQLite2
Summary:	DBD::SQLite2 - Self Contained RDBMS in a DBI Driver (sqlite 2.x)
Summary(pl.UTF-8):	DBD::SQlite2 - Kompletny RDBMS zawarty w sterowniku DBI (sqlite 2.x)
Name:		perl-DBD-SQLite2
Version:	0.37
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f05f60d8a54f0024abb3b3e39861ee3d
URL:		http://search.cpan.org/dist/DBD-SQLite2/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBI
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::SQLite2 is a DBI driver for SQLite database. SQLite is a public
domain RDBMS database engine that you can find at
<http://www.sqlite.org/>.

Rather than ask you to install SQLite first, DBD::SQLite2 includes the
entire thing in the distribution. So in order to get a fast
transaction capable RDBMS working for your perl project you simply
have to install this module, and nothing else.

This version uses older version of SQLite engine (2.x). To get a
newest one please use perl-DBD-SQLite.

%description -l pl.UTF-8
DBD::SQLite2 to sterownik DBI do baz danych SQLite. SQLite to silnik
relacyjnych baz danych na licencji public domain. Można go znaleźć pod
adresem <http://www.sqlite.org/>.

DBD::SQLite2 zawiera w sobie cały silnik bazy danych. Dzięki temu aby
otrzymać działający RDBMS dostępny z poziomu Perla nie trzeba
instalować żadnych innych pakietów.

Ta wersja korzysta ze starszej wersji silnika SQLite (2.x). Aby użyć
nowszej wersji należy zainstalować pakiet perl-DBD-SQLite.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# not real test
mv t/ak-dbd.t{,est}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/DBD/getsqlite.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/DBD/SQLite2.pm
%dir %{perl_vendorarch}/auto/DBD/SQLite2
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/SQLite2/SQLite2.so
%{_mandir}/man3/DBD*
