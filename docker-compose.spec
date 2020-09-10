#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define		module		compose
%define		egg_name	docker_compose
%define		pypi_name	docker-compose
Summary:	Multi-container orchestration for Docker
Name:		docker-compose
Version:	1.27.1
Release:	1
License:	Apache v2.0
Group:		Applications/System
# https://github.com/docker/compose/releases
Source0:	https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	2919b94bfec307aa1eff68bbb85e42c5
Patch0:		remove-requires-upper-bound.patch
URL:		https://docs.docker.com/compose/
%if %{with tests}
BuildRequires:	python3-PyYAML
BuildRequires:	python3-docker
BuildRequires:	python3-docopt
BuildRequires:	python3-paramiko
BuildRequires:	python3-requests
BuildRequires:	python3-setuptools
BuildRequires:	python3-texttable
BuildRequires:	python3-websocket-client
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	docker(engine) >= 1.10.0
Requires:	python3-docker >= 4.3.1
Requires:	python3-paramiko >= 2.4.2
Requires:	python3-setuptools
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
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md CONTRIBUTING.md README.md SWARM.md LICENSE
%attr(755,root,root) %{_bindir}/%{name}
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
