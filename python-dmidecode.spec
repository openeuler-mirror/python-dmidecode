Name:           python-dmidecode
Version:        3.12.2
Release:        18
Summary:        Python extension module for dmidecode

License:        GPLv2
URL:            http://projects.autonomy.net.au/python-dmidecode/
Source0:        https://github.com/nima/python-dmidecode/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc libxml2-devel python2-libxml2 python3-libxml2
BuildRequires:  python2-devel python3-devel

%description
Dmidecode reports information about your system's hardware as described in
your system BIOS according to the SMBIOS/DMI standard. This information
typically includes system manufacturer, model name, serial number, BIOS
version, asset tag as well as a lot of other details of varying level of
interest and reliability depending on the manufacturer. This will often
include usage status for the CPU sockets, expansion slots (e.g. AGP, PCI,
ISA) and memory module slots, and the list of I/O ports (e.g. serial,
parallel, USB).

Python-dmidecode is a python extension module that uses the code-base
of the 'dmidecode' utility and uses libxml2 to display data as python
data structures or XML data.

%package        -n python2-dmidecode
Summary:        A python 2 extension module to get DMI data
Requires:       python2-libxml2
%{?python_provide:%python_provide python2-dmidecode}

%description    -n python2-dmidecode
Python2-dmidecode is a python 2 extension module that uses the code-base
of the 'dmidecode' utility and uses libxml2 to display data as python 2
data structures or XML data.

%package        -n python3-dmidecode
Summary:        A python 3 module to access DMI data
Requires:       python3-libxml2

%description    -n python3-dmidecode
Python3-dmidecode is a python 3 extension module that uses the code-base
of the 'dmidecode' utility and uses libxml2 to display data as python 3
data structures or XML data.

%package_help

%prep
%autosetup -c -n %{name}-%{version} -p1
cp -a %{name}-%{version} python2
cp -a %{name}-%{version} python3
rm -r %{name}-%{version}
pushd python3
sed -i 's/python2/python3/g' Makefile unit-tests/Makefile
popd

%build
export CFLAGS="${CFLAGS-} -std=gnu89"
pushd python2
make build
popd
pushd python3
make build
popd

%install
pushd python2
%{__python2} src/setup.py install --root %{buildroot} --prefix=%{_prefix}
popd
pushd python3
%{__python3} src/setup.py install --root %{buildroot} --prefix=%{_prefix}
popd

%check
pushd python2/unit-tests
make
popd
pushd python3/unit-tests
make
popd

%files -n python2-dmidecode
%license python2/doc/LICENSE python2/doc/AUTHORS python2/doc/AUTHORS.upstream
%{python2_sitearch}/dmidecode.py
%{python2_sitearch}/dmidecode.pyc
%{python2_sitearch}/dmidecode.pyo
%{python2_sitearch}/dmidecodemod.so
%{python2_sitearch}/python_dmidecode-3.12.2-py2.7.egg-info
%{_datadir}/python-dmidecode/pymap.xml

%files -n python3-dmidecode
%license python3/doc/LICENSE python3/doc/AUTHORS python3/doc/AUTHORS.upstream
%{python3_sitearch}/__pycache__/*.pyc
%{python3_sitearch}/dmidecode.py
%{python3_sitearch}/dmidecodemod.cpython-3*.so
%{python3_sitearch}/python_dmidecode-3.12.2-py3.*.egg-info
%{_datadir}/python-dmidecode/pymap.xml

%files help
%doc python2/README python2/doc/README.upstream
%doc python3/README python3/doc/README.upstream

%changelog
* Thu Jun 16 2020 hanhui <hanhui15@huawei.com> - 3.12.2-18
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:Modify the file patch for python3.8

* Sun Dec 29 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.12.2-17
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:optimization the spec 

* Thu Nov 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.12.2-16
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:Modify the file name for x86

* Sat Sep 28 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.12.2-15
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:Modify the file path of the help package

* Mon Sep 09 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.12.2-14
- Package Init
