%define name	autologin
%define version	1.0.0
%define release	%mkrel 20

Name:		%{name}
Summary:	Automatically log in
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source1:	startx.autologin
Patch0:		autologin-1.0.0-mdv.patch
Group:		System/Base
URL:		http://www.linux-easy.com/development/autologin/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pam-devel automake autoconf >= 2.50
License:	GPL
Requires:	initscripts >= 5.15

%description
Autologin automatically logs in as the user specified in
/etc/sysconfig/autologin and starts the X session defined there.

Install autologin if you want to bypass the login screen.

%prep
%setup -q
%patch0 -p1 -b .fred

%build
FORCE_AUTOCONF_2_5 AUTOMAKE="automake --add-missing" autoreconf
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}
install -m755 %{SOURCE1} -D $RPM_BUILD_ROOT/usr/bin/startx.autologin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README AUTHORS
%{_sbindir}/autologin
/usr/bin/startx.autologin
%config(noreplace) /etc/pam.d/autologin
