%undefine _missing_build_ids_terminate_build
%global debug_package %{nil}

Name:           browserpass
Version:        3.1.0
Release:        1%{?dist}
Summary:        Native application for the browserpass browser extension
License:        ISC
URL:            https://github.com/browserpass/browserpass-native
Source:         %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

Requires:       gnupg2
BuildRequires:  golang
BuildRequires:  git
ExcludeArch:    ppc64

Recommends:     browserpass-chromium
Recommends:     browserpass-firefox
Suggests:       pass

%description
This is a host application for browserpass browser extension providing it
access to your password store. The communication is handled through Native
Messaging API.

%prep
%setup -qn %{name}-native-%{version}
make configure

%build
%make_build %{name}

%check
make test

%install
%make_install LIB_DIR=%{?buildroot}%{_libdir}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/%{name}/

%changelog
%autochangelog
