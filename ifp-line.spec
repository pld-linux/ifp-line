# TODO:
# - a lot of things...
Summary:	iRiver command line interface
Name:		ifp-line
Version:	0.2.4.5
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/ifp-driver/%{name}-%{version}.tar.gz
# Source0-md5:	53985c0f00a842026195eed8a4bdd7c5
#Source1:	ifpdev.sh
Requires:	hotplug
URL:		http://ifp-driver.sourceforge.net/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
- this project aims to be an open-source driver for iRiver iFP flash
  player
- currently, it's a command line utility, which uses libusb to access
  USB
- one can use Midnight Commander as frontend
- ifp supported manager firmware; not supported UMS firmware

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/hotplug/usb,%{_mandir}/man1

install ifp $RPM_BUILD_ROOT%{_bindir}
install ifp.1 $RPM_BUILD_ROOT%{_mandir}/man1
#install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/etc/hotplug/usb/ifpdev

%post
#grep -q "^ifp:" /etc/group
#if [ $? -ne 0 ]; then
#	/usr/sbin/groupadd ifp &> /dev/null
#	echo "ifp group added"
#fi
#
#egrep -q '^ifpdev[[:blank:]]' /etc/hotplug/usb.usermap
#if [ $? -ne 0 ]; then
#	cat >> /etc/hotplug/usb.usermap << EOF
#
## for iRiver iFP MP3 player
#ifpdev 0x0003 0x4102 0x1001 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#ifpdev 0x0003 0x4102 0x1003 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#ifpdev 0x0003 0x4102 0x1005 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#ifpdev 0x0003 0x4102 0x1007 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#ifpdev 0x0003 0x4102 0x1008 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#ifpdev 0x0003 0x4102 0x1009 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#ifpdev 0x0003 0x4102 0x1010 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#
#EOF
#
#	echo "/etc/hotplug/usb.usermap changed."
#fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING NEWS TIPS nonroot.sh
%attr(755,root,root) %{_bindir}/*
#/etc/hotplug/usb/ifpdev
%{_mandir}/man1/*.1*
