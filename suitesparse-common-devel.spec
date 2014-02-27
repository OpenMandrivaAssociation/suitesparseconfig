%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define NAME	SuiteSparse_config

Summary:	Configuration file for SuiteSparse packages
Name:		suitesparse-common-devel
Version:	4.2.1
Release:	2
License:	LGPL
Group:		Development/C
Url:		http://www.cise.ufl.edu/research/sparse/UFconfig/
Source0:	http://www.cise.ufl.edu/research/sparse/UFconfig/%{NAME}-%{version}.tar.gz
Patch0:		SuiteSparse_config-4.2.1-increase-default-optimizations.patch
Provides:	ufsparse-common-devel = %{version}-%{release}

%description
UFconfig provides a configuration header file needed by most of the other
packages in SuiteSparse. And static library with few functions.

%prep
%setup -q -n %{NAME}
%patch0 -p1 -b .opts~
chmod 0644 README.txt

%build
%make CF="%{optflags}"

%install
install -d -m 755 %{buildroot}/%{_includedir}/suitesparse
install -m 644 *.h %{buildroot}/%{_includedir}/suitesparse
install -m 644 *.mk %{buildroot}/%{_includedir}/suitesparse

install -d -m 755 %{buildroot}/%{_libdir}
install -m 644 *.a %{buildroot}/%{_libdir}

%files
%doc README.txt
%dir %{_includedir}/suitesparse/
%{_includedir}/suitesparse/*.*
%{_libdir}/*.a
