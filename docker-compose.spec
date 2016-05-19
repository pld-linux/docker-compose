#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

Summary:	Multi-container orchestration for Docker
Name:		docker-compose
Version:	1.7.1
Release:	1
License:	Apache v2.0
Group:		Applications/System
# https://github.com/docker/compose/releases
# https://pypi.python.org/pypi/docker-compose
Source0:	https://pypi.python.org/packages/b6/20/0a65e13ac06c4693f28ded22b87882ca1750239bdc0a05d4a4df4e3a9faa/%{name}-%{version}.tar.gz
# Source0-md5:	8c2b9a88c3aa46dbef422c7eb6802108
Patch0:		remove-requires-upper-bound.patch
URL:		https://docs.docker.com/compose/
%if %{with tests}
BuildRequires:	python-PyYAML
BuildRequires:	python-docker
BuildRequires:	python-docopt
BuildRequires:	python-requests
BuildRequires:	python-setuptools
BuildRequires:	python-texttable
BuildRequires:	python-websocket-client
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	docker >= 1.10.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Multi-container orchestration for Docker

Docker-compose allows you to:
- Define your application's environment with Docker so it can be
  reproduced anywhere.
- Define the services that make up your app so they can be run
  together in an isolated environment.
- Run 'docker-compose up', and docker-compose will start and run your
  entire app.

%prep
%setup -q
%patch0 -p1

rm -r docker_compose.egg-info

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md CONTRIBUTING.md README.rst SWARM.md LICENSE
%attr(755,root,root) %{_bindir}/%{name}
%{py_sitescriptdir}/compose
%{py_sitescriptdir}/docker_compose-%{version}-py*.egg-info
