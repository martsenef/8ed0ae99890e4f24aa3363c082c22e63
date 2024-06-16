langs=ru_RU.utf8 ja_JP.utf8

all: $(patsubst %,locales/%/LC_MESSAGES/main.mo,$(langs))

locales/main.pot: main.py main.sh locales
	xgettext --keyword=_ -o $@ $<

%.po: locales/main.pot
	mkdir -p $$(dirname $@)
	msgmerge --update $@ $<

%.mo: %.po
	msgfmt --output-file $@ $<

locales:
	mkdir locales
