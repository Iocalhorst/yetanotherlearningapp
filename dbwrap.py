import sqlite3


def setup(settings):
	if settings.get("dbname")=="sqlite":
			try :
				connection==sqlite3(settings("filename"))
				return connection,None
			except :
				return None,"file not found"


def create_table(name,params,connection):

	command="CREATE TABLE "+name+" " "+params

	cur.execute(command)





