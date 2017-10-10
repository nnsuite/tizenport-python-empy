Name:           python-empy
Version:        3.3.3
Release:        0
License:        LGPL-2.1
Summary:        A powerful and robust templating system for Python
Url:            http://www.alcyone.com/software/empy/
Group:          Development/Languages/Python
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  python-devel

%description
EmPy is a system for embedding Python expressions and statements in
template text; it takes an EmPy source file, processes it, and
produces output. This is accomplished via expansions, which are
special signals to the EmPy system and are set off by a special prefix
(by default the at sign, @). EmPy can expand arbitrary Python
expressions and statements in this way, as well as a variety of
special forms. Textual data not explicitly delimited in this way is
sent unaffected to the output, allowing Python to be used in effect as
a markup language. Also supported are callbacks via hooks, recording
and playback via diversions, and dynamic, chainable filters. The
system is highly configurable via command line options and embedded
commands.

%prep
%setup -q
cp %{SOURCE1001} .	
sed -i -e '1d' em.py

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
