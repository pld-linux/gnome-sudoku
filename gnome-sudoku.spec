Summary:	Simple interface for playing, saving, printing and solving Sudoku
Summary(pl.UTF-8):	Prosty interfejs do grania, zapisywania, drukowania i rozwiązywania Sudoku
Name:		gnome-sudoku
Version:	3.10.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-sudoku/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	ee06d241a3ad1dbfce29419e2f5ef62d
URL:		https://wiki.gnome.org/Apps/Sudoku
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.11
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	python-pygobject3-devel >= 2.28.3
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	gdk-pixbuf2
Requires:	gobject-introspection >= 0.10.0
Requires:	gtk+3
Requires:	hicolor-icon-theme
Requires:	python-pycairo
Requires:	python-pygobject3
Provides:	gnome-games-sudoku
Provides:	gnome-games-sudoku = 1:%{version}-%{release}
Obsoletes:	gnome-games-sudoku
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

%py_postclean

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
%{_iconsdir}/HighContrast/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%dir %{py_sitescriptdir}/gnome_sudoku
%{py_sitescriptdir}/gnome_sudoku/*.py[co]
%dir %{py_sitescriptdir}/gnome_sudoku/gtk_goodies
%{py_sitescriptdir}/gnome_sudoku/gtk_goodies/*.py[co]
%{_mandir}/man6/gnome-sudoku.6*
