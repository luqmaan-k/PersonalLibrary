import streamlit as st
import sqlite3 as sql
from PIL import Image
import pandas as pd
import csv
st.write("""
# Test
""")
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))