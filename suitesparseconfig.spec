%define NAME	SuiteSparse_config
%define	major	4
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname -d %{name}

Summary:	Configuration file for SuiteSparse packages
Name:		suitesparseconfig
Version:	4.2.1
Release:	7
License:	LGPLv2+
Group:		Development/C
Url:		http://www.cise.ufl.edu/research/sparse/UFconfig/
Source0:	http://www.cise.ufl.edu/research/sparse/UFconfig/%{NAME}-%{version}.tar.gz
Patch0:		SuiteSparse_config-4.2.1-increase-default-optimizations.patch

%description
UFconfig provides a configuration header file needed by most of the other
packages in SuiteSparse. And static library with few functions.

%package -n	%{libname}
Summary:	Configuration library for SuiteSparse packages
Group:		System/Libraries

%description -n %{libname}
UFconfig provides a configuration header file needed by most of the other
packages in SuiteSparse. And static library with few functions.

%package -n	%{devname}
Summary:	Configuration files for SuiteSparse packages
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
%rename		suitesparse-common-devel
Provides:	ufsparse-common-devel = %{EVRD}

%description -n %{devname}
UFconfig provides a configuration header file needed by most of the other
packages in SuiteSparse. And static library with few functions.

%prep
%setup -q -n %{NAME}
%patch0 -p1 -b .opts~
chmod -R o+r .
sed	-e 's#^INSTALL_LIB =.*#INSTALL_LIB = %{_libdir}#g' \
	-e 's#^INSTALL_INCLUDE = .*#INSTALL_INCLUDE = %{_includedir}#g' \
	-e 's#^TBB =.*#TBB = -ltbb#g' \
	-e 's#^SQPR_CONFIG =.*#SQPR_CONFIG = DHAVE_TBB#g' \
	-e 's#^METIS =.*#METIS = -lmetis#g' \
	-i SuiteSparse_config.mk

%build
%make CFLAGS="%{optflags}"
ar x lib%{name}.a
gcc %{ldflags} -shared -Wl,-soname,lib%{name}.so.%{major} -o \
        lib%{name}.so.%{version} *.o

%install
for f in *.so*; do
    install -m755 $f -D %{buildroot}%{_libdir}/`basename $f`
done
for f in *.a; do
    install -m644 $f -D %{buildroot}%{_libdir}/`basename $f`
done
for f in *.h *.mk; do
    install -m644 $f -D %{buildroot}%{_includedir}/suitesparse/`basename $f`
done

ln -s lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%doc README.txt
%dir %{_includedir}/suitesparse/
%{_includedir}/suitesparse/*.*
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.a
