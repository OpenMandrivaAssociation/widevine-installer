%global git 20231126
%global debug_package %{nil}

Name:           widevine-installer
Version:        0^%{git}
Release:        1
Summary:        Widevine CDM installer for aarch64 systems

License:        MIT
URL:            https://github.com/AsahiLinux/widevine-installer
Source0:        %{name}-1.%{git}.tar.xz
#Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  bash
BuildRequires:  coreutils
#BuildRequires:  systemd-rpm-macros
BuildRequires:  sed

Requires:       bash
Requires:       coreutils
Requires:       curl
Requires:       glibc >= 2.36
Requires:       python
Requires:       setup
Requires:       squashfs-tools
Requires:       systemd

#Enhances:       chromium
Enhances:       firefox
#Enhances:       qt5-webengine
#Enhances:       qt6-webengine

ExclusiveArch:  aarch64

%description
This tool will download and install Widevine systemwide for aarch64 systems. It
performs the necessary configuration changes to make Widevine available for
both Firefox and Chromium-based browsers.

%prep
%autosetup -p1 -n %{name}-1.%{git}

# Configs are already installed by the package
sed -i 's/COPY_CONFIGS=1/COPY_CONFIGS=0/' widevine-installer

%build
# Nothing to build

%install
DESTDIR="%{buildroot}" ./widevine-installer --distinstall

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%dir %{_libdir}/chromium-browser
%{_libdir}/chromium-browser/WidevineCdm
%dir %{_libdir}/firefox
%dir %{_libdir}/firefox/defaults
%dir %{_libdir}/firefox/defaults/pref
%{_libdir}/firefox/defaults/pref/gmpwidevine.js
%{_sysconfdir}/profile.d/gmpwidevine.sh
#dir %{_sharedstatedir}/widevine
%dir %ghost %{_sharedstatedir}/widevine/gmp-widevinecdm
%dir %ghost %{_sharedstatedir}/widevine/gmp-widevinecdm/system-installed
%ghost %{_sharedstatedir}/widevine/gmp-widevinecdm/system-installed/libwidevinecdm.so
%ghost %{_sharedstatedir}/widevine/gmp-widevinecdm/system-installed/manifest.json
%ghost %{_sharedstatedir}/widevine/libwidevinecdm.so
%ghost %{_sharedstatedir}/widevine/LICENSE
%ghost %{_sharedstatedir}/widevine/manifest.json
/var/lib/widevine/README
%dir %ghost %{_sharedstatedir}/widevine/WidevineCdm
%ghost %{_sharedstatedir}/widevine/WidevineCdm/manifest.json
%dir %ghost %{_sharedstatedir}/widevine/WidevineCdm/_platform_specific
%dir %ghost %{_sharedstatedir}/widevine/WidevineCdm/_platform_specific/linux_arm64
%ghost %{_sharedstatedir}/widevine/WidevineCdm/_platform_specific/linux_arm64/libwidevinecdm.so
%dir %ghost %{_sharedstatedir}/widevine/WidevineCdm/_platform_specific/linux_x64
%ghost %{_sharedstatedir}/widevine/WidevineCdm/_platform_specific/linux_x64/libwidevinecdm.so
