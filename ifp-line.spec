# TODO:
# - proper connection with hotplug
# - integration with mc
Summary:	iRiver command line interface
Summary(pl):	Interfejs linii poleceñ do urz±dzeñ iRiver
Name:		ifp-line
Version:	0.2.4.5
Release:	0.2
License:	GPL v2
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/ifp-driver/%{name}-%{version}.tar.gz
# Source0-md5:	53985c0f00a842026195eed8a4bdd7c5
#Source1:	ifpdev.sh
Patch0:		%{name}-DESTDIR.patch
URL:		http://ifp-driver.sourceforge.net/
BuildRequires:	libusb-devel
Requires:	hotplug
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
- this project aims to be an open-source driver for iRiver iFP flash
  player
- currently, it's a command line utility, which uses libusb to access
  USB
- one can use Midnight Commander as frontend
- ifp supported manager firmware; not supported UMS firmware

%description -l pl
Ten projekt ma byæ sterownikiem z otwartymi ¼ród³ami do odtwarzaczy
iRiver iFP. Aktualnie dostêpne jest narzêdzie dzia³aj±ce z linii
poleceñ, u¿ywaj±ce libusb do dostêpu do USB. Mo¿na u¿ywaæ Midnight
Commandera jako frontendu. ifp obs³uguje firmware managera, nie
obs³uguje natomiast UMS.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `libusb-config --cflags` -Wall" \
	LDFLAGS="%{rpmcflags} `libusb-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/hotplug/usb,%{_mandir}/man1}

%{__make} install \
	PREFIX=%{_prefix} \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

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
## for iRiver iFP MP3 player
#ifpdev 0x0003 0x4102 0x1001 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#ifpdev 0x0003 0x4102 0x1003 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#ifpdev 0x0003 0x4102 0x1005 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#ifpdev 0x0003 0x4102 0x1007 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#ifpdev 0x0003 0x4102 0x1008 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#ifpdev 0x0003 0x4102 0x1009 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#ifpdev 0x0003 0x4102 0x1010 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000
#EOF
#	echo "/etc/hotplug/usb.usermap changed."
#fi

%files
%defattr(644,root,root,755)
%doc NEWS README TIPS nonroot.sh
%attr(755,root,root) %{_bindir}/*
#/etc/hotplug/usb/ifpdev
%{_mandir}/man1/*.1*
