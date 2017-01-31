#!/usr/bin/python
import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# Create table as per requirement
sql = """CREATE TABLE Sense (id int(5) auto_increment, 
ultra_sonic varchar(25) not null defauly,
temperature varchar(25) not null default 'nothing'"""
cursor.execute(sql)
# disconnect from server
db.close()
