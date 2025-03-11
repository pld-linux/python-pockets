#
# Conditional build:
%bcond_with	doc	# Sphinx documentation (not included in sdist)
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A collection of helpful Python tools
Summary(pl.UTF-8):	Zbiór przydatnych narzędzi dla Pythona
Name:		python-pockets
Version:	0.9.1
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pockets/
Source0:	https://files.pythonhosted.org/packages/source/p/pockets/pockets-%{version}.tar.gz
# Source0-md5:	4f7e699bd6d1a6b05e1a71905c1d58d1
URL:		https://pypi.org/project/pockets/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest >= 3.0.7
BuildRequires:	python-pytz >= 2018.3
BuildRequires:	python-six >= 1.5.2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 3.0.7
BuildRequires:	python3-pytz >= 2018.3
BuildRequires:	python3-six >= 1.5.2
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-sphinx-napeleon-typehints >= 2.1.6
BuildRequires:	sphinx-pdg-2 >= 1.8.5
%endif
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pockets full of useful Python tools!

The Pockets library pulls together many of the Python helper functions
found useful over the years.

%description -l pl.UTF-8
Kieszenie pełne przydatnych narzędzi dla Pythona!

Biblioteka Pockets zbiera wiele funkcji pomocniczych, uznanych za
przydatne na przestrzeni lat.

%package -n python3-pockets
Summary:	A collection of helpful Python tools
Summary(pl.UTF-8):	Zbiór przydatnych narzędzi dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pockets
Pockets full of useful Python tools!

The Pockets library pulls together many of the Python helper functions
found useful over the years.

%description -n python3-pockets -l pl.UTF-8
Kieszenie pełne przydatnych narzędzi dla Pythona!

Biblioteka Pockets zbiera wiele funkcji pomocniczych, uznanych za
przydatne na przestrzeni lat.

%package apidocs
Summary:	API documentation for Python pockets module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pockets
Group:		Documentation

%description apidocs
API documentation for Python pockets module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pockets.

%prep
%setup -q -n pockets-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.rst
%{py_sitescriptdir}/pockets
%{py_sitescriptdir}/pockets-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pockets
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.rst
%{py3_sitescriptdir}/pockets
%{py3_sitescriptdir}/pockets-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
