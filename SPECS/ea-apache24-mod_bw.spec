%global ns_name ea-apache24
%global upstream_name mod_bw

Name: %{ns_name}-%{upstream_name}
Version: 0.92
Summary: Set a limit to the maximum speed available to certains users to download.

# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4556 for more details
%define release_prefix 2
License: Apache License, Version 2.0
Release: %{release_prefix}%{?dist}.cpanel
Group: System Environment/Daemons
Vendor: cPanel, Inc.
URL: https://sourceforge.net/projects/bwmod/files/bwmod/mod_bw%200.92/
Source: mod_bw-0.92.tgz
Patch0: mod_bw-apache24-api.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: ea-apache24-devel
Requires: ea-apache24

%description
Bandwidth mod is an apache module extension, which enables the web admin to set a limit to the max    imum speed available to certains users to download. Controls Apache Bandwidth Per Virtualhost

%prep
%setup -q -n mod_bw

%patch0 -p1 -b .apache24api

%build
%{_httpd_apxs} -c mod_bw.c
mv .libs/%{upstream_name}.so .
%{__strip} -g %{upstream_name}.so

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_httpd_moddir}

install %{upstream_name}.so %{buildroot}%{_httpd_moddir}/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/apache2/conf.modules.d/
mkdir -p $RPM_BUILD_ROOT/usr/local/cpanel/scripts
install -p $RPM_SOURCE_DIR/491_mod_bw.conf $RPM_BUILD_ROOT%{_sysconfdir}/apache2/conf.modules.d/491_mod_bw.conf
install -p $RPM_SOURCE_DIR/setbwlimit $RPM_BUILD_ROOT/usr/local/cpanel/scripts/setbwlimit

%clean
%{__rm} -rf %{buildroot}

%files
%{_libdir}/apache2/modules/mod_bw.so
%config(noreplace) %{_sysconfdir}/apache2/conf.modules.d/491_mod_bw.conf
/usr/local/cpanel/scripts/setbwlimit

%changelog
* Mon Jun 19 2017 Jacob Perkins <jacob.perkins@cpanel.net> - 0.92-2
- Adjusted installation to ULC/scripts

* Mon Apr 03 2017 Dan Muey <dan@cpanel.net> - 0.92-1
- EA-6015: Initial mod_bw for ea4
