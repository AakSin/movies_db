import mysql.connector
import datetime
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    
)
mycursor=db.cursor()
mycursor.execute("create database if not exists movies;")
mycursor.execute("USE MOVIES;")
mycursor.execute("CREATE TABLE if not exists Movies (id int PRIMARY KEY, name varchar(50) NOT NULL,director varchar(30) NOT NULL, language varchar(20) NOT NULL,genre varchar(20) NOT NULL);")
mycursor.execute("CREATE TABLE if not exists Shows (showId int PRIMARY KEY, movieId int NOT NULL,FOREIGN KEY(movieId) REFERENCES MOVIES(id), show_time TIME, seats_left int DEFAULT 50 );")

# # Data entry for the movies
# mycursor.execute("Insert INTO MOVIES VALUES (%s,%s,%s,%s,%s)",(1,"The Grand Budapest Hotel","Wes Anderson","English","Comedy"))
# mycursor.execute("Insert INTO MOVIES VALUES (%s,%s,%s,%s,%s)",(2,"Don 2","Farhan Akhtar","Hindi","Thriller"))
# mycursor.execute("Insert INTO MOVIES VALUES (%s,%s,%s,%s,%s)",(3,"Spirited Away","Hayao Miyazaki","Japanese","Drama"))
# mycursor.execute("Insert INTO MOVIES VALUES (%s,%s,%s,%s,%s)",(4,"Newton","Amit V. Masurkar","Hindi","Comedy"))
# mycursor.execute("Insert INTO MOVIES VALUES (%s,%s,%s,%s,%s)",(5,"The Social Network","David Fincher","English","Drama"))

# #Data entry for the show timings
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(1,1,"08:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(2,1,"12:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(3,1,"16:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(4,2,"9:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(5,2,"13:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(6,2,"17:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(7,3,"10:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(8,3,"14:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(9,3,"18:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(10,4,"11:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(11,4,"15:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(12,4,"19:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(13,5,"20:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(14,5,"00:00"))
# mycursor.execute("Insert INTO Shows(showId,movieId,show_time) VALUES (%s,%s,%s)",(15,5,"04:00"))

def showMovies():
    





db.commit()
mycursor.execute("select * from movies;")
for i in mycursor:
    print(i)

mycursor.execute("select * from shows;")
for i in mycursor:
    for j in i:
        print(str(j),end=" ")
    print()