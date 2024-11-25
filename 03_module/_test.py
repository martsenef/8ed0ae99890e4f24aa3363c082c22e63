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
