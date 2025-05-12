Name:       doxygen
Summary:    Automated C, C++, and Java Documentation Generator
Version:    1.13.2
Release:    1
License:    GPLv2+
URL:        https://github.com/sailfishos/doxygen/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  gettext
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  python3-base

%description
Doxygen is a documentation system for C, C++, Java, and IDL. It can
generate an online class browser (in HTML) and an offline reference
manual (in LaTeX) from a set of documented source files. The
documentation is extracted directly from the sources. Doxygen is
developed on a Linux platform, but it runs on most other UNIX flavors
as well. An executable for Windows 95/NT is also available.

%prep
%autosetup -p1 -n %{name}-%{version}/doxygen

%build
unset QTDIR
%cmake -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install
%cmake_install

rm -Rf %{buildroot}%{_mandir}

%files
%{_bindir}/doxygen
