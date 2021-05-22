from settings import *
from dbwrap import *



def connect():
	connection,error=setup(default)
	return connection,error
	


def main():

	connection,error=connect()
	if error=="file not found":
		file=open(default.get("filename"),"w")
		file.close()
		connection,error=connect()

	statements:

	insert_col(col)
	create_table("statements")

main()