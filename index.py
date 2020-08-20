import mysql.connector
import datetime
dbpw=input("Enter your MySQL database password for the user root ")
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=dbpw
)
mycursor=db.cursor()
mycursor.execute("create database if not exists movies;")
mycursor.execute("USE MOVIES;")
mycursor.execute("CREATE TABLE if not exists Movies (id int PRIMARY KEY, name varchar(50) NOT NULL,director varchar(30) NOT NULL, language varchar(20) NOT NULL,genre varchar(20) NOT NULL);")
mycursor.execute("CREATE TABLE if not exists Shows (showId int PRIMARY KEY, movieId int NOT NULL,FOREIGN KEY(movieId) REFERENCES MOVIES(id), show_time TIME, seats_left int DEFAULT 50 );")
mycursor.execute("CREATE TABLE if not exists Users (un varchar(20) primary key,password varchar(20) not null);")
mycursor.execute("CREATE TABLE if not exists Bookings (showId int,FOREIGN KEY(showId) REFERENCES Shows(showId),un varchar(20),FOREIGN KEY(un) REFERENCES Users(un), seat_no int);")

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


# Function code

def showMovies():
    mycursor.execute("SELECT * FROM MOVIES;")
    print("Values are in the order of movieId | movieName | Director | Language | Genre")
    for i in mycursor:
        for j in i:
            print(str(j),end="|")
        print()

def showMovieTimings():
    mycursor.execute("SELECT a.showId,b.name,a.show_time, a.seats_left FROM shows as a inner join movies as b on b.id=a.movieId")
    print("Values are in the order of showId | Movie Name | Show timing | Number of Seats left")
    for i in mycursor:
        for j in i:
            print(str(j),end="|")
        print()
def showSelectedMovieTimings():
    global currentMovie 
    currentMovie=input("Please select the movie ID: ")
    mycursor.execute("SELECT a.showId,b.name,a.show_time, a.seats_left FROM shows as a inner join movies as b on b.id=a.movieId and a.movieId=%s;"%currentMovie )
    print("Values are in the order of showId | Movie Name | Show timing | Number of Seats left")
    for i in mycursor:
        for j in i:
            print(str(j),end="|")
        print()

def signUp():
    global un
    global pw
    while True:
        un=input("Enter username: ")
        pw=input("Enter password: ")
        try:
            mycursor.execute("Insert INTO Users VALUES (%s,%s)",(un,pw))
            db.commit()
            break
        except:
            print("Your username is taken")
    

def logIn():
    global un
    global pw
    
    while True:
        un=input("Enter username: ")
        mycursor.execute("SELECT un from users where un='%s';"%un)
        if (int(len(list(mycursor)))>0):
            print("username verified")
            break
        else:
            print("that username wasn't found")
    
    while True:    
        pw=input("Enter password: ")
        mycursor.execute("SELECT password from users where un='%s';"%un )
        if mycursor.fetchone()[0]==pw:
            print("Password verified")
            break
        else:
            print("Password Failed")


def bookShow():
    global currentShow
    currentShow=int(input("Enter your show's id "))
    n=int(input("Please enter the number of tickets you want "))
    for i in range(n):
        mycursor.execute("SELECT seats_left from shows where showId=%s;"%currentShow)
        seats_left=mycursor.fetchone()[0]
        mycursor.execute("INSERT INTO BOOKINGS VALUES(%s,%s,%s);",(currentShow,un,seats_left))
        db.commit()
        mycursor.execute("Update shows set seats_left=(seats_left-1) where showId=%s;"%currentShow)
        db.commit()
       

def showBookings():
    mycursor.execute("SELECT showId,seat_no from bookings where un='%s';"%un)
    print("Values are in the order of showId | Your Seat Number")
    for i in mycursor:
        for j in i:
            print(str(j),end="|")
        print()

while True:
    print("""
    1. Login
    2. Sign Up
    """)
    n=int(input("Please select option number from above "))
    if n==1:
        logIn()
        break
    elif n==2:
        signUp()
        break
    else:
        print('Write "1" or "2". No other number is accpeted')

while True:
    print("""
    1. Show all movies
    2. Show all movie timings
    3. Show selected movie timings
    4. Book a show (You should know your show's showId)
    5. Show all of your Bookings
    6. Exit
    """)
    x=int(input())
    if x==1:
        showMovies()
    elif x==2:
        showMovieTimings()
    elif x==3:
        showSelectedMovieTimings()
    elif x==4:
        bookShow()
        print("Here are all the shows you have booked")
        showBookings()
    elif x==5:
        showBookings()
    elif x==6:
        break  
    else:
        print("Please enter a correct number.")





