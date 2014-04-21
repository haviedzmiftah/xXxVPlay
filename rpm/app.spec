%define name xXxVPlay.ign
%define release 1
%define version 1.0
%define license MIT
%define url http://example.com
%define group System Environment/Base

Summary:IGOS Nusantara SDK Application
Name:%{name}
Version:%{version}
Release:%{release}
License:%{license}
Group:%{group}
URL:%{url}
Source0:%{name}.tar.gz
BuildRoot:%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:ignsdk
BuildArch:noarch
%description
%{description}
xXxVplay adalah aplikasi multimedia detector pornografi

%prep
%setup -q -n %{name}

%install
%include %{buildsubdir}/rpm/install_list.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir
%config %attr(0755,root,root) 
/opt/ignsdk/*
/usr/share/applications/*

%changelog

* Mon Feb 18 2013 foo <foo@bar.org>
- First Build
