import sqlite3

import psycopg2


db_config = "dbname='todoapp' user='postgres' password='Ashleydsouz1@' host='localhost' port='5432'"

def create_new_db(dbname):
    """Sets up tables for new database"""
    con = psycopg2.connect(db_config)
    if con:
        print(" Database is Connected")
    else:
        print("not connected")

    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
    userid SERIAL,
    username character varying(100) NOT NULL,
    PRIMARY KEY(userid),
    password character(40) NOT NULL,
    confirm_password character(40) NOT NULL);""")

    #create project table
    cursor.execute("""CREATE TABLE IF NOT EXISTS Projects(
            ProjectID SERIAL,
            Description text,
            Duedate date,
            Created timestamp,
            Completed timestamp,
            userid integer,
            PRIMARY KEY(ProjectID),
            FOREIGN KEY(userid) REFERENCES Users(userid));""")

        #create tasks table
    cursor.execute("""CREATE TABLE IF NOT EXISTS Tasks(
            TaskID SERIAL,
            Description text,
            Duedate date,
            Created timestamp,
            Completed timestamp,
            ProjectID integer,
            userid integer,
            PRIMARY KEY(TaskID),
            FOREIGN KEY(ProjectID) REFERENCES Projects(ProjectID),
            FOREIGN KEY(userid) REFERENCES Users(userid));""")


        

        
    con.commit()





