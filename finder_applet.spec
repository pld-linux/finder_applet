Summary:	MacOS Finder like applet menu for GNOME
Summary(pl):	Aplet menu GNOME podobny do Findera z MacOS
Name:		finder_applet
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://students.washington.edu/mpalczew/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gnome-core-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This is a MacOS Finder like applet menu for GNOME.

%description -l pl
To jest aplet menu GNOME podobny do Findera z MacOS.

%prep
%setup -q
%build
./configure --prefix=/usr --sysconfdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/CORBA/servers
install -d $RPM_BUILD_ROOT%{_datadir}/applets/Utility
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps/finder_applet

install src/finder_applet $RPM_BUILD_ROOT%{_bindir}
install support/finder_applet.desktop $RPM_BUILD_ROOT%{_datadir}/applets/Utility
install support/finder_applet.gnorba $RPM_BUILD_ROOT%{_sysconfdir}/CORBA/servers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO

%attr(755,root,root) %{_bindir}/finder_applet
%{_datadir}/applets/Utility/finder_applet.desktop
%{_sysconfdir}/CORBA/servers/finder_applet.gnorba
