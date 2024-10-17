Summary:	Tetris meets Space Invaders
Name:		gemdropx
Version:	0.9
Release:	13
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/gemdropx/gemdropx-%{version}.tar.bz2
License:	GPLv2+
Url:		https://newbreedsoftware.com/gemdropx
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	imagemagick
Patch0:		%{name}-0.9-fix-CFLAGS.patch

%description
Gem Drop X is a fast-paced puzzle game where it's your job to clear the screen
of gems before they squash you! (You're at the bottom, they're at the top, and
they keep coming!)

%prep
%setup -q
%patch0 -p1
chmod a+r -R .
rm -rf `find -type d -name .xvpics`

%build
%make CFLAGS="%{optflags}" DATA_PREFIX=%{_gamesdatadir}/%{name}/

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_gamesbindir}/%{name}
install -d $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
cp -a data/* $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}

%{__install} -d $RPM_BUILD_ROOT{%{_liconsdir},%{_miconsdir}}
convert data/images/gemdropx-icon.xpm -size 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert data/images/gemdropx-icon.xpm -size 32x32 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert data/images/gemdropx-icon.xpm -size 48x48 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gem Drop X
Comment=%{summary}
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGES.txt README.txt
%{_gamesdatadir}/%{name}
%{_datadir}/applications/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}


%changelog
* Thu Feb 03 2011 Funda Wang <fwang@mandriva.org> 0.9-12mdv2011.0
+ Revision: 635493
- tighten BR

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-11mdv2011.0
+ Revision: 610827
- rebuild

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 0.9-10mdv2010.1
+ Revision: 508342
- fix CFLAGS

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.9-10mdv2009.0
+ Revision: 245878
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 14 2007 Funda Wang <fwang@mandriva.org> 0.9-8mdv2008.1
+ Revision: 119616
- drop menu

  + Thierry Vignaud <tv@mandriva.org>
    - buildrequires X11-devel instead of XFree86-devel
    - import gemdropx


* Fri Jul  7 2006 Pixel <pixel@mandriva.com> 0.9-7mdv2007.0
- switch to XDG menu

* Fri Feb  3 2006 Pixel <pixel@mandriva.com> 0.9-6mdk
- rebuild

* Fri Nov 12 2004 Pixel <pixel@mandrakesoft.com> 0.9-5mdk
- rebuild

* Mon Aug 04 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9-4mdk
- rebuild
- move stuff to %%{_gamesbindir} and %%{_gamesdatadir}
- drop Prefix tag
- added menu item
- added icons
- use %%make macro
- get rid of .xvpics lying around
- cosmetics

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.9-3mdk
- rebuild

* Sun Jul 21 2002 Pixel <pixel@mandrakesoft.com> 0.9-2mdk
- recompile against new vorbis stuff

* Thu Jun 27 2002 Pixel <pixel@mandrakesoft.com> 0.9-1mdk
- new release

* Mon Apr 29 2002 Pixel <pixel@mandrakesoft.com> 0.7-9mdk
- rebuild for new libasound (alsa)

* Mon Jan 21 2002 Stefan van der Eijk <stefan@eijk.nu> 0.7-8mdk
- BuildRequires

* Thu Sep 13 2001 Stefan van der Eijk <stefan@eijk.nu> 0.7-7mdk
- BuildRequires: libSDL-devel

* Thu Sep  6 2001 Pixel <pixel@mandrakesoft.com> 0.7-6mdk
- rebuild

* Mon May 14 2001 Pixel <pixel@mandrakesoft.com> 0.7-5mdk
- rebuild with new SDL

* Tue Dec 19 2000 Pixel <pixel@mandrakesoft.com> 0.7-4mdk
- reuibld for new libSDL_mixer

* Wed Nov 29 2000 Pixel <pixel@mandrakesoft.com> 0.7-3mdk
- rebuild, build req

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 0.7-2mdk
- rebuild

* Thu Nov  2 2000 Pixel <pixel@mandrakesoft.com> 0.7-1mdk
- initial spec


# end of file
