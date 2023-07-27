Summary:	Simple interface for playing, saving, printing and solving Sudoku
Summary(pl.UTF-8):	Prosty interfejs do grania, zapisywania, drukowania i rozwiązywania Sudoku
Name:		gnome-sudoku
Version:	44.0
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/gnome-sudoku/44/%{name}-%{version}.tar.xz
# Source0-md5:	bd81e3a0af4ebd301cab3beeb7561e5b
URL:		https://wiki.gnome.org/Apps/Sudoku
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	json-glib-devel
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	meson >= 0.59
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	qqwing-devel >= 1.3.4
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.36
BuildRequires:	vala-libgee >= 0.8
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.40.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.24.0
Requires:	hicolor-icon-theme
Requires:	qqwing-libs >= 1.3.4
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-sudoku
%{_datadir}/dbus-1/services/org.gnome.Sudoku.service
%{_datadir}/glib-2.0/schemas/org.gnome.Sudoku.gschema.xml
%{_datadir}/metainfo/org.gnome.Sudoku.appdata.xml
%{_desktopdir}/org.gnome.Sudoku.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Sudoku.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Sudoku-symbolic.svg
%{_mandir}/man6/gnome-sudoku.6*
