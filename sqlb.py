#Create SQLite3 database and table

#import the library
import sqlite3

#create database if one does not exist

conn = sqlite3.connect("new.db")

#get a cursor object used to execute sql statements

cursor = conn.cursor()

#create a table

cursor.execute("INSERT INTO population VALUES ('New York City', 'NY', 820000)")
cursor.execute("INSERT INTO population VALUES ('San Francisco', 'CA', 800000)")

conn.commit()

#close database connection
conn.close()