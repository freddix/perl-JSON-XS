%include	/usr/lib/rpm/macros.perl

%define		pdir	JSON
%define		pnam	XS

Summary:	JSON serialising/deserialising, done correctly and fast
Name:		perl-JSON-XS
Version:	3.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b7be65295baf6dd9233c6494782c1153
URL:		http://search.cpan.org/dist/JSON-XS/
BuildRequires:	perl-common-sense
BuildRequires:	perl-devel
BuildRequires:	perl-types-serialiser
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be correct and its secondary goal is to be fast. To
reach the latter goal it was written in C.

%prep
%setup -qn %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/json_xs
%dir %{perl_vendorarch}/auto/JSON
%dir %{perl_vendorarch}/auto/JSON/XS
%attr(755,root,root) %{perl_vendorarch}/auto/JSON/XS/*.so
%{perl_vendorarch}/JSON/XS
%{perl_vendorarch}/JSON/XS.pm
%{perl_vendorarch}/auto/JSON/XS/XS.bs
%{_mandir}/man*/*.*

