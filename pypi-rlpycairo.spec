#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-rlpycairo
Version  : 0.0.7
Release  : 5
URL      : https://files.pythonhosted.org/packages/20/47/ff0e6c7e765e7eb96310e1171e854db8fbcb0950e9366f6d3695c64cc1b2/rlPyCairo-0.0.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/20/47/ff0e6c7e765e7eb96310e1171e854db8fbcb0950e9366f6d3695c64cc1b2/rlPyCairo-0.0.7.tar.gz
Summary  : Plugin backend renderer for reportlab.graphics.renderPM
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-rlpycairo-license = %{version}-%{release}
Requires: pypi-rlpycairo-python = %{version}-%{release}
Requires: pypi-rlpycairo-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pycairo)
BuildRequires : pypi(reportlab)

%description
README
        =====================================
        
        (C) Copyright ReportLab Europe Ltd. 2000-2021.
        See ``LICENSE.txt`` for license details.
        
        This is a plugin for the ReportLab PDF Toolkit.
        which constructs rich PDF documents, and also creation
        of charts in a variety of bitmap and vector formats.
        
        This plugin is intended to replace most of the usage of the
        libart based C extension _renderPM which has been shown to
        have issues when rendering complex documents.
        
        This backend can be brought into use by setting 
        reportlab.rl_config.renderPMBackend = 'rlPyCairo'
        any of the methods detailed in reportlab/rl_config.py
        can be used to accomplish this.
        
        The new backend seems able to handle all the same behaviour as
        _renderPM and the only place where it seems inferior is in the
        rendering of scaled images and the speed with which it draws
        text.
        
        At present the rlPyCairo backend only uses the _renderPM extension 
        to use its mapping of ReportLab font names to extract paths for
        rendering this is no doubt the reason for its slowness when
        rendering text.
        
        Currently we are not making use of any of the more advanced 
        abilities of PyCairo such as transparency, patterns etc,
        but that may change in the future.

%package license
Summary: license components for the pypi-rlpycairo package.
Group: Default

%description license
license components for the pypi-rlpycairo package.


%package python
Summary: python components for the pypi-rlpycairo package.
Group: Default
Requires: pypi-rlpycairo-python3 = %{version}-%{release}

%description python
python components for the pypi-rlpycairo package.


%package python3
Summary: python3 components for the pypi-rlpycairo package.
Group: Default
Requires: python3-core
Requires: pypi(pycairo)
Requires: pypi(reportlab)

%description python3
python3 components for the pypi-rlpycairo package.


%prep
%setup -q -n rlPyCairo-0.0.7
cd %{_builddir}/rlPyCairo-0.0.7
pushd ..
cp -a rlPyCairo-0.0.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656376375
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-rlpycairo
cp %{_builddir}/rlPyCairo-0.0.7/rlPyCairo/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-rlpycairo/9de627173b67374df2be7bb7e87519f54d811a11
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-rlpycairo/9de627173b67374df2be7bb7e87519f54d811a11

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
