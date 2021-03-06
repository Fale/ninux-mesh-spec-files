%global pypi_name cookies
%global sum Friendlier RFC 6265-compliant cookie parser/renderer

Name:           python-%{pypi_name}
Version:        2.2.1
Release:        1%{?dist}
Summary:        Friendlier RFC 6265-compliant cookie parser/renderer

License:        MIT
URL:            https://gitlab.com/sashahart/cookies
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:		https://gitlab.com/sashahart/cookies/raw/master/LICENSE

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  pytest
BuildRequires:  python3-pytest

%description
cookies.py is a Python module for working with HTTP cookies:
parsing and rendering ‘Cookie:’ request headers and ‘Set-Cookie:’
response headers, and exposing a convenient API for creating
and modifying cookies. It can be used as a replacement of
Python’s Cookie.py (aka http.cookies).

%package -n python2-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
cookies.py is a Python module for working with HTTP cookies:
parsing and rendering ‘Cookie:’ request headers and ‘Set-Cookie:’
response headers, and exposing a convenient API for creating
and modifying cookies. It can be used as a replacement of
Python’s Cookie.py (aka http.cookies).


%package -n python3-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
cookies.py is a Python module for working with HTTP cookies:
parsing and rendering ‘Cookie:’ request headers and ‘Set-Cookie:’
response headers, and exposing a convenient API for creating
and modifying cookies. It can be used as a replacement of
Python’s Cookie.py (aka http.cookies).


%prep
%setup -q -n %{pypi_name}-%{version}
cp %{SOURCE1} .
rm test_cookies.py

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
# removing test_cookies.py to avoid import file mismatch error
# imported module 'test_cookies' has this __file__ attribute:
#   /home/makerpm/rpmbuild/BUILD/cookies-2.2.1/test_cookies.py
# which is not the same as the test file we want to collect:
#   /home/makerpm/rpmbuild/BUILD/cookies-2.2.1/build/lib/test_cookies.py
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE
%doc README
%{python2_sitelib}/*

%files -n python3-%{pypi_name}
%license LICENSE
%doc README
%{python3_sitelib}/*

%changelog
* Fri Jan 15 2016 Germano Massullo <germano.massullo@gmail.com> - 2.2.1-1
- First commit on Fedora's Git