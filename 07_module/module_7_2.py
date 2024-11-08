#!/usr/bin/python3
def uopen(file_name,mode):
	return open(file_name,mode,encoding='utf-8')
def custom_write(file_name, strings):
	with uopen(file_name,'w') as f:
		res={}
		for i,s in enumerate(strings):
			res[i+1,f.tell()]=s
			f.write(s+'\n')
		return res
			
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

