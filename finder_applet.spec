Summary:	A Battery  monitor for linuxppc.
Name:		finder_applet
Version:	0.4.1
Release:	0
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://students.washington.edu/mpalczew/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is a MacOS Finder like applet menu for GNOME.

%prep
%setup -q
%build
./configure --prefix=/usr --sysconfdir=%{_sysconfdir}
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/CORBA/servers/
install -d $RPM_BUILD_ROOT%{_datadir}/applets/Utility
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps/finder_applet

install src/finder_applet $RPM_BUILD_ROOT%{_bindir}
install support/finder_applet.desktop $RPM_BUILD_ROOT%{_datadir}/applets/Utility
install support/finder_applet.gnorba $RPM_BUILD_ROOT%{_sysconfdir}/CORBA/servers

%files
%defattr(644,root,root,755)
%doc README TODO COPYING 

%attr(755,root,root) %{_bindir}/finder_applet
%{_datadir}/applets/Utility/finder_applet.desktop
%{_sysconfdir}/CORBA/servers/finder_applet.gnorba


%clean
rm -rf $RPM_BUILD_ROOT
