Summary:	Waloon dictionary for aspell
Summary(pl):	S³ownik waloñski dla aspella
Name:		aspell-wa
Version:	0.50
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/wa/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	e3817402d7be19d4b0d0342d3a5970ea
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.50.0
Requires:	aspell >= 3:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Waloon dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik (lista s³ów) waloñski  dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
