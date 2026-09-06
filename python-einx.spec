Name:		python-einx
Version:	0.4.3
Release:	1
Summary:	Universal numpy-style tensor operations
License:	MIT
Group:		Development/Python
URL:		https://github.com/fferflo/einx
Source0:	https://files.pythonhosted.org/packages/source/e/einx/einx-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python%{pyver}dist(numpy)
Requires:	python%{pyver}dist(sympy)
Requires:	python%{pyver}dist(frozendict)

# setuptools.packages.find only excludes test_typechecking*, so
# test/ and docs/ land in site-packages. Drop them after install.
%install -a
rm -rf %{buildroot}%{py_sitedir}/test %{buildroot}%{py_sitedir}/docs

%description
einx provides a universal notation for tensor operations, similar to
einops. Required by vector-quantize-pytorch (ACE-Step FSQ tokenizer).

%files
%doc README.md
%license LICENSE
%{py_sitedir}/einx
%{py_sitedir}/einx-*.*-info
