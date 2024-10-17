%define major           0
%define penge_name      penge
%define libname         %mklibname %{penge_name} %{major}
%define develname       %mklibname %{penge_name} -d

Name: meego-panel-myzone
Summary: Myzone panel for MeeGo
Group: Graphical desktop/Other 
Version: 0.2.4
License: LGPL 2.1
URL: https://www.meego.com
Release: %mkrel 1
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libglib2-devel
BuildRequires: libGConf2-devel
BuildRequires: clutter-devel
BuildRequires: jana-devel
BuildRequires: gtk2-devel
BuildRequires: nbtk-devel
BuildRequires: meego-panel-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: mx-devel
Obsoletes: meego-panel-myzone <= 0.0.12

%description
MeeGo myzone panel for MeeGo

%package -n %{libname}
Summary: MeeGo's myzone library
Group: System/Libraries

%description -n %{libname}
MeeGo's myzone library

%package -n %{develname}
Summary: MeeGo's myzone library (development files)
Group: System/Libraries
Requires: %{libname} = %{version}-%{release}

%description -n %{develname}
MeeGo's myzone library (development files)

%prep
%setup -q 

%build
%configure2_5x --disable-static
#%make
make LIBS='$(PENGE_LIBS) $(MPL_LIBS) -ltelepathy-glib -ljana-ecal'

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING NEWS README AUTHORS ChangeLog
%{_libexecdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/*service
%{_sysconfdir}/gconf/schemas/meego-panel-myzone.schemas
%{_sysconfdir}/xdg/autostart/meego-panel-myzone.desktop
%{_datadir}/mutter-meego/panels/meego-panel-myzone.desktop
%{_datadir}/applications/myzone.desktop
%{_libdir}/control-center-1/extensions/*

%files -n %{libname}
%{_libdir}/lib%{penge_name}*.so.*

%files -n %{develname}
%{_libdir}/lib%{penge_name}*.so
%{_libdir}/lib%{penge_name}*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*
