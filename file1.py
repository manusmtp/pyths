import os
from pathlib import Path

print("home path of the user")
print(Path.home())
print("relative path to full path::",Path.cwd())

if os.path.isdir('dir4'):
	print("directory exist and deleting it")
	os.rmdir('dir4')
else:
	print('dir does not exist')

if os.path.isabs('.'):
	print(" . - this is abosulte")
else:
	print(". is not abosulte path")

#from the docs
print('size of the directory::',os.path.getsize(os.getcwd()))

for i in range(10):
	if os.path.isdir('dir'+str(i)):
	    print("dir exist cleaning dir"+str(i))
	    os.rmdir('dir'+str(i))
	else:
		os.mkdir('dir'+str(i))

