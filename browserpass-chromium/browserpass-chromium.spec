%undefine _missing_build_ids_terminate_build
%global debug_package %{nil}
%global id pjmbgaakjkbhpopmakjoedenlfdmcdgm

Name:           browserpass-chromium
Version:        3.8.0
Release:        2%{?dist}
Summary:        Chromium extension for Browserpass, browser extension for zx2c4's pass (password manager)
License:        ISC
BuildArch:      noarch
URL:            https://github.com/browserpass/browserpass-extension
Source0:        %{URL}/releases/download/%{version}/browserpass-github-%{version}.crx
Source1:        %{URL}/releases/download/%{version}/browserpass-github-%{version}.crx.asc
Source2:        https://raw.githubusercontent.com/browserpass/browserpass-extension/master/LICENSE
Source3:        https://maximbaz.com/pgp_keys.asc

BuildRequires:  gnupg2
Requires:       browserpass

%description
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE3}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
cat << EOF > "%{id}.json"
{
    "external_crx": "%{_libdir}/%{name}/%{name}-%{version}.crx",
    "external_version": "%{version}"
}
EOF

%build

%check

%install
%{__install} -Dm644 -t "%{buildroot}/usr/share/chromium/extensions/" "%{id}.json"
%{__install} -Dm644 "%{SOURCE0}" "%{buildroot}/%{_libdir}/%{name}/%{name}-%{version}.crx"
%{__install} -dm755 "%{buildroot}/etc/chromium/native-messaging-hosts/"
ln -sf "%{_libdir}/browserpass/hosts/chromium/com.github.browserpass.native.json" "%{buildroot}/etc/chromium/native-messaging-hosts/"
%{__install} -Dm644 -t "%{buildroot}/usr/share/licenses/%{name}/" "%{SOURCE2}"

%files
%license LICENSE
%{_libdir}/%{name}/
/etc/chromium/native-messaging-hosts/
/usr/share/chromium/extensions/

%changelog
%autochangelog
