%define upstream_name    Class-C3-Adopt-NEXT
%define upstream_version 0.13

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Make NEXT suck less
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(NEXT)
BuildRequires: perl(Test::Exception)
BuildRequires: perl-devel
BuildArch: noarch

%description
the NEXT manpage was a good solution a few years ago, but isn't any more.
It's slow, and the order in which it re-dispatches methods appears random
at times. It also encourages bad programming practices, as you end up with
code to re-dispatch methods when all you really wanted to do was run some
code before or after a method fired.

However, if you have a large application, then weaning yourself off 'NEXT'
isn't easy.

This module is intended as a drop-in replacement for NEXT, supporting the
same interface, but using the Class::C3 manpage to do the hard work. You
can then write new code without 'NEXT', and migrate individual source files
to use 'Class::C3' or method modifiers as appropriate, at whatever pace
you're comfortable with.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.130.0-2mdv2011.0
+ Revision: 658740
- rebuild for updated spec-helper

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 554166
- update to 0.13

* Fri Jun 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 385442
- import perl-Class-C3-Adopt-NEXT


* Fri Jun 12 2009 cpan2dist 0.12-1mdv
- initial mdv release, generated with cpan2dist

