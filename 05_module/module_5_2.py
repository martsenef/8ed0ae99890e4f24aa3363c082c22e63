#!/usr/bin/python3
class House:
	Err_NoExist="Такого этажа не существует"
	def __init__(self,name,number_of_floors):
		self.name=name
		self.number_of_floors=number_of_floors
	def __len__(self):
		return self.number_of_floors
	def __str__(self):
		return "Название: "+self.name+", кол-во этажей: "+str(self.number_of_floors)
	def go_to(self,new_floor):
		if new_floor<1 or new_floor>self.number_of_floors:
			print(self.Err_NoExist)
			return
		for i in range(new_floor):
			print(i+1)
		return
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

