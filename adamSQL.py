#Create SQLite3 database and table

#import the library
import sqlite3
import csv

#create database if one does not exist

with sqlite3.connect("adam.db") as connection:
    c = connection.cursor()

    # open the csv file and assign it to a variable
    cars = csv.reader(open("adamcsv.csv", "rU"))

    # create a new table called employees
    #c.execute("CREATE TABLE inventory(type, color, quantity)")

    # insert data into table
    #c.executemany("INSERT INTO inventory(type, color, quantity) values (?, ?, ?)", cars)

    # update data 

    #c.execute("UPDATE inventory SET quantity = 2378 WHERE type ='Tesla'")

    # delete data 

    #c.execute("DELETE FROM inventory WHERE type ='Honda'") 
    #print "\nNEW DATA:\n" 

    #c.execute("SELECT * FROM inventory") 

    #rows = c.fetchall() 

    #for r in rows: 
    #    print r[0], r[1], r[2]

    c.execute("SELECT * FROM inventory WHERE type ='Mustang'")
    
    rows = c.fetchall()

    for r in rows: 
        print r[0], r[1], r[2]