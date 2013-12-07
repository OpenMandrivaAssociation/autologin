Summary:	Automatically log in
Name:		autologin
Version:	1.0.0
Release:	34
Group:		System/Base
License:	GPL
URL:		http://www.linux-easy.com/development/autologin/
Source0:	%{name}-%{version}.tar.bz2
Source1:	startx.autologin
Patch0:		autologin-1.0.0-mdv.patch
Patch1:		autologin-glibc28_fix.diff
Patch2:		autologin-1.0.0-automake-1.13.patch
BuildRequires:	pam-devel automake autoconf >= 2.50
Requires:	initscripts >= 5.15

%description
Autologin automatically logs in as the user specified in
/etc/sysconfig/autologin and starts the X session defined there.

Install autologin if you want to bypass the login screen.

%prep
%setup -q

%patch0 -p1 -b .fred
%patch1 -p0 -b .glibc28_fix
%patch2 -p1 -b .automake13~

%build
#FORCE_AUTOCONF_2_5=1 AUTOMAKE="automake --add-missing" autoreconf
autoreconf -fiv
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

install -m755 %{SOURCE1} -D %{buildroot}%{_bindir}/startx.autologin

%files
%defattr(-,root,root,0755)
%doc README AUTHORS
%{_sbindir}/autologin
%{_bindir}/startx.autologin
%config(noreplace) /etc/pam.d/autologin


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-29mdv2011.0
+ Revision: 662897
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-28mdv2011.0
+ Revision: 603483
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-27mdv2010.1
+ Revision: 520012
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-26mdv2010.0
+ Revision: 413147
- rebuild

  + Funda Wang <fwang@mandriva.org>
    - use configure2_5x

* Fri Mar 06 2009 Emmanuel Andry <eandry@mandriva.org> 1.0.0-25mdv2009.1
+ Revision: 350613
- use autoreconf to fix x86_64 build

  + Antoine Ginies <aginies@mandriva.com>
    - 2009.1 rebuild

* Thu Sep 11 2008 Pixel <pixel@mandriva.com> 1.0.0-24mdv2009.0
+ Revision: 283812
- fix keyboard not working (#39549)

* Wed Jul 02 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-23mdv2009.0
+ Revision: 230703
- added P1 to make it build (misc)
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jun 19 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0-20mdv2008.0
+ Revision: 41172
- try again. let's just conflict with autoconf2.1.
- bump for BS
- try to fix autotools failure
- BuildRequires autoconf; simplify autotools calls; bunzip2 and rename patch; rebuild for 2008
- Import autologin



* Thu Aug 17 2006 Olivier Blin <blino@mandriva.com> 1.0.0-16mdv2007.0
- fix doc to specify that AUTOLOGIN defaults to "no" (#20925)

* Mon Aug 14 2006 Pixel <pixel@mandriva.com> 1.0.0-15mdv2007.0
- move startx.autologin from /usr/X11R6/bin to /usr/bin
- modify startx.autologin to call /usr/bin/startx

* Sun May 28 2006 Stefan van der Eijk <stefan@eijk.nu> 1.0.0-14mdk
- %%mkrel
- remark to maintainer: URL is not correct

* Fri May 12 2006 Stefan van der Eijk <stefan@eijk.nu> 1.0.0-13mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.0.0-12mdk
- Rebuild

* Mon May 30 2005 Frederic Lepied <flepied@mandriva.com> 1.0.0-11mdk
- fix build

* Wed Jan 12 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.0-10mdk
- fix buildrequires
- cosmetics

* Tue Sep 28 2004 Frederic Lepied <flepied@mandrakesoft.com> 1.0.0-9mdk
- fixed build problem

* Mon Oct 20 2003 Frederic Lepied <flepied@mandrakesoft.com> 1.0.0-8mdk
- rebuild for rewriting /etc/pam.d file

* Fri Mar  7 2003 Frederic Lepied <flepied@mandrakesoft.com> 1.0.0-7mdk
- launch startx.autologin instead of startx

* Tue Apr  9 2002 Frederic Lepied <flepied@mandrakesoft.com> 1.0.0-6mdk
- prefix all error messages by "autologin " for better spotting (Sitsofe Wheeler).

* Fri Jun  1 2001 Frederic Lepied <flepied@mandrakesoft.com> 1.0.0-5mdk
- use pam_stack in pam file.

* Tue Feb  6 2001 Frederic Lepied <flepied@mandrakesoft.com> 1.0.0-4mdk
- don't report an error if the user is not set, just exit properly.

* Wed Oct  4 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.0-3mdk
- set path to /usr/X11R6/bin:/usr/local/bin:/bin:/usr/bin (close bug #558).

* Fri Sep 22 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.0-2mdk
- kill the child when autologin receive SIGTERM to work nicely with init.
- corrected the init of groups.
- log output to /var/log/autologin.log.

* Fri Aug 25 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.0-1mdk
- first Mandrake rpm

* Mon Aug 14 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- initial public RPM
