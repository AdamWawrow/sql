#import the library
import sqlite3

#Prompt the user whether he or she would like to perform an aggregation 
#(AVG, MAX, MIN, or SUM) or exit the program altogether.

prompt = raw_input('AVG, MAX, MIN, or SUM? ')
print(prompt)

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    if prompt == 'a':
    	c.execute("SELECT avg(num) FROM numbers")
    	r = c.fetchone()
    	print r[0]

    elif prompt == "b":
    	c.execute("SELECT max(num) FROM numbers")
    	r = c.fetchone()
    	print r[0]

    elif prompt == "c":
    	c.execute("SELECT min(num) FROM numbers")
    	r = c.fetchone()
    	print r[0]

    elif prompt == "d":
    	c.execute("SELECT sum(num) FROM numbers")
    	r = c.fetchone()
    	print r[0]