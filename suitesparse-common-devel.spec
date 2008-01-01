%define NAME	UFconfig
%define name	suitesparse-common-devel
%define version 3.1.0
%define release %mkrel 1

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
Obsoletes:	ufsparse-common-devel < %{epoch}:%{version}-%{release}
Provides:	ufsparse-common-devel = %{epoch}:%{version}-%{release}

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

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt
%{_includedir}/suitesparse/*.h
