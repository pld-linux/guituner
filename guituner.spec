Summary:	GuiTuner - a simple guitar tuning program
Summary(pl):	GuiTuner - program do strojenia gitary
Name:		guituner
Version:	0.02
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://digilander.libero.it/guituner/downloads/%{name}_%{version}.tar.gz
# Source0-md5:	aa071f1250aaaaa0068c839bdcd34445
Source1:        %{name}.desktop
URL:		http://digilander.libero.it/guituner
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	fftw-devel
BuildRequires:	glib-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GuiTuner is a simple guitar tuning program.

%description -l pl
GuiTuner to prosty program do strojenia gitary.

%prep
%setup -q -n %{name}_%{version}

%build
%{__aclocal} -I macros
%{__libtoolize}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*
