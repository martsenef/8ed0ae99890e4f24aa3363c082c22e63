#!/usr/bin/python3

import math

class Figure:
	sides_count=0
	def __init__(self,color,*sides):
		self.r,self.g,self.b=color
		self.set_color(self.r,self.g,self.b)
		self.__sides=[1]*self.sides_count
		self.set_sides(*sides)
	def get_color(self):
		return (self.r,self.g,self.b)
	def get_sides(self):
		return self.__sides
	def __is_valid_color(self,r,g,b):
		return all(map(lambda x: 0<=x<=255,[r,g,b]))
	def set_color(self,r,g,b):
		if(self.__is_valid_color(r,g,b)):
			self.r=r
			self.g=g
			self.b=b
	def __is_valid_sides(self,*sides):
		return (len(*sides)==self.sides_count) and all(map(lambda x: x>0,list(*sides)))
	def get_sides(self):
		return self.__sides
	def __len__(self):
		return sum(self.__sides)
	def set_sides(self, *new_sides):
		if self.__is_valid_sides(new_sides):
			self.__sides=new_sides
class Circle(Figure):
	sides_count=1
	def __init__(self,color,*sides):
		super().__init__(color,*sides)
	def get_square(self):
		return self.sides**2/(2*math.pi)
	def set_sides(self, *new_sides):
		super().set_sides(*new_sides)
		self.__radius=self.get_sides()[0]/(2*math.pi)
class Triangle(Figure):
	sides_count=3
	def __init__(self,color,*sides):
		super().__init__(color,*sides)
	def get_square(self):
		p=len(self)
		a,b,c=self.get_sides()
		return math.sqrt(p*(p-a)*(p-b)*(p-c)/2)
class Cube(Figure):
	sides_count=12
	def __init__(self,color,*sides):
		super().__init__(color,*sides)
	def set_sides(self, *new_sides):
		super().set_sides(*(new_sides*12))
	def get_volume(self):
		return self.get_sides()[0]**3

		
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
