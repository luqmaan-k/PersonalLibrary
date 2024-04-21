import os
import streamlit as st
from hydralit import HydraHeadApp

import sqlite3 as sql
from PIL import Image
import pandas as pd
import csv


MENU_LAYOUT = [1,1,1,7,2]

def get_all_books():
    database = "library.db"
    books_csv_file = "books.csv"

    # Create a connection to the database
    conn = sql.connect("library.db",check_same_thread=False)
     
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('SELECT "Image-URL-M",title,average_rating FROM booksdata INNER JOIN bookswithimage ON bookswithimage.ISBN = booksdata.isbn WHERE ratings_count > 1000 ORDER BY average_rating DESC LIMIT 10')
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
    return '<img src="' + path + '" width="200" >'

@st.cache_data
def convert_df(input_df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return input_df.to_html(escape=False, formatters=dict(Cover=path_to_image_html))
                 
class HomeApp(HydraHeadApp):


    def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title


    #This one method that must be implemented in order to be used in a Hydralit application.
    #The application must also inherit from the hydrapp class in order to correctly work within Hydralit.
    def run(self):

        try:
            # st.markdown("<h1 style='text-align:center;padding: 0px 0px;color:black;font-size:200%;'>Home</h1>",unsafe_allow_html=True)     
            # st.markdown("<h2 style='text-align: center;'>This example was written using the <a href = https://github.com/TangleSpace/hydralit>Hydralit</a> library. Sourecode for this example is located <a href = https://github.com/TangleSpace/hydralit-example>here</a>.</h2>",unsafe_allow_html=True)


            st.write("""
                        # Top 10 Books By Rating
                     """)
            #col_header_logo_left_far, col_header_logo_left,col_header_text,col_header_logo_right,col_header_logo_right_far = st.columns([1,2,2,2,1])
            bookdata = get_all_books()
            #st.write(bookdata)

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
            
            # print(html)
            
            # st.data_editor(book_clean_df,
                           # column_config = {"Cover" : st.column_config(label = None,*,width = "Large",help = None)},
                           # hide_index = True)

            # #col_header_logo_right_far.image(os.path.join(".","resources","hydra.png"),width=100,)

            # if col_header_text.button('This will open a new tab and go'):
                # self.do_redirect("https://hotstepper.readthedocs.io/index.html")

            # _,_,col_logo, col_text,_ = st.columns(MENU_LAYOUT)
            # col_logo.image(os.path.join(".","resources","data.png"),width=80,)
            # col_text.subheader("This explorer has multiple applications, each application could be run individually, however where is the fun in that? Below is a sample home page.")

            # st.markdown('<br><br>',unsafe_allow_html=True)


            # _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            # # if col_text.button('Cheat Sheet ➡️'):
            # #     self.do_redirect('Cheat Sheet')
            # col_logo.image(os.path.join(".","resources","classroom.png"),width=50,)
            # col_text.info("This application is all credit to [streamlit cheat sheet](https://github.com/daniellewisDL/streamlit-cheat-sheet), this is an example of how quickly an existing application can be wrapped in a HydraHeadAPP class and used in Hydralit.")

            # #The sample content in a sub-section with jump to format.
            # _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            # # if col_text.button('Sequency Denoising ➡️'):
            # #     self.do_redirect('Sequency Denoising')
                
            # col_logo.image(os.path.join(".","resources","denoise.png"),width=50,)
            # col_text.info("This application is a quick look at some analysis of vessel queue data with discrete denoising using Sequency methods as provided by the [Hotstepper](https://github.com/TangleSpace/hotstepper) package.")

            # _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            # # if col_text.button('Solar Mach ➡️'):
            # #     self.do_redirect('Solar Mach')
            # col_logo.image(os.path.join(".","resources","satellite.png"),width=50,)
            # col_text.info("This application is all credit to [Solar-MACH](https://github.com/jgieseler/Solar-MACH), this is an example of how quickly an existing application can be wrapped in a HydraHeadAPP class and used in Hydralit.")

            # _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            # # if col_text.button('Spacy NLP ➡️'):
            # #     self.do_redirect('Spacy NLP')
            # col_logo.image(os.path.join(".","resources","belgium.png"),width=50,)
            # col_text.info("This application is all credit to [spacy-streamlit-demo](https://github.com/ines/spacy-streamlit-demo), this is an example of how quickly an existing application can be wrapped in a HydraHeadAPP class and used in Hydralit.")

            # _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            # # if col_text.button('Uber Pickups ➡️'):
            # #     self.do_redirect('Uber Pickups')
            # col_logo.image(os.path.join(".","resources","taxi.png"),width=50,)
            # col_text.info("This application is all credit to [demo-uber-nyc-pickups](https://github.com/streamlit/demo-uber-nyc-pickups), this is an example of how quickly an existing application can be wrapped in a HydraHeadAPP class and used in Hydralit.")

    
        
        except Exception as e:
            # st.image(os.path.join(".","resources","failure.png"),width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))





