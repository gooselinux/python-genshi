%{!?python_sitelib: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-genshi
Version:        0.5.1
Release:        7.1%{?dist}
Summary:        Toolkit for stream-based generation of output for the web

Group:          Development/Languages
License:        BSD
URL:            http://genshi.edgewall.org/

Source0:        http://ftp.edgewall.com/pub/genshi/Genshi-%{version}.tar.bz2
Patch0:         %{name}-%{version}-length_hint.patch
Patch1:		0001-Ported-913-927-and-928-to-the-0.5.x-branch.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel

Requires:       python-babel >= 0.8

%description
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or other
textual content for output generation on the web. The major feature is
a template language, which is heavily inspired by Kid.

%prep
%setup0 -q -n Genshi-%{version}
%patch0 -p0 -b .length_hint
%patch1 -p1

find examples -type f | xargs chmod a-x

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING doc examples README.txt 
%{python_sitearch}/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.5.1-7.1
- Rebuilt for RHEL 6

* Fri Sep 11 2009 Luke Macken <lmacken@redhat.com> - 0.5.1-7
- Add a patch to work around some recent Python2.6.2 behavior

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Luke Macken <lmacken@redhat.com> - 0.5.1-5
- Add python-babel as a requirement

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.5.1-3
- Rebuild for Python 2.6

* Thu Oct  9 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.5.1-2
- Add patch from upstream that fixes problems when using Genshi in
- conjuction with Babel.

* Tue Oct  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.5.1-1
- Version 0.5.1
- http://svn.edgewall.org/repos/genshi/tags/0.5.1/
- (Jul 9 2008, from branches/stable/0.5.x)
- 
-  * Fix problem with nested match templates not being applied when buffering
-    on the outer `py:match` is disabled. Thanks to Erik Bray for reporting the
-    problem and providing a test case!
-  * Fix problem in `Translator` filter that would cause the translation of
-    text nodes to fail if the translation function returned an object that was
-    not directly a string, but rather something like an instance of the
-    `LazyProxy` class in Babel (ticket #145).
-  * Fix problem with match templates incorrectly being applied multiple times.
-  * Includes from templates loaded via an absolute path now include the correct
-    file in nested directories as long if no search path has been configured
-    (ticket #240).
-  * Unbuffered match templates could result in parts of the matched content
-    being included in the output if the match template didn't actually consume
-    it via one or more calls to the `select()` function (ticket #243).

* Mon Jun  9 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.5-1
- Update to released version of Genshi.

* Thu Apr 24 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.5-0.1.svn847
- Update to snapshot of 0.5

* Tue Aug 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.4.4-2
- BR python-setuptools-devel

* Mon Aug 27 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.4.4-1
- Update to 0.4.4

* Mon Jul  9 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.4.2-2
- BR python-setuptools so that egg-info files get installed.  Fixes #247430.

* Thu Jun 21 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.4.2-1
- Update to 0.4.2

* Sat Jun  9 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.4.1-1
- Update to 0.4.1

* Wed Apr 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.4.0-1
- Update to 0.4.0

* Thu Apr 12 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.3.6-1
- First version for Fedora Extras

