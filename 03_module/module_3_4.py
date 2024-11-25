#!/usr/bin/python3
from _test import test_display
from functools import reduce

def single_root_words(root_word,*other_words):
	root_word=root_word.lower()
	return reduce(
	 lambda l,r: l+[r[1]],(
	  filter(
	   lambda e: root_word in e[0] or e[0] in root_word,
	   (map(lambda e: (e.lower(),e),other_words))
	  )
	 ),
	[])
testdata=[
	[['richiest', 'orichalcum', 'richies'],single_root_words,['rich', 'richiest', 'orichalcum', 'cheers', 'richies'] ],
	[['Able', 'Disable'],single_root_words,['Disablement', 'Able', 'Mable', 'Disable', 'Bagel'] ],
]
test_display(testdata)
