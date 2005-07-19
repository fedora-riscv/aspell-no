%define lang nb
%define langrelease 0
Summary: Norwegian dictionaries for Aspell.
#Name: aspell-%{lang}
Name: aspell-no
Epoch: 50
Version: 0.50.1
Release: 9
License: GPL
Group: Applications/Text
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell-%{lang}-%{version}-%{langrelease}.tar.bz2
Patch: aspell-nb-0.50.1-0.utf-filename.patch
Buildrequires: aspell >= 12:0.60
Requires: aspell >= 12:0.60
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%define debug_package %{nil}

%description
Provides the word list/dictionaries for the following: Norwegian

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n aspell-%{lang}-%{version}-%{langrelease}
%patch -p1 -b .utf-filename
mv $(echo -e 'bokm\345l.alias') $(echo -e 'bokm\303\245l.alias')

%build
echo "ASPELL = aspell" > Makefile
echo "DEST_DIR = $RPM_BUILD_ROOT" >> Makefile
echo "WORD_LIST_COMPRESS = word-list-compress" >> Makefile
echo "dictdir = ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60" >> Makefile
echo "datadir = ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60" >> Makefile
cat Makefile.pre >> Makefile
make

%install
make install
cp ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60/nb.multi ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60/no.multi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{_libdir}/aspell-0.60/*
#%{_datadir}/aspell/*

%changelog
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
