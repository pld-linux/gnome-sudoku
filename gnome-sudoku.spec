Summary:	Simple interface for playing, saving, printing and solving Sudoku
Summary(pl.UTF-8):	Prosty interfejs do grania, zapisywania, drukowania i rozwiązywania Sudoku
Name:		gnome-sudoku
Version:	3.12.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-sudoku/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	db1751f2053475cb9c0f820bea41f07a
URL:		https://wiki.gnome.org/Apps/Sudoku
BuildRequires:	appdata-tools
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gnome-common
BuildRequires:	intltool >= 0.50.0
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-pygobject3-devel >= 3.12.0
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	gdk-pixbuf2 >= 2.0
Requires:	glib2 >= 2.0
Requires:	gobject-introspection >= 0.10.0
Requires:	gtk+3 >= 3.0
Requires:	hicolor-icon-theme
Requires:	pango
Requires:	python3-pycairo
Requires:	python3-pygobject3 >= 3.12.0
Provides:	gnome-games-sudoku = 1:%{version}-%{release}
Obsoletes:	gnome-games-sudoku < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Sudoku provides a simple interface for playing, saving, printing
and solving Sudoku.

%description -l pl.UTF-8
GNOME Sudoku dostarcza prosty interfejs do grania, zapisywania,
drukowania i rozwiązywania Sudoku.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-sudoku
%{_datadir}/appdata/gnome-sudoku.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-sudoku.gschema.xml
%{_datadir}/gnome-sudoku
%{_desktopdir}/gnome-sudoku.desktop
%{_iconsdir}/HighContrast/*/apps/gnome-sudoku.png
%{_iconsdir}/hicolor/*/apps/gnome-sudoku.png
%{_iconsdir}/hicolor/scalable/apps/gnome-sudoku.svg
%dir %{py3_sitescriptdir}/gnome_sudoku
%{py3_sitescriptdir}/gnome_sudoku/*.py
%{py3_sitescriptdir}/gnome_sudoku/__pycache__
%dir %{py3_sitescriptdir}/gnome_sudoku/gtk_goodies
%{py3_sitescriptdir}/gnome_sudoku/gtk_goodies/*.py
%{py3_sitescriptdir}/gnome_sudoku/gtk_goodies/__pycache__
%{_mandir}/man6/gnome-sudoku.6*
