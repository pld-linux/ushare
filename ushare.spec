Summary:	uShare is a UPnP A/V Media Server
Summary(pl.UTF-8):	uShare jest serwerem mediów A/V UPnP
Name:		ushare
Version:	0.9.7
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://ushare.geexbox.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	e978c648f808cf1740b1583a78b922ff
Patch0:		%{name}-rc.d.patch
URL:		http://www.geexbox.org/wiki/index.php/UShare
BuildRequires:	libupnp-devel >= 1.3.1
BuildRequires:  rpmbuild(macros) >= 1.228
Requires(post,preun):   /sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uShare is a UPnP (TM) A/V Media Server. It implements the server
component that provides UPnP media devices with information on
available multimedia files.

%description -l pl.UTF-8
uShare jest serwerem mediów A/V UPnP. Implementuje komponenty serwera,
który udostępnia urządzeniom UPnP media z informacjami.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%post
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun
if [ "$1" = "0" ]; then
        %service -q %{name} stop
        /sbin/chkconfig --del %{name}
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/ushare.conf
%attr(755,root,root) /usr/bin/ushare
%{_mandir}/man1/*
