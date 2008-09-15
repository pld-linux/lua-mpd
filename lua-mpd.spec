Summary:	LuaMPD is an object-oriented interface to the MusicPD protocol
Summary(hu.UTF-8):	LuaMPD egy objektum-orientált interfész a MusicPD-hez.
Name:		lua-mpd
Version:	0.1b
Release:	1
License:	BSD-like
Group:		Development/Languages
Source0:	http://luaforge.net/frs/download.php/1744/lua_mpd-%{version}.tar.gz
# Source0-md5:	3b7ee42c0e705c3950ff47a0065edd5b
URL:		http://luaforge.net/projects/luampd/
BuildRequires:	lua51-devel
Requires:	lua-socket
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LuaMPD is an object-oriented interface to the MusicPD protocol. This
package may be useful to awesome window manager.

%description -l hu.UTF-8
LuaMPD egy objektum-orientált interfész a MusicPD-hez. Az awesome
ablakkezelőhöz lehet nagyon hasznos ez a csomag.

%prep
%setup -q -n lua_mpd

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/lua/5.1
cp src/lua_mpd.lua $RPM_BUILD_ROOT%{_datadir}/lua/5.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README test/test_luampd.lua
%attr(755,root,root) %{_datadir}/lua/5.1/lua_mpd.lua
