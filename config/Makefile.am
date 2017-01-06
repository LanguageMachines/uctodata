config_DATA = tokconfig-eng tokconfig-nld tokconfig-fra tokconfig-ita \
	tokconfig-spa tokconfig-por tokconfig-deu tokconfig-swe \
	tokconfig-nld-twitter tokconfig-nld-sonarchat tokconfig-tur \
	tokconfig-nld-withplaceholder tokconfig-fry tokconfig-rus \
	tokconfig-generic ligatures.filter \
	exotic-quotes.quote exotic-eos.eos \
	nld_afk.abr spa.abr por.abr

configdir = $(sysconfdir)/ucto

EXTRA_DIST = $(config_DATA)

install-data-hook:
# for backward compatability add symlinks with 'historical' names
	cd $(DESTDIR)$(configdir) && \
	$(LN_S) -f tokconfig-eng tokconfig-en && \
	$(LN_S) -f tokconfig-deu tokconfig-de && \
	$(LN_S) -f tokconfig-nld tokconfig-nl && \
	$(LN_S) -f tokconfig-fra tokconfig-fr && \
	$(LN_S) -f tokconfig-spa tokconfig-es && \
	$(LN_S) -f tokconfig-ita tokconfig-it && \
	$(LN_S) -f tokconfig-por tokconfig-pt && \
	$(LN_S) -f tokconfig-swe tokconfig-sv && \
	$(LN_S) -f tokconfig-rus tokconfig-ru && \
	$(LN_S) -f tokconfig-tur tokconfig-tr && \
	$(LN_S) -f tokconfig-fry tokconfig-fy && \
	$(LN_S) -f tokconfig-nld-twitter tokconfig-nl-twitter && \
	$(LN_S) -f tokconfig-nld-sonarchat tokconfig-nl-sonarchat && \
	$(LN_S) -f tokconfig-nld-withplaceholder tokconfig-nl-withplaceholder && \
	$(LN_S) -f nld_afk.abr nl_afk.abr && \
	$(LN_S) -f spa.abr es.abr && \
	$(LN_S) -f por.abr pt.abr
