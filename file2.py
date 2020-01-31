import os
from pathlib import Path


def reading(file_name):
	try:
		 fh=open(str(Path.cwd())+'/'+file_name+'.txt','r')	
		 contents=fh.read()   
		 print("the contents of the file are as follows") 
		 print("---------------------------------------") 
		 print(contents)
		 fh.close()
	except FileNotFoundError as e:
		 print("Entered file name does not exist")

def writing(file_name):
	try:
		fh=open(str(Path.cwd())+'/'+file_name+'.txt','w')
		contents=input("Enter the contents to write")
		fh.write(contents)
		fh.close()
	except FileNotFoundError as e:
	    print("re-run and try with proper file name")


if __name__ == '__main__':
	
	file_name=input("enter the name of file:: ")  
	print("1.Reading")  
	print("2.Writing")  
	option=int(input("enter any below option"))   
	if option == 1: 
	       reading(file_name)
	if option == 2:
		   writing(file_name)
    