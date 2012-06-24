#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	SQLite2
Summary:	DBD::SQLite2 - Self Contained RDBMS in a DBI Driver (sqlite 2.x) 
Summary(pl):	DBD::SQlite2 - Kompletny RDBMS zawarty w sterowniku DBI (sqlite 2.x)
Name:		perl-DBD-SQLite2
Version:	0.33
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	babd83fd5eb9ba7560ad4bab4c76c0eb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBI
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::SQLite2 is a DBI driver for SQLite database. SQLite is a public
domain RDBMS database engine that you can find at
http://www.sqlite.org/ .

Rather than ask you to install SQLite first, DBD::SQLite2 includes the
entire thing in the distribution. So in order to get a fast
transaction capable RDBMS working for your perl project you simply
have to install this module, and nothing else.

This version uses older version of SQLite engine (2.x). To get
a newest one please use perl-DBD-SQLite.

%description -l pl
DBD::SQLite2 to sterownik DBI do baz danych SQLite. SQLite to silnik
relacyjnych baz danych na licencji public domain. Mo�na go znale�� pod
adresem http://www.sqlite.org/ .

DBD::SQLite2 zawiera w sobie ca�y silnik bazy danych. Dzi�ki temu aby
otrzyma� dzia�aj�cy RDBMS dost�pny z poziomu Perla nie trzeba
instalowa� �adnych innych pakiet�w.

Ta wersja korzysta ze starszej wersji silnika SQLite (2.x). Aby u�y�
nowszej wersji nale�y zainstalowa� pakiet perl-DBD-SQLite.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo y | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
# If SQLITE_PTR_SZ is not set in OPTIMIZE SQLite assumes 64-bit
# architecture and fails. 
%{__make} \
	OPTIMIZE="%{rpmcflags} -DSQLITE_PTR_SZ=`%{__perl} -MConfig -e 'print \"$Config{ptrsize}\";'`"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/DBD/SQLite2.pm
%dir %{perl_vendorarch}/auto/DBD/SQLite2
%{perl_vendorarch}/auto/DBD/SQLite2/SQLite2.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/SQLite2/SQLite2.so
%{_mandir}/man3/DBD*
