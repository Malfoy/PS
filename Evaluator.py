#!/usr/bin/env python
import subprocess,sys,struct,os,time,shutil,random

if len(sys.argv) < 2:
	sys.exit( 'Usage : [Corrected read file] ' )

debut=time.time()

readFile=sys.argv[1]
readNumber=0
list=[0,0,0,0,0,0,0,0,0,0]
with open(readFile) as f:
	while True:
		refSeq = f.readline()
		corSeq = f.readline()
		readNumber+=1
		if not refSeq: break
		refSeq=refSeq[1:]
		error=0
		for i in range(0,99):
			if(refSeq[i]!=corSeq[i]):
				error+=1
		list[error]+=1
count=0
print(str(readNumber)+" reads")
for e in list:
	print(str(count)+": "+str(float(10000*e/readNumber)/100)+"%")
	count+=1
