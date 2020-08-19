import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    
)

mycursor=db.cursor()
mycursor.execute("create database if not exists movies;")
mycursor.execute("USE MOVIES;")
mycursor.execute("CREATE TABLE Movies (id int PRIMARY KEY, name varchar(50),director varchar(30), language varchar(20),genre varchar(20));")
