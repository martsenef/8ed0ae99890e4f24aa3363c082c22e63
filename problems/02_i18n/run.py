#!/usr/bin/python3
import subprocess

testdata=[
	['C',"['Hello!', 'My name is testuser']"],
	['ru_RU.utf8',"['Здрасьте!', 'Меня зовут тестюзер']"],
	['ja_JP.utf8',"['おはよう！', 'お名前はテストユーゼル']"],
]

for i in testdata:
	for s in ['.sh','.py']:
		str='LANG=%s ./main%s' % (i[0],s)
		res=subprocess.getoutput(str)
		if(i[1]==res):
			print([' OK ', i[0], s])
		else:
			print(['FAIL', i[0], s, res, ' != ', i[1]])

