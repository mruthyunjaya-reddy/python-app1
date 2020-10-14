'''
a=open("abc.txt",'w')
print("File Name:",a.name)
print("File Mode:",a.mode)
print("File readable:",a.readable())
print("File writable:",a.writable())
print("File Closed:",a.closed)
a.close()
print("File Closed:",a.closed)
print("file is closed")
'''
#-----------------------------------------------
'''
f=open("abcd.txt",'w')
f.write("hiii\n")
f.write("muthu\n")
f.write("how r u\n")
f.write("--------------------\n")
f.close()
print("data write into file successfully")
'''
#--------------------------------------------------------
'''
f=open("abcd.txt",'a')
f.write("vinayaka\n")
f.write("hanumantudu\n")
f.write("barbikudu\n")
f.write("---------------------\n")
f.close()
print("data write into file successfully")
'''
#-------------------------------------------------------------
'''
f=open("abcd.txt",'r')
data=f.read()
print(data)
print("read the data from the file successfully")
'''
#-----------------------------------------------------------------
'''
f=open("abcd.txt",'a')
f.write("abhimanudu\n")
f.write("arjunudu\n")
f.write("suryudu\n")
f.write("karnudu\n")
f.write("--------------------\n")
f.close()
print("data write into file successfully")
'''
#--------------------------------------------------------------
'''
f=open("abcd.txt",'r')
data=f.read()
print(data)
print('read data successfully')
'''
#---------------------------------------------------
'''
f=open("abcd.txt",'a')
f.writelines("nmr\n")
f.writelines("nnr\n")
f.writelines("nmsr\n")
f.writelines("----------------------\n")
f.close()
print("write data successfully")
'''
#-------------------------------------------------------
'''
f=open("abcd.txt","a")
list=["sunny\n","bunny\n","chinny\n","binny\n"]
f.writelines(list)
f.writelines("------------------------\n")
print("write data successfully")
'''
#----------------------------------------------------
'''
f=open("abcd.txt","r")
data=f.read()
print(data)
f.close()
print("read data successfully")
'''
#------------------------------------------------------
'''
f=open("abcd.txt","r")
data=f.read(10)
print(data)
f.close()
print("read data successfully")
'''
#-----------------------------------------------
'''
f=open("abcd.txt",'r')
line1=f.readline()
print(line1,end='')
line2=f.readline()
print(line2,end='')
line3=f.readline()
print(line3,end='')
f.close()
print("3 line are printed")
'''
#----------------------------------------------
'''
f=open("abcd.txt",'r')
lines=f.readlines()
for i in lines:
	print(i,end='')
f.close()
'''
#-------------------------------------------
'''
f=open("python.txt",'r')
data=f.read()
print(data)
'''
#--------------------------------------------
'''
with open("abcd.txt",'a') as f:
	f.write("mruthyunjaya")
	f.write("reddy\n")
	f.writelines("where are from\n")
	f.write("iam from lingala\n")
	print("file is close:",f.closed)
print("file is close:",f.closed)
'''
#-----------------------------------------------
'''
f=open("abcd.txt","r")
print(f.tell())
print(f.read(17))
print(f.tell())
print(f.read(30))
print(f.tell())
f.close()
'''
#-----------------------------------------------
'''
a="Mruthyunjayudu means death  "
f=open("abc.txt",'w')
f.write(a)
with open("abc.txt","r+") as f:
	op=f.read()
	print(op)
	print("the current position of cursor:",f.tell())
	f.seek(21)
	print("the current position of cursor:",f.tell())
	f.write("immotal")
	f.seek(0)
	text=f.read()
	print("data after modification")
	print(text)
'''
#-----------------------------------------------
'''
import os,sys
fname=input("enter file name:")
if os.path.isfile(fname):
	print("file exits:",fname)
	f=open(fname,"r")
else:
	print("file dost not exist:",fname)
	sys.exit()
print("the content of file is:")
data=f.read()
print(data)
'''
#---------------------------------------------------
'''
from random import *
#for i in range(1):
data=random()
print(data)
'''
#-----------------------------------------------------
'''
import os,sys
fname=input("enter file name:")
if os.path.isfile(fname):
	print("file exist:",fname)
	f=open(fname,"r")
else:
	print("file does not exist:",fname)
	sys.exit()
lines=words=char=0
for i in f:
	lines+=1
	char=char+len(i)
	w=i.split()
	words=words+len(w)
print("no of lines:",lines)
print("no of characters:",char)
print("no of words:",words)
'''
#-------------------------------------------------------
'''
f1=open("space.jpg","rb")
f2=open("newspace.jpg","wb")
name=f1.read()
f2.write(name)
print("check image")
'''
#----------------------------------------------
'''
import csv
with open("emp.csv","w",newline='') as f:
	w=csv.writer(f)
	w.writerow(["ENO","ENAME","ESAL","EADDR"])
	n=int(input("enter number of emplyoees:"))
	for i in range(n):
		eno=input("emplyoee number:")
		ename=input("emplyoee name:")
		esal=input("emplyoee salary:")
		eaddr=input("emplyoee address:")
		w.writerow([eno,ename,esal,eaddr])    
print("hii csv file write successfully")
'''
#--------------------------------------------------------
'''
import csv
f=open("emp.csv","r")
r=csv.reader(f)
data=list(r)
#print(data)
for i in data:
	for j in i:
		print(j,"\t",end="")
	print()
'''
#----------------------------------------------------------
'''
import os 
data=os.getcwd()
print("current working directory:",data)
'''
#-------------------------------------------------------
'''
import os
os.mkdir("mysub")
print("mysub directory created in cwd:")
'''
#-------------------------------------------------------
'''
import os 
os.mkdir("mysub/mysub1")
print("mysub1 directory created in cwd:")
'''
#-------------------------------------------------
'''
import os
data=os.mkdir("mysub/mysub1/useful-data1")
print("created multiple directories",data)
 '''
 #---------------------------------------------
'''
import os 
data=os.makedirs("nmr/space/moon/moon_potos")
print("multiple dirctories created",data)
'''
#----------------------------------------------------
'''
import os 
os.removedirs("nmr/space")
print("deleted directory")
'''
#--------------------------------------------
'''
import os 
os.rmdir("nmr/space")
print("deleted directory")
'''
#-------------------------------------------
'''
f=open("abcd.txt",'r')
data=f.read()
print(data)
'''
#-----------------------------------
f=open("abcd.txt",'a')
f.write("om navasivaya\n")
f.write("shankharaaaaaaaaaaaa\n")
print("text crated")