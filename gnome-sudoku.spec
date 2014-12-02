Summary:	Simple interface for playing, saving, printing and solving Sudoku
Summary(pl.UTF-8):	Prosty interfejs do grania, zapisywania, drukowania i rozwiązywania Sudoku
Name:		gnome-sudoku
Version:	3.14.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-sudoku/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	73445779e693ed5b847435c0f7c9ef11
URL:		https://wiki.gnome.org/Apps/Sudoku
BuildRequires:	appdata-tools
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	json-glib-devel
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	libtool >= 2:2.4
BuildRequires:	pkgconfig
BuildRequires:	qqwing-devel >= 1.2.0
BuildRequires:	vala >= 2:0.26.0
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.14.0
Requires:	hicolor-icon-theme
Requires:	qqwing-libs >= 1.2.0
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
%{__libtoolize}
%{__aclocal} -I m4
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
%{_datadir}/glib-2.0/schemas/org.gnome.sudoku.gschema.xml
%{_datadir}/gnome-sudoku
%{_desktopdir}/gnome-sudoku.desktop
%{_iconsdir}/HighContrast/*/apps/gnome-sudoku.png
%{_iconsdir}/hicolor/*/apps/gnome-sudoku.png
%{_iconsdir}/hicolor/scalable/apps/gnome-sudoku.svg
%{_mandir}/man6/gnome-sudoku.6*
