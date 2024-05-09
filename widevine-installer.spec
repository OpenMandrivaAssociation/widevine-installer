Name:           widevine-installer
Version:        2.0
Release:        1
Summary:        Widevine CDM installer
License:        MIT
URL:            https://openmandriva.org/
Source0:        widevine-installer
Source1:	https://github.com/AsahiLinux/widevine-installer/raw/main/widevine_fixup.py

ExclusiveArch:	%{x86_64} %{aarch64}

%ifarch %{x86_64}
Requires:	tar
Requires(post):	tar
%endif

%ifarch %{aarch64}
Requires:       glibc >= 2.36
# For extracting a ChromeOS image
Requires:	squashfs-tools
# For widevine_fixup.py
Requires:       python
Requires(post):	squashfs-tools
Requires(post):	python
%endif

BuildRequires:  coreutils

Requires:       coreutils
Requires:       curl

Requires(post):	bash
Requires(post):	curl

Enhances:       chromium
Enhances:       firefox
Enhances:       %{_lib}Qt6WebEngineCore

%description
This tool will download and install Widevine systemwide for aarch64 and x86_64
systems. It performs the necessary configuration changes to make Widevine
available for both Firefox and Chromium-based browsers.

%install
mkdir -p %{buildroot}%{_bindir}
install -c -m 755 %{S:0} %{buildroot}%{_bindir}/

%ifarch %{aarch64}
mkdir -p %{buildroot}%{_libexecdir}
install -c -m 755 %{S:1} %{buildroot}%{_libexecdir}/
%endif

%files
%{_bindir}/widevine-installer
%ifarch %{aarch64}
%{_libexecdir}/widevine_fixup.py
%endif
%ghost /opt/widevine
%ghost /opt/widevine/libwidevinecdm.so

%post
%{_bindir}/widevine-installer
