%define		vendor_version	2.33.1

Summary:	Multi-container orchestration for Docker
Name:		docker-compose
Version:	2.33.1
Release:	1
License:	Apache v2.0
Group:		Applications/System
# https://github.com/docker/compose/releases
Source0:	https://github.com/docker/compose/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	25b2e28a0dd4eb5141915ba91b8dbcc1
Source1:	%{name}-vendor-%{vendor_version}.tar.xz
# Source1-md5:	115906d7b51c96f7380d068576e42b84
Source2:	docker-compose.sh
URL:		https://docs.docker.com/compose/
BuildRequires:	golang >= 1.22.10
BuildRequires:	rpmbuild(macros) >= 2.009
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	docker-ce-cli
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	_debugsource_packages

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
%setup -q -n compose-%{version} -a1

%{__mv} compose-%{vendor_version}/vendor .

%build
%{__make} \
	VERSION="%{version}" \
	BUILD_FLAGS="-v -mod=vendor"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libexecdir}/docker/cli-plugins}

cp -p bin/build/docker-compose $RPM_BUILD_ROOT%{_libexecdir}/docker/cli-plugins
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/docker-compose

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING.md README.md LICENSE
%attr(755,root,root) %{_bindir}/docker-compose
%attr(755,root,root) %{_libexecdir}/docker/cli-plugins/docker-compose
