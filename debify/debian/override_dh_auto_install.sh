#!/bin/bash

source debian/vars.sh

set -x 

mkdir -p $DEB_INSTALL_ROOT$_httpd_moddir
install $upstream_name.so $DEB_INSTALL_ROOT$_httpd_moddir/
mkdir -p $DEB_INSTALL_ROOT$_sysconfdir/apache2/conf.modules.d/
mkdir -p $DEB_INSTALL_ROOT/usr/local/cpanel/scripts
install -p $RPM_SOURCE_DIR/491_mod_bw.conf $DEB_INSTALL_ROOT$_sysconfdir/apache2/conf.modules.d/491_mod_bw.conf
install -p $RPM_SOURCE_DIR/setbwlimit $DEB_INSTALL_ROOT/usr/local/cpanel/scripts/setbwlimit

