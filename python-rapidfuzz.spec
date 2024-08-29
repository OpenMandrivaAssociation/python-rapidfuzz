%undefine _debugsource_packages

Name:		python-rapidfuzz
Version:	3.9.6
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/r/rapidfuzz/rapidfuzz-%{version}.tar.gz
Summary:	rapid fuzzy string matching
URL:		https://pypi.org/project/rapidfuzz/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(scikit-build)
BuildRequires:	pkgconfig(python3)
BuildRequires:	cmake
BuildRequires:	ninja

%description
rapid fuzzy string matching

%prep
%autosetup -p1 -n rapidfuzz-%{version}

%build
%py_build

%install
%py_install

%files
%{py_platsitedir}/rapidfuzz
%{py_platsitedir}/rapidfuzz-*.*-info
