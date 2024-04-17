#import streamlit as st
import sqlite3 as sql
from PIL import Image
import pandas as pd
import csv

def create_books_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS "books" (
    	"bookID"	INTEGER,
    	"title"	TEXT,
    	"authors"	TEXT,
    	"average_rating"	REAL,
    	"isbn"	TEXT,
    	"isbn13"	REAL,
    	"language_code"	TEXT,
    	"num_pages"	INTEGER,
    	"ratings_count"	INTEGER,
    	"text_reviews_count"	INTEGER,
    	"publication_date"	DATE,
    	"publisher"	TEXT,
    	PRIMARY KEY("isbn13"),
    	UNIQUE("bookID","isbn","isbn13")
    )''')
    conn.commit()
    print('Customer Table create Successfully')
    
def insert_books(conn,csvfilepath):
    try:
        cursor = conn.cursor()
        with open(csvfilepath, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row if exists
            for row in csv_reader:
                try:
                    cursor.execute('''INSERT INTO books (bookID, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count, publication_date, publisher) 
                                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', row)
                    print('Entered :',row)
                except:
                    print('Unclean Data')
        conn.commit()
        print("Data inserted successfully")
    except sql.Error as e:
        print(e)
    
def setup():
    database = "library.db"
    books_csv_file = "books.csv"

    # Create a connection to the database
    conn = sql.connect("library.db",check_same_thread=False)
     
    if conn is not None:
        
        create_books_table(conn)

        # Insert data from CSV file
        #insert_books(conn,books_csv_file)

        # Close the connection
        return conn
    else:
        print("Error! Cannot create the database connection.")
        
def connect():
    database = "library.db"
    conn = sql.connect("library.db",check_same_thread=False)
    return conn