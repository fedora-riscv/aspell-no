%define lang no
%define langrelease 2
Summary: Norwegian dictionaries for Aspell.
Name: aspell-%{lang}
Version: 0.50
Release: 3
License: GPL
Group: Applications/Text
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell >= 0.50
Requires: aspell >= 0.50
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Provides the word list/dictionaries for the following: Norwegian

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n aspell-%{lang}-%{version}-%{langrelease}

%build
echo "ASPELL = aspell" > Makefile
echo "DEST_DIR = $RPM_BUILD_ROOT" >> Makefile
echo "WORD_LIST_COMPRESS = word-list-compress" >> Makefile
echo "dictdir = ${RPM_BUILD_ROOT}%{_libdir}/aspell" >> Makefile
echo "datadir = ${RPM_BUILD_ROOT}%{_datadir}/aspell" >> Makefile
cat Makefile.pre >> Makefile
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Mon Jun 23 2003 Adrian Havill <havill@redhat.com> 0.50-3
- first build for new aspell (0.50)
