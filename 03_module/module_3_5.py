#!/usr/bin/python3
from _test import test_display

def get_multiplied_digits_helper(number:int):
	str_number=str(number)
	if len(str_number)==1:
		return number
	first=int(str_number[0])
	last=int(str_number[1:])
	return (first*get_multiplied_digits_helper(last) if last !=0 else first)
	
def get_multiplied_digits(number:int):
	if number<0:
		number=-number
	return get_multiplied_digits_helper(number)

testdata=[
	[0,get_multiplied_digits,[0] ],
	[6,get_multiplied_digits,[-23] ],
	[6,get_multiplied_digits,[321] ],
	[8,get_multiplied_digits,[1024] ],
	[8,get_multiplied_digits,[4200] ],
	[24,get_multiplied_digits,[40203] ],
	[24,get_multiplied_digits,[402030] ],
]
test_display(testdata)
