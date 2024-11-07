#!/usr/bin/python3
class Vehicle:
	__COLOR_VARIANTS=['blue', 'red', 'green', 'black', 'white']
	def __init__(self,owner,model,color,power):
		self.owner=owner
		self.__model=model
		self.__color=color
		self.__engine_power=power
	def get_model(self):
		print("Модель: %s" % self.__model)
	def get_horsepower(self):
		print("Мощность двигателя: %s" % self.__engine_power)
	def get_color(self):
		print("Цвет: %s" % self.__color)
	def print_info(self):
		self.get_model()
		self.get_horsepower()
		self.get_color()
		print("Владелец: %s" % self.owner)
	def set_color(self,color):
		if color.lower() in self.__COLOR_VARIANTS:
			self.__color=color
		else:
			print("Нельзя сменить цвет на %s" % color)
class Sedan(Vehicle):
	__PASSENGERS_LIMIT = 5
	def __init__(self,owner,model,color,power):
		super().__init__(owner,model,color,power)

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
