%define upstream_name    Class-C3-Adopt-NEXT
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

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
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


