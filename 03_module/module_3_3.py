#!/usr/bin/python3

'''
Данная функция принимает список тестов.
Каждый тест описывается списком из трёх параметров:
1) ожидаемый результат
2) тестируемая функция
3) параметры, передаваемые в функцию.
Если передан список или словарь, то он будет распакован.
В случае возникнования ошибки, результатом будет exception
'''
def test_display(testlist):
	for test in testlist:
		try:
			if(list==type(test[2])):
				res=test[1](*test[2])
			elif(dict==type(test[2])):
				res=test[1](**test[2])
			else:
				res=test[1](test[2])
		except Exception as e:
			print(e)
			res=type(e)
		if(res!=test[0]):
			print("Error: ", test[1], test[2],":",res,"!=",test[0])
		else:
			print(res)
'''
В этой функции print заменён на return,
чтобы тест мог сравнить ожидаемый результат с фактическим.
Результат будет выведен в самом тесте.
Вызовы с разным числом параметров, в том числе и без них, работют,
также работают вызовы с b=25 и c=[1,2,3]
'''
def print_params(a = 1, b = 'строка', c = True):
	return(a,b,c)
'''
Функция к заданию 2.3.
Осуществляет распаковку списка и словаря и передаёт их в print_params
TypeError возникает, если в словаре присутствует любой из параметров уже был задан в списке.
'''
def l23(list,dict):
	return print_params(*list,**dict)
'''
Функция к заданию 3.2.
Осуществляет распаковку списка и добавляет отдельный параметр, работает нормально.
'''
def l32v(l,v):
	return print_params(*l,v)
	
values_list=[1,'текст',[None]]
values_dict ={'a':{'a'},'b':['b'],'c':'c'}

testdata=[
#1
	[(1,'строка',True),print_params,[] ],
	[(1,'строка',True),print_params,[1] ],
	[(1,'два',True),print_params,[1,'два'] ],
	[(1,'два',[3]),print_params,[1,'два',[3]] ],
	[(1,25,True),print_params,{'b':25} ],
	[(1,'строка',[1,2,3]),print_params,{'c':[1,2,3]} ],
#2.1
	[(1,'текст',None),print_params,[1,'текст',None] ],
	[(False,[{},{0}],print),print_params,[False,[{},{0}],print] ],
	[('Нет',-1,(2,3)),print_params,['Нет',-1,(2,3)] ],
#2.2
	[(1,'текст',None),print_params,{'a':1,'b':'текст','c':None} ],
	[(False,[{},{0}],print),print_params,{'b':[{},{0}],'a':False,'c':print} ],
	[('Нет',-1,(2,3)),print_params,{'c':(2,3),'b':-1,'a':'Нет'} ],
#2.3
	[TypeError,l23,[values_list,values_dict] ],
	[([1],{'b'},{'c'}),l23,[[[1]],{'b':{'b'},'c':{'c'}}] ],
	[([1],'строка',{'c'}),l23,[[[1]],{'c':{'c'}}] ],
	[TypeError,l23,[[[1],[2]],{'b':{'b'},'c':{'c'}}] ],
	[([1],[2],{'c'}),l23,[[[1],[2]],{'c':{'c'}}] ],
#3.2
	[([1],[2],42),l32v,[[[1],[2]],42] ]
]
test_display(testdata)
