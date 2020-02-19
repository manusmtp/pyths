import sqlalchemy as db

engine=db.create_engine("sqlite:///student.db")
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('student',metadata,autoload=True,autoload_with=engine)


print("printing the columns")
print(census.columns.keys())
#print(repr(metadata.tables['student']))
print()
query=db.select([census])
result=connection.execute(query)
print(result.fetchall())


