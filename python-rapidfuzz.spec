%undefine _debugsource_packages

Name:		python-rapidfuzz
Version:	3.14.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/r/rapidfuzz/rapidfuzz-%{version}.tar.gz
Summary:	rapid fuzzy string matching
URL:		https://pypi.org/project/rapidfuzz/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(scikit-build)
BuildRequires:	cmake
BuildRequires:	ninja

%description
rapid fuzzy string matching

%files
%{py_platsitedir}/rapidfuzz
%{py_platsitedir}/rapidfuzz-*.*-info
