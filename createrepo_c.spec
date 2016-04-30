#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : createrepo_c
Version  : 0.1.14
Release  : 11
URL      : https://fedorahosted.org/releases/c/r/createrepo_c/createrepo_c-0.1.14.tar.xz
Source0  : https://fedorahosted.org/releases/c/r/createrepo_c/createrepo_c-0.1.14.tar.xz
Summary  : ""
Group    : Development/Tools
License  : LGPL-2.0 GPL-2.0
Requires: createrepo_c-bin
Requires: createrepo_c-lib
Requires: createrepo_c-data
Requires: createrepo_c-doc
BuildRequires : bzip2-dev
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : expat-dev
BuildRequires : file-dev
BuildRequires : libxml2-dev
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : popt-dev
BuildRequires : rpm-dev
BuildRequires : zlib-dev
Patch1: 0001-Fix-CMAKE_INSTALL_PREFIX.patch

%description


%package bin
Summary: bin components for the createrepo_c package.
Group: Binaries
Requires: createrepo_c-data

%description bin
bin components for the createrepo_c package.


%package data
Summary: data components for the createrepo_c package.
Group: Data

%description data
data components for the createrepo_c package.


%package dev
Summary: dev components for the createrepo_c package.
Group: Development
Requires: createrepo_c-lib
Requires: createrepo_c-bin
Requires: createrepo_c-data

%description dev
dev components for the createrepo_c package.


%package doc
Summary: doc components for the createrepo_c package.
Group: Documentation

%description doc
doc components for the createrepo_c package.


%package lib
Summary: lib components for the createrepo_c package.
Group: Libraries
Requires: createrepo_c-data

%description lib
lib components for the createrepo_c package.


%prep
%setup -q -n createrepo_c-0.1.14
%patch1 -p1

%build
mkdir clr-build
cd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DLIB_INSTALL_DIR=/usr/lib64
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
cd clr-build
%make_install
## make_install_append content
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
mv %{buildroot}%{_sysconfdir}/bash_completion.d/createrepo_c.bash %{buildroot}%{_datadir}/bash-completion/completions/createrepo_c
rm -rf %{buildroot}%{_sysconfdir}/bash_completion.d
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/createrepo_c
/usr/bin/mergerepo_c

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/createrepo_c

%files dev
%defattr(-,root,root,-)
/usr/include/createrepo_c/compression_wrapper.h
/usr/include/createrepo_c/constants.h
/usr/include/createrepo_c/createrepo_c.h
/usr/include/createrepo_c/load_metadata.h
/usr/include/createrepo_c/locate_metadata.h
/usr/include/createrepo_c/misc.h
/usr/include/createrepo_c/package.h
/usr/include/createrepo_c/parsehdr.h
/usr/include/createrepo_c/parsepkg.h
/usr/include/createrepo_c/repomd.h
/usr/include/createrepo_c/sqlite.h
/usr/include/createrepo_c/version.h
/usr/include/createrepo_c/xml_dump.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/createrepo_c/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
