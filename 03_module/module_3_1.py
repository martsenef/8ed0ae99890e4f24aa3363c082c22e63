#!/usr/bin/python
from _test import test_display

calls=0
def count_calls():
	global calls
	calls+=1
def get_calls():
	global calls
	return calls
def string_info(string:str)->tuple:
	count_calls()
	return (len(string),string.upper(),string.lower())
def is_contains(string:str,list_to_search:list)->bool:
	count_calls()
	string=string.lower()
	return any(map(lambda e: string in e.lower(),list_to_search))
testdata=[
	[(8,'CAPYBARA','capybara'),string_info,['Capybara']],
	[(10,'ARMAGEDDON','armageddon'),string_info,['Armageddon']],
	[True,is_contains,['Urban', ['ban', 'BaNaN', 'urBAN']]],
	[False,is_contains,['cycle', ['recycling', 'cyclic']]],
	[4,get_calls,[]],
]
test_display(testdata)
