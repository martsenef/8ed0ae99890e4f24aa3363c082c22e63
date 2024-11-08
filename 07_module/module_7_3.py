#!/usr/bin/python3
import re

def uopen(file_name,mode):
	return open(file_name,mode,encoding='utf-8')
class WordsFinder:
	def __init__(self,*file_names):
		self.file_names=list(file_names)
	def get_all_words(self):
		all_words={}
		for f in self.file_names:
			all_words[f]=[]
			with uopen(f,'r') as ff:
				for l in ff.read().lower().splitlines():
					for w in re.sub(r'[,.=!?;:]', '',l.lower().replace(' - ',' ')).split(' '):
						if w!='':
							all_words[f].append(w)
		return all_words
	def find(self, word):
		result={}
		all_words=self.get_all_words()
		word=word.lower()
		for f,w in all_words.items():
			try:
				result[f]=w.index(word)+1
			except ValueError:
				continue
		return result
	def count(self, word):
		result={}
		all_words=self.get_all_words()
		word=word.lower()
		for f,w in all_words.items():
			result[f]=w.count(word)
		return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

