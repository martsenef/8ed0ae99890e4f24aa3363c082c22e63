#!/usr/bin/python
from functools import reduce
from _test import test_display

def len_Int(arg:int)->int:
	return arg
def len_Str(arg:str)->int:
	return len(arg)
def len_List(arg:list)->int:
	return reduce(
	 lambda l,r: l+r,
	 map(
	  lambda x: calculate_structure_sum(x),
	  arg
	 )
	,0)
def len_Tuple(arg:tuple)->int:
	return len_List(list(arg))
def len_Set(arg:set)->int:
	return len_List(list(arg))
def len_Dict(arg:dict)->int:
	return len_List(list(arg.keys())+list(arg.values()))
len_types={dict,list,tuple,set,str,int}
def get_type(arg):
	for type in len_types:
		if isinstance(arg,type):
			return type
len_helper={int:len_Int,str:len_Str,list:len_List,dict:len_Dict,tuple:len_Tuple,set:len_Set}
#req=0
def calculate_structure_sum(arg):
#	global req
#	print("  "*req,get_type(arg),arg)
#	req+=1
	res=len_helper[get_type(arg)](arg) if get_type(arg) in len_helper else 0
#	req-=1
#	print("  "*req,res)
	return res

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
testdata=[
	[99,calculate_structure_sum,[data_structure] ],
]
test_display(testdata)
