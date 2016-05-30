#Create SQLite3 database and table

#import the library
import sqlite3
from random import randint

#create database if one does not exist

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE numbers(num int)")

    for i in range(100): 
		c.execute("INSERT INTO numbers VALUES(?)",(randint(0,100),))
