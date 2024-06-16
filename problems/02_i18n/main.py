#!/usr/bin/python3
import gettext
from gettext import gettext as _

gettext.bindtextdomain('main','./locales')
gettext.textdomain('main')

print([_('Hello!'),_('My name is %s' % (_('testuser')))])

