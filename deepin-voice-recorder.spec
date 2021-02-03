Name:           deepin-voice-recorder
Version:        1.4.2
Release:        6%{?dist}
Summary:        Deepin Voice Recorder
License:        GPLv3+
URL:            https://github.com/linuxdeepin/deepin-voice-recorder
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  qt5-linguist
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  gcc
Requires:       hicolor-icon-theme
Requires:       deepin-manual-directory

%description
%{summary}.

%prep
%setup -q
sed -i 's|=lupdate|=lupdate-qt5|;s|=lrelease|=lrelease-qt5|' %{name}.pro
find manual -executable -name "*.svg" -exec chmod 0644 "{}" \;

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -pDm644 %{S:1} %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/dman/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.svg

%changelog
* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.2-5
- Rebuilt for new ffmpeg snapshot

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.4.2-3
- Rebuild for ffmpeg-4.3 git

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Zamir SUN <sztsian@gmail.com> - 1.4.2-1
- Update to 1.4.2

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 1.3.8-3
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Zamir SUN <sztsian@gmail.com> - 1.3.8-1
- Update to 1.3.8

* Fri Jul 20 2018 mosquito <sensor.wen@gmail.com> - 1.3.7-1
- Update to 1.3.7

* Tue Mar 20 2018 mosquito <sensor.wen@gmail.com> - 1.3.6.1-1
- Update to 1.3.6.1

* Sun Jan 21 2018 Zamir SUN <sztsian@gmail.com> - 1.3.6-3
- Add appdata file

* Fri Jan 12 2018 Zamir SUN <sztsian@gmail.com> - 1.3.6-2
- Prepare for rpmfusion

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 1.3.6-1
- Update to 1.3.6

* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 1.3.5-1
- Update to 1.3.5

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 1.3.3-1
- Update to 1.3.3

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 1.3.1-1.git6cf1cb9
- Update to 1.3.1

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 1.3-1.git6c05bf1
- Update to 1.3

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 1.2-1.git2a95a46
- Initial build
