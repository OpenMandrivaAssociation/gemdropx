%define	name	gemdropx
%define	version	0.9
%define release	%mkrel 8
%define	Summary	Tetris meets Space Invaders
Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/gemdropx/gemdropx-%{version}.tar.bz2
License:	GPLv2+
Url:		http://newbreedsoftware.com/gemdropx
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL_mixer-devel X11-devel alsa-lib-devel esound-devel ImageMagick
Patch:		%{name}-0.9-fix-CFLAGS.patch.bz2

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
