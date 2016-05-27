#Create SQLite3 database and table

#import the library
import sqlite3

#create database if one does not exist

conn = sqlite3.connect("new.db")

#get a cursor object used to execute sql statements

cursor = conn.cursor()

#create a table

cursor.execute("""CREATE TABLE population
				(city TEXT, state TEXT, population INT)
				""")

#close database connection
conn.close()

