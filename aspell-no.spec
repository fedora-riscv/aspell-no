Summary: Norwegian files for aspell
Name: aspell-no
Version: 0.3
Release: 3
Group: Applications/Text
Source: aspell-no-%{version}.tar.bz2
URL: http://www.uio.no/~runekl/dictionary.html
License: GPL
Requires: aspell
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: aspell
Obsoletes: ispell-no, ispell-norwegian

%description
A Norwegian dictionary for use with aspell, a spelling checker.

%prep
%setup -q

%build
cp /usr/share/aspell/iso8859-1.dat .

LC_CTYPE=no_NO aspell --lang=norwegian --data-dir=. \
    create master ./norwegian < words.norsk

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/aspell
mkdir -p $RPM_BUILD_ROOT/usr/share/aspell
mkdir -p $RPM_BUILD_ROOT/usr/share/pspell

install -m 0644 norwegian $RPM_BUILD_ROOT/usr/lib/aspell
ln -s norwegian $RPM_BUILD_ROOT/usr/lib/aspell/norsk
install -m 0644 norwegian.dat $RPM_BUILD_ROOT/usr/share/aspell

echo "/usr/lib/aspell/norwegian" > $RPM_BUILD_ROOT/usr/share/pspell/no-aspell.pwli

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.orig
/usr/share/aspell/*
/usr/lib/aspell/*
/usr/share/pspell/*

%changelog
* Fri Jun 14 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.3-3
- Rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Feb 26 2002 Trond Eivind Glomsrød <teg@redhat.com>
- Rebuild

* Wed Jan 23 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.3-1
- Bigger dictionary (combine the ones from 0.1 and 0.2, uniqify)

* Mon Sep 24 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.2-4
- Add a few common, but missing, words (#53911)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Tue May 01 2001 Bill Nottingham <notting@redhat.com>
- build on ia64

* Thu Feb  1 2001 Trond Eivind Glomsrød <teg@redhat.com>
- new dictionary, from the ispell 2.0 dictionary

* Sat Aug 19 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Wed Aug 16 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Tue Aug 01 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jun 30 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use the proper name on the pwli file

* Mon Jun 26 2000 Trond Eivind Glomsrød <teg@redhat.com>
- change build procedure
- include .pwli file

* Sat Jun 17 2000 Trond Eivind Glomsrød <teg@redhat.com>
- first RPM
