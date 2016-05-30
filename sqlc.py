import sqlite3 
with sqlite3.connect("new.db") as connection: 
	c = connection.cursor() 
	c.execute("INSERT INTO population VALUES('Washington DC', 'DC', 7879546)") 
	c.execute("INSERT INTO population VALUES('Boston', 'MA', 500000)")

