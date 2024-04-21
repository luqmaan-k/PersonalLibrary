import time
from typing import Dict
import streamlit as st
from hydralit import HydraHeadApp

import sqlite3 as sql
from PIL import Image
import pandas as pd
import csv

def getreading():
    database = "library.db"
    books_csv_file = "books.csv"

    # Create a connection to the database
    conn = sql.connect("library.db",check_same_thread=False)
     
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('SELECT "Image-URL-L",title,average_rating FROM booksdata INNER JOIN bookswithimage ON bookswithimage.ISBN = booksdata.isbn WHERE ratings_count > 1000 ORDER BY average_rating DESC LIMIT 10')
        book_data = cursor.fetchall()
        conn.close()
        return book_data

        # Insert data from CSV file
        #insert_books(conn,books_csv_file)

        # Close the connection
        
    else:
        print("Error! Cannot create the database connection.")
        return None
    
def getCompleted():
    database = "library.db"
    books_csv_file = "books.csv"

    # Create a connection to the database
    conn = sql.connect("library.db",check_same_thread=False)
     
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('SELECT "Image-URL-L",title,average_rating FROM booksdata INNER JOIN bookswithimage ON bookswithimage.ISBN = booksdata.isbn WHERE ratings_count > 1000 ORDER BY average_rating DESC LIMIT 10')
        book_data = cursor.fetchall()
        conn.close()
        return book_data

        # Insert data from CSV file
        #insert_books(conn,books_csv_file)

        # Close the connection
        
    else:
        print("Error! Cannot create the database connection.")
        return None
        
def getPlanning():
    database = "library.db"
    books_csv_file = "books.csv"

    # Create a connection to the database
    conn = sql.connect("library.db",check_same_thread=False)
     
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('SELECT "Image-URL-L",title,average_rating FROM booksdata INNER JOIN bookswithimage ON bookswithimage.ISBN = booksdata.isbn WHERE ratings_count > 1000 ORDER BY average_rating DESC LIMIT 10')
        book_data = cursor.fetchall()
        conn.close()
        return book_data

        # Insert data from CSV file
        #insert_books(conn,books_csv_file)

        # Close the connection
        
    else:
        print("Error! Cannot create the database connection.")
        return None
        
def path_to_image_html(path):
    return '<img src="' + path + '" width="100" height="100">'

@st.cache_data
def convert_df(input_df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return input_df.to_html(escape=False, formatters=dict(Cover=path_to_image_html))

class UserApp(HydraHeadApp):

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title


    def run(self) -> None:
        """
        Application entry point.
        """

        st.write("# Welcome to your Personal Library 📚")
        bookdata = getCompleted()
        book_clean_df = pd.DataFrame(bookdata, columns=["Cover", "Title", "Rating"])
        
        # st.markdown(book_clean_df.to_html(escape=False), unsafe_allow_html=True)

        book_clean_df.index += 1
        html = convert_df(book_clean_df)

        # st.column_config.ImageColumn(label=None, *, width=None, help=None)
        print(book_clean_df)


        st.markdown(
            html,
            unsafe_allow_html=True
        )
        
        print(html)