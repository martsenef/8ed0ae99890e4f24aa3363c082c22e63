#!/usr/bin/python3
def custom_write(file_name, strings,encoding='utf-8'):
	with open(file_name,'w') as file:
		result={}
		for index,string in enumerate(strings):
			result[index+1,file.tell()]=string
			file.write(string+'\n')
		return result
			
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
