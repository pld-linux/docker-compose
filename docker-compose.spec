#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define		module		compose
%define		egg_name	docker_compose
%define		pypi_name	docker-compose
Summary:	Multi-container orchestration for Docker
Name:		docker-compose
Version:	1.25.5
Release:	1
License:	Apache v2.0
Group:		Applications/System
# https://github.com/docker/compose/releases
Source0:	https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	a6f296957148e4c61b28fb324c27c966
Patch0:		remove-requires-upper-bound.patch
URL:		https://docs.docker.com/compose/
%if %{with tests}
BuildRequires:	python-PyYAML
BuildRequires:	python-docker
BuildRequires:	python-docopt
BuildRequires:	python-paramiko
BuildRequires:	python-requests
BuildRequires:	python-setuptools
BuildRequires:	python-texttable
BuildRequires:	python-websocket-client
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	docker(engine) >= 1.10.0
Requires:	python-docker >= 3.6.0
Requires:	python-setuptools
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
%doc CHANGELOG.md CONTRIBUTING.md README.md SWARM.md LICENSE
%attr(755,root,root) %{_bindir}/%{name}
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
