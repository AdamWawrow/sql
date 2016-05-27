#Create SQLite3 database and table

#import the library
import sqlite3

#create database if one does not exist

conn = sqlite3.connect("cars.db")

#get a cursor object used to execute sql statements

cursor = conn.cursor()

#create a table

#cursor.execute("""CREATE TABLE cars
#				(Make TEXT, Model TEXT, Quantity INT)
#				""")

cursor.execute("""DROP TABLE population""")

#close database connection
conn.close()