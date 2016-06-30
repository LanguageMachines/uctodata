SUBDIRS = config

EXTRA_DIST = bootstrap.sh AUTHORS TODO NEWS uctodata.pc.in

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = uctodata.pc

ChangeLog: $(top_srcdir)/NEWS
	git pull; git2cl > ChangeLog
