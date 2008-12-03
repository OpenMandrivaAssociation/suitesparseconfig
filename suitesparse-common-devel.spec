%define NAME	UFconfig
%define name	suitesparse-common-devel
%define version 3.2.0
%define release %mkrel 2

Summary: 	Configuration file for SuiteSparse packages
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	LGPL
Group:		Development/C
Url:		http://www.cise.ufl.edu/research/sparse/UFconfig/
Source0: 	http://www.cise.ufl.edu/research/sparse/UFconfig/%{NAME}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Obsoletes:	suitesparse-common-devel < %{version}-%{release}
Obsoletes:	suitesparse-static-devel 
Obsoletes:	ufsparse-common-devel < %{version}-%{release}
Provides:	ufsparse-common-devel = %{version}-%{release}

%description
UFconfig provides a configuration header file needed by most of the other 
packages in SuiteSparse.

%prep
%setup -q -n %{NAME}

%build

%install
%__rm -rf %{buildroot}
%__install -d -m 755 %{buildroot}/%{_includedir}/suitesparse
%__install -m 644 *.h %{buildroot}/%{_includedir}/suitesparse
%__install -m 644 *.mk %{buildroot}/%{_includedir}/suitesparse

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt
%{_includedir}/suitesparse/*.*
