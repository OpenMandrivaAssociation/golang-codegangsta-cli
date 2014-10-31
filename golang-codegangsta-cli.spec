%global debug_package   %{nil}
%global import_path     github.com/codegangsta/cli
%global commit          565493f259bf868adb54d45d5f4c68d405117adf
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%define gosrc %{go_dir}/src/pkg/%{import_path}

Name:           golang-codegangsta-cli
Version:        1.2.0
Release:        2
Summary:        Package for building command line apps in Go
License:        MIT
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	golang

%description
cli.go is simple, fast, and fun package for building command line apps in Go.
The goal is to enable developers to write fast and distributable command line
applications in an expressive way.

%package devel
# Earliest NVR containing relevant golang macros
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        Package for building command line apps in Go
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
cli.go is simple, fast, and fun package for building command line apps in Go.
The goal is to enable developers to write fast and distributable command line
applications in an expressive way.

This package contains library source intended for building other packages
which use codegangsta/cli.

%prep
%setup -n cli-%{version}

%build

%install
install -d -p %{buildroot}%{gosrc}
cp -pav *.go %{buildroot}%{gosrc}

%files devel
%doc LICENSE README.md
%{gosrc}/
