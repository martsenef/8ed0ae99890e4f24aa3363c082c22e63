#!/usr/bin/python3
import os

for i in [-10,-1,0,1,254,255,256,257,300,1000]:
	res=os.system('./main.py %d' % i)
	if(i%256==res):
		print([' OK ',i])
	else:
		print(['FAIL',i,res,' != ',i%256])

