#!/usr/bin/python3

class Product:
	def __init__(self,name,weight,category):
		self.name=name
		self.weight=weight
		self.category=category
	def __str__(self):
		return ', '.join(map(str,[self.name,self.weight,self.category]))
class Shop:
	__file_name='products.txt'
	def get_products(self):
		try:
			with open(self.__file_name,mode='r') as f:
				return f.read()
		except FileNotFoundError as e:
			return ''
	def add(self,*products):
		exist_products=list(map(lambda x: x.split(', ')[0],self.get_products().splitlines()))
		for p in products:
			if p.name in exist_products:
				print('Продукт "%s" уже есть в магазине' % p.name)
			else:
				with open(self.__file_name,mode='a') as f:
					f.write(str(p)+'\n')
				exist_products.append(p.name)

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

