#!/usr/bin/python3
class House:
	houses_history = []
	Err_NoExist="Такого этажа не существует"
	def __new__(cls,*args,**kwargs):
		cls.houses_history.append(args[0])
		return object.__new__(cls)
	def __init__(self,name,number_of_floors):
		self.name=name
		self.number_of_floors=number_of_floors
	def __del__(self):
		print(self.name+" снесён, но он останется в истории")
	def __eq__(self, other):
		return self.number_of_floors==other.number_of_floors
	def __lt__(self, other):
		return self.number_of_floors<other.number_of_floors
	def __le__(self, other):
		return self.number_of_floors<=other.number_of_floors
	def __gt__(self, other):
		return self.number_of_floors>other.number_of_floors
	def __ge__(self, other):
		return self.number_of_floors>=other.number_of_floors
	def __ne__(self, other):
		return self.number_of_floors!=other.number_of_floors
	def __add__(self,value):
		self.number_of_floors+=value
		return self
	def __radd__(self,value):
		return self+value
	def __iadd__(self,value):
		return self+value
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
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

