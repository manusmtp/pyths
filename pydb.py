import sqlite3

db=sqlite3.connect('student.db')

try:
	cur=db.cursor()
	cur.execute("select * from student")
	while True:
		record=cur.fetchone()
		if record:
			print("record exist")
			print(record)
			break
except:
	print("error1")
db.close()


def inser(dbobj):
	#dbobj to manipulate the db 
	#dbobj=sqlite3.connect('student.db')
	try:
		cur=dbobj.cursor()
		cur.execute("insert into student(name,age,marks) values ('manu',33,87);")
		dbobj.commit()
	except:
		print("there is some error in manipulating the db")
	dbobj.close()

db=sqlite3.connect('student.db')
inser(db)


