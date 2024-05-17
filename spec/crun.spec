Name:        crun
Version:     1.15
Release:     e9b84d1.oe2203
Summary:     crun

License:     Apache-2.0
URL:         https://github.com/iscas-fork/crun
Source0:     %{name}-%{version}.tar.gz

Requires: yajl

%description

%prep
%setup -n %{name}-%{version}
cp -r /root/rpmbuild/BUILD/%{name}-%{version} /root/rpmbuild/BUILDROOT/%{name}-%{version}-%{release}.x86_64

%files
%defattr (-,root,root,0755)
/usr/bin/crun
/etc/iscas/share/libhook.so
