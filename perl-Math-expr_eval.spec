#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	expr_eval
Summary:	Math::expr_eval - an expression evaluator
Summary(pl):	Math::expr_eval - obliczanie wyra�e�
Name:		perl-Math-expr_eval
Version:	1.0
%define	_ver	%(echo %{version} | tr . _)
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}_%{_ver}.zip
# Source0-md5:	f4962039a99c1dddf460291b1cf5feff
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is an expression evaluator. It has three main objectives:
efficiency, extensibility, user-friendly error messages. It's features
include: standard data types, arithmetic and boolean operators,
conditionals, pattern matching, user-defined data types, user-defined
binary operators and prefix unary operators, over-loaded binary
operators and prefix unary operators, calls to user-provided perl
functions, a mode for syntax checking only, optimized re-evaluation of
expressions, multiple symbol tables.

%description -l pl
Ten modu� s�u�y do obliczania wyra�e�. Ma trzy g��wne cele: wydajno��,
rozszerzalno�� i przyjazne dla u�ytkownika komunikaty b��d�w. Jego
mo�liwo�ci obejmuj�: standardowe typy danych, operatory arytmetyczne i
logiczne, warunki, dopasowywanie wzorc�w, definiowalne typy danych,
definiowalne operatory dwuargumentowe i prefiksowe jednoargumentowe,
przeci��one operatory dwuargumentowe i prefiksowe jednoargumentowe,
wywo�ania dostarczonych funkcji Perla, tryb do sprawdzania sk�adni,
zoptymalizowane ponowne obliczanie wyra�e�, wiele tablic symboli.

%prep
%setup -q -c

mv -f Makefile.pl Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

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
%{perl_vendorlib}/Math/expr_eval.pm
