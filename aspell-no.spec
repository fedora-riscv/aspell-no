%define lang nb
%define langrelease 0
Summary: Norwegian dictionaries for Aspell
Name: aspell-no
Epoch: 50
Version: 0.50.1
Release: 12%{?dist}
License: GPLv2
Group: Applications/Text
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell-%{lang}-%{version}-%{langrelease}.tar.bz2
Patch: aspell-nb-0.50.1-0.utf-filename.patch
Buildrequires: aspell >= 12:0.60
Requires: aspell >= 12:0.60
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define debug_package %{nil}

%description
Provides the word list/dictionaries for the following: Norwegian

%prep
%setup -q -n aspell-%{lang}-%{version}-%{langrelease}
%patch -p1 -b .utf-filename
cp bokmal.alias bokmål.alias

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT 
make install  DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING Copyright
%{_libdir}/aspell-0.60/*

%changelog
* Mon Sep 17 2007 Ivana Varekova <varekova@redhat.com> - 50:0.50.1-12
- remove useles souce file

* Thu Mar 29 2007 Ivana Varekova <varekova@redhat.com> - 50:0.50.1-11
- add documentation
- use configure script to create Makefile
- update default buildroot
- some minor spec changes

* Wed Jan 24 2007 Ivana Varekova <varekova@redhat.com> - 50:0.50.1-10
- spec file cleanup
- fix 224147 - rawhide rebuild fails

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 50:0.50.1-9.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 50:0.50.1-9.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 50:0.50.1-9.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Jul 19 2005 Ivana Varekova <varekova@redhat.com> 50:0.50.1-9
- build with aspell-0.60.3

* Mon Apr 11 2005 Ivana Varekova <varekova@redhat.com> 50:0.50.1-8
- rebuilt

* Tue Sep 28 2004 Adrian Havill <havill@redhat.com> 50:0.50.1-7
- bump n-v-r, remove debuginfo, use "nb" lang, utf alias filename,
  add nb locale (Norsk Bokmål) support (#126690; Håvard Wigtil)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun 23 2003 Adrian Havill <havill@redhat.com> 0.50-3
- first build for new aspell (0.50)
