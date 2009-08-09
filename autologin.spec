Summary:	Automatically log in
Name:		autologin
Version:	1.0.0
Release:	%mkrel 26
Group:		System/Base
License:	GPL
URL:		http://www.linux-easy.com/development/autologin/
Source0:	%{name}-%{version}.tar.bz2
Source1:	startx.autologin
Patch0:		autologin-1.0.0-mdv.patch
Patch1:		autologin-glibc28_fix.diff
BuildRequires:	pam-devel automake autoconf >= 2.50
Requires:	initscripts >= 5.15
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Autologin automatically logs in as the user specified in
/etc/sysconfig/autologin and starts the X session defined there.

Install autologin if you want to bypass the login screen.

%prep
%setup -q

%patch0 -p1 -b .fred
%patch1 -p0 -b .glibc28_fix

%build
#FORCE_AUTOCONF_2_5=1 AUTOMAKE="automake --add-missing" autoreconf
autoreconf -fiv
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

install -m755 %{SOURCE1} -D %{buildroot}%{_bindir}/startx.autologin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README AUTHORS
%{_sbindir}/autologin
%{_bindir}/startx.autologin
%config(noreplace) /etc/pam.d/autologin
