%undefine _missing_build_ids_terminate_build
%global debug_package %{nil}

Name:           browserpass-firefox
Version:        3.8.0
Release:        1%{?dist}
Summary:        Firefox extension for Browserpass, browser extension for zx2c4's pass (password manager)
License:        ISC
BuildArch:      noarch
URL:            https://github.com/browserpass/browserpass-extension
Source0:        https://addons.mozilla.org/firefox/downloads/file/4187654/browserpass_ce-%{version}.xpi
Source1:        https://raw.githubusercontent.com/browserpass/browserpass-extension/master/LICENSE

Requires:       browserpass

%description
%{summary}.

%prep

%build

%check

%install
%{__install} -Dm644 "%{SOURCE0}" "%{buildroot}%{_libdir}/firefox/browser/extensions/browserpass@maximbaz.com.xpi"
%{__install} -dm755 "%{buildroot}%{_libdir}/mozilla/native-messaging-hosts/"
ln -sf "%{_libdir}/browserpass/hosts/firefox/com.github.browserpass.native.json" "%{buildroot}%{_libdir}/mozilla/native-messaging-hosts/"
%{__install} -Dm644 -t "%{buildroot}/usr/share/licenses/%{name}/" "%{SOURCE1}"

%files
%license LICENSE
%{_libdir}/firefox/browser/extensions/
%{_libdir}/mozilla/native-messaging-hosts/

%changelog
%autochangelog
