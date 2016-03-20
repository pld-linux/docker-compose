#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

Summary:	Multi-container orchestration for Docker
Name:		docker-compose
Version:	1.6.2
Release:	2
License:	Apache v2.0
Source0:	https://pypi.python.org/packages/source/d/docker-compose/%{name}-%{version}.tar.gz
# Source0-md5:	1c80fd99f2dc393e8ac5313c9a2fa4c7
Group:		Applications/System
URL:		https://docs.docker.com/compose/
Patch0:		remove-requires-upper-bound.patch
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

# Upstream uses an underscore here
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
