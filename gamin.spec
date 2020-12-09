Summary: Library providing the FAM File Alteration Monitor API
Name: gamin
Version: 0.1.10
Release: 1
License: LGPL
Group: Development/Libraries
Source: gamin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://www.gnome.org/~veillard/gamin/
Obsoletes: fam
Provides: fam
BuildRequires: glib2-devel python python-devel

%description
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.

%package devel
Summary: Libraries, includes, etc. to embed the Gamin library
Group: Development/Libraries
Requires: gamin = %{version}
Obsoletes: fam-devel
Provides: fam-devel

%description devel
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.

%package python
Summary: Python bindings for the gamin library
Group: Development/Libraries
Requires: gamin = %{version}
Requires: %{_libdir}/python%(echo `python -c "import sys; print sys.version[0:3]"`)

%description python
The gamin-python package contains a module that allow monitoring of
files and directories from the Python language based on the support
of the gamin package.

%prep
%setup -q

%build
%configure
make

%install
rm -fr %{buildroot}

%makeinstall
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -fr %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README Copyright TODO
%doc doc/*.html
%doc doc/*.gif
%doc doc/*.txt
%{_libdir}/lib*.so.*
%{_libexecdir}/gam_server

%files devel
%defattr(-, root, root)

%{_libdir}/lib*.so
%{_libdir}/*a
%{_includedir}/fam.h
%{_libdir}/pkgconfig/gamin.pc

%files python
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README Copyright TODO
%{_libdir}/python*/site-packages/gamin.py*
%{_libdir}/python*/site-packages/_gamin*
%doc python/tests/*.py
%doc doc/python.html

%changelog
* Thu Oct 27 2005 Daniel Veillard <veillard@redhat.com> 0.1.7-1
- hopefully fixes gam_server crashes
- some portability fixes
- removed a minor leak
* Thu Sep  8 2005 Daniel Veillard <veillard@redhat.com> 0.1.6-1
- revamp of the inotify back-end
- memory leak fix
- various fixes and cleanups
* Tue Aug  9 2005 Daniel Veillard <veillard@redhat.com> 0.1.5-1
- Improvement of configuration, system wide configuration files and
  per filesystem type default
- Rewrite of the inotify back-end, reduce resources usage, tuning in
  case of busy resources
- Documentation updates
- Changes to compile inotify back-end on various architectures
- Debugging output improvements
* Tue Aug  2 2005 Daniel Veillard <veillard@redhat.com> 0.1.3-1
- Fix to compile on older gcc versions
- Inotify back-end changes and optimizations
- Debug ouput cleanup, pid and process name reports
- Dropped kernel monitor bugfix
- Removed the old glist copy used for debugging
- Maintain mounted filesystems knowledge, and per fstype preferences
* Wed Jul 13 2005 Daniel Veillard <veillard@redhat.com> 0.1.2-1
- inotify back end patches, ready for the new inotify support in kernel
- lot of server code cleanup patches
- fixed an authentication problem
* Fri Jun 10 2005 Daniel Veillard <veillard@redhat.com> 0.1.1-1
- gamin_data_conn_event fix
- crash from bug gnome #303932
- Inotify and mounted media #171201
- mounted media did not show up on Desktop #159748
- write may not be atomic
- Monitoring a directory when it is a file
- Portability to Hurd/Mach and various code cleanups
- Added support for ~ as user home alias in .gaminrc
* Thu May 12 2005 Daniel Veillard <veillard@redhat.com> 0.1.0-1
- Close inherited file descriptors on exec of gam_server
- Cancelling a monitor send back a FAMAcknowledge
- Fixed for big files > 2GB
- Bug when monitoring a non existing directory
- Make client side thread safe
- Unreadable directory fixes
- Better flow control handling
- Updated to latest inotify version: 0.23-6
* Tue Mar 15 2005 Daniel Veillard <veillard@redhat.com> 0.0.26-1
- Fix an include problem showing up with gcc4</li>
- Fix the crash on failed tree assert bug #150471 based on patch from Dean Brettle
- removed an incompatibility with SGI FAM #149822
* Tue Mar  1 2005 Daniel Veillard <veillard@redhat.com> 0.0.25-1
- Fix a configure problem reported by Martin Schlemmer
- Fix the /media/* and /mnt/* mount blocking problems from 0.0.24 e.g. #142637
- Fix the monitoring of directory using poll and not kernel
* Fri Feb 18 2005 Daniel Veillard <veillard@redhat.com> 0.0.24-1
- more documentation
- lot of serious bug fixes including Gnome Desktop refresh bug
- extending the framework for more debug (configure --enable-debug-api)
- extending the python bindings for watching the same resource multiple times
  and adding debug framework support
- growing the regression tests a lot based on python bindings
- inotify-0.19 patch from John McCutchan
- renamed python private module to _gamin to follow Python PEP 8

* Tue Feb  8 2005 Daniel Veillard <veillard@redhat.com> 0.0.23-1
- memory corruption fix from Mark on the client side
- extending the protocol and API to allow skipping Exists and EndExists
  events to avoid deadlock on reconnect or when they are not used.

* Mon Jan 31 2005 Daniel Veillard <veillard@redhat.com> 0.0.22-1
- bit of python bindings improvements, added test
- fixed 3 bugs

* Wed Jan 26 2005 Daniel Veillard <veillard@redhat.com> 0.0.21-1
- Added Python support
- Updated for inotify-0.18 

* Thu Jan  6 2005 Daniel Veillard <veillard@redhat.com> 0.0.20-1
- Frederic Crozat seems to have found the GList corruption which may fix
  #132354 and related problems
- Frederic Crozat also fixed poll only mode

* Fri Dec  3 2004 Daniel Veillard <veillard@redhat.com> 0.0.19-1
- still chasing the loop bug, made another pass at checking GList,
  added own copy with memory poisonning of GList implementation.
- fixed a compile issue when compiling without debug

* Fri Nov 26 2004 Daniel Veillard <veillard@redhat.com> 0.0.18-1
- still chasing the loop bug, checked and cleaned up all GList use
- patch from markmc to minimize load on busy apps

* Wed Oct 20 2004 Daniel Veillard <veillard@redhat.com> 0.0.16-1
- chasing #132354, lot of debugging, checking and testing and a bit
  of refactoring

* Sat Oct 16 2004 Daniel Veillard <veillard@redhat.com> 0.0.15-1
- workaround to detect loops and avoid the nasty effects, see RedHat bug #132354

* Sun Oct  3 2004 Daniel Veillard <veillard@redhat.com> 0.0.14-1
- Found and fixed the annoying bug where update were not received
  should fix bugs ##132429, #133665 and #134413
- new mechanism to debug on-the-fly by sending SIGUSR2 to client or server
- Added documentation about internals

* Fri Oct  1 2004 Daniel Veillard <veillard@redhat.com> 0.0.13-1
- applied portability fixes
- hardened the code while chasing a segfault

* Thu Sep 30 2004 Daniel Veillard <veillard@redhat.com> 0.0.12-1
- potential fix for a hard to reproduce looping problem.

* Mon Sep 27 2004 Daniel Veillard <veillard@redhat.com> 0.0.11-1
- update to the latest version of inotify
- inotify support compiled in by default
- fix ABI FAM compatibility problems #133162 

* Tue Sep 21 2004 Daniel Veillard <veillard@redhat.com> 0.0.10-1
- more documentation
- Added support for a configuration file $HOME/.gaminrc
- fixes FAM compatibility issues with FAMErrno and FamErrlist #132944

* Wed Sep  1 2004 Daniel Veillard <veillard@redhat.com> 0.0.9-1
- fix crash with konqueror #130967
- exclude kernel (dnotify) monitoring for /mnt//* /media//*

* Thu Aug 26 2004 Daniel Veillard <veillard@redhat.com> 0.0.8-1
- Fixes crashes of the gam_server
- try to correct the kernel/poll switching mode

* Tue Aug 24 2004 Daniel Veillard <veillard@redhat.com> 0.0.7-1
- add support for both polling and dnotify simultaneously
- fixes monitoring of initially missing files
- load control on very busy resources #124361, desactivating
  dnotify and falling back to polling for CPU drain

* Thu Aug 19 2004 Daniel Veillard <veillard@redhat.com> 0.0.6-1
- fixes simple file monitoring should close RH #129974
- relocate gam_server in $(libexec)

* Thu Aug  5 2004 Daniel Veillard <veillard@redhat.com> 0.0.5-1
- Fix a crash when the client binary forks the gam_server and an
  atexit handler is run.

* Wed Aug  4 2004 Daniel Veillard <veillard@redhat.com> 0.0.4-1
- should fix KDE build problems
