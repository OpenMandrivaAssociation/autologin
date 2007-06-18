Name:		autologin
Summary:	Automatically log in
Version:	1.0.0
Release:	%mkrel 16
Source0:	%{name}-%{version}.tar.bz2
Source1:	startx.autologin
Patch0:		autologin-1.0.0-mdk.patch.bz2
Group:		System/Base
URL:		http://www.linux-easy.com/development/autologin/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pam-devel automake1.4
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
export FORCE_AUTOCONF_2_5=1
aclocal-1.4
autoheader
automake-1.4
autoconf
%configure2_5x
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
