#!/usr/bin/env python
import subprocess,sys,struct,os,time,shutil
from random import *
if len(sys.argv) < 6:
	sys.exit( 'Usage : [Ref file] [Size read] [Error rate] [output file] [Number of read]' )

debut=time.time()

#~ refFile=sys.argv[1]
sizeRead=int(sys.argv[2])
errorRate=int(sys.argv[3])
outputFile=sys.argv[4]
nRead=int(sys.argv[5])

out = open(outputFile, 'w')
out.truncate()


def randNuc(nuc):
	rand=randint(0,4)
	if(rand==0 and nuc!='A'):
		return 'A'
	if(rand==1 and nuc!='C'):
		return 'C'
	if(rand==2 and nuc!='G'):
		return 'G'
	if(rand==3 and nuc!='T'):
		return 'T'
	return randNuc(nuc)


with open(sys.argv[1]) as refFile:
	useless = refFile.readline()
	ref = refFile.readline()
	for num in range(0,nRead):
		position=(randint(0,len(ref)-sizeRead))
		#~ print (position)
		readRef=ref[position:position+sizeRead]
		#~ print(readRef)
		#~ wait = input("PRESS ENTER TO CONTINUE.")
		#~ readRef.upper()
		#~ readErr=readRef
		#~ readRef=">"+readRef
		i=0
		#~ for c in readErr:
			#~ i+=1
			#~ if(randint(0,errorRate)==0):
				#~ readErr=readErr[:i]+randNuc(c)+readErr[i+1:]
		#~ out.write(readRef)
		out.write(">lol\n")
		out.write(readRef)
		out.write("\n")
