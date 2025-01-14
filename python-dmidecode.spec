Name:           python-dmidecode
Version:        3.12.3
Release:        2
Summary:        Python extension module for dmidecode

License:        GPLv2
URL:            http://projects.autonomy.net.au/python-dmidecode/
Source0:        https://github.com/nima/python-dmidecode/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%ifarch sw_64
Patch1:         python-dmidecode-3.12.3-sw.patch
%endif

BuildRequires:  gcc libxml2-devel python3-libxml2 python3-devel

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

%package        -n python3-dmidecode
Summary:        A python 3 module to access DMI data
Requires:       python3-libxml2

%description    -n python3-dmidecode
Python3-dmidecode is a python 3 extension module that uses the code-base
of the 'dmidecode' utility and uses libxml2 to display data as python 3
data structures or XML data.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1
sed -i 's/python2/python3/g' Makefile unit-tests/Makefile

%build
export PYTHON_BIN=%{__python3}
export PYTHON_VERSION=%{python3_version}
export CFLAGS="%{build_cflags} -std=gnu89"
export CC=gcc
%make_build

%install
export CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="${RPM_LD_FLAGS}"
%{__python3} src/setup.py install --root %{buildroot} --prefix=%{_prefix}

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export PYTHON_BIN=%{__python3}
make -C unit-tests

%files -n python3-dmidecode
%license doc/LICENSE doc/AUTHORS doc/AUTHORS.upstream
%{python3_sitearch}/__pycache__/*.pyc
%{python3_sitearch}/dmidecode.py
%{python3_sitearch}/dmidecodemod.cpython-3*.so
%{python3_sitearch}/python_dmidecode-3.12.2-py3.*.egg-info
%{_datadir}/python-dmidecode/pymap.xml

%files help
%doc README doc/README.upstream

%changelog
* Wed Mar 01 2023 zhouwenpei <zhouwenpei@h-partners.com> - 3.12.3-2
- strip binary file

* Tue Dec 6 2022 chendexi <chendexi@kylinos.cn> - 3.12.3-1
- Upgrade to 3.12.3

* Wed Nov 23 2022 wuzx<wuzx1226@qq.com> - 3.12.2-24
- Add sw64 architecture

* Mon Jun 6 2022 yangcheng <yangcheng87@h-partners.com> - 3.12.2-23
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:strip binary file

* Thu Apr 14 2022 dongyuzhen <dongyuzhen@h-partners.com> - 3.12.2-22
- fix test case failed

* Sat Mar 20 2021 Dehui Fan<fandehui1@huawei.com> - 3.12.2-21
- strip binary files

* Fri Oct 30 2020 chengguipeng <chengguipeng1@huawei.com> - 3.12.2-20
- remove python2-dmidecode subpackage

* Wed Sep 9 2020 hanhui <hanhui15@huawei.com> - 3.12.2-19
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:modify source url

* Tue Jun 16 2020 hanhui <hanhui15@huawei.com> - 3.12.2-18
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
