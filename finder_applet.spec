Summary: A Battery  monitor for linuxppc.
Name: finder_applet
Version: 0.4
Release: 0
Copyright: GPL
Group: X11/Utilities
Source: http://students.washington.edu/mpalczew/finder_applet-0.4.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot

%description
This is a MacOS Finder like applet menu for GNOME.  

%prep
%setup -q
%build
./configure --prefix=/usr --sysconfdir=/etc
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/CORBA/servers/
mkdir -p $RPM_BUILD_ROOT/usr/share/applets/Utility
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/finder_applet

install src/finder_applet $RPM_BUILD_ROOT/usr/bin
install support/finder_applet.desktop $RPM_BUILD_ROOT/usr/share/applets/Utility
install support/finder_applet.gnorba $RPM_BUILD_ROOT/etc/CORBA/servers

%files
%defattr(-,root,root)
%doc README TODO COPYING 

/usr/bin/finder_applet
/usr/share/applets/Utility/finder_applet.desktop
/etc/CORBA/servers/finder_applet.gnorba
