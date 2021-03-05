# First we imported necessary libraries
import streamlit as st
import pandas as pd
import base64
from PIL import Image # To load image for designing

# We selected necessary columns with variables
aud = "AUD/US$"
euro = "EURO/US$"
pound = "POUND/US$"

date = "time/date"

# Function to load csv file to cache memory. By that we avoided loading the same file several times. 
@st.cache
def load_data():
    url = "Foreign_Exchange_Rates.csv"
    data = pd.read_csv(url, parse_dates=True, index_col=date)
    return data

# The function that downloads csv file
def download_csv(name,df):
    csv = df.to_csv(index=False)
    base = base64.b64encode(csv.encode()).decode()
    file = (f'<a href="data:file/csv;base64,{base}" download="%s.csv">Download file</a>' % (name))
    return file

# Starting main function
if __name__ == '__main__':
    df = load_data() # Loading data by inherited function

    # Loading image
    img = Image.open("index.jpeg") 
    st.image(img)

    # Writing title and subtitle of project 
    st.title('Exchange rates comparison')
    st.write("## Data Vizualation")
    st.write("#") # For making space

    # We made containers for each column 
    column_1 = st.sidebar 
    column_1.subheader("Types of charts")

    column_1.write("#") # For making space
    
    charts = ["Line Chart", "Bar Chart", "Table"] # List of charts and table
    # For making selecting box
    selected_chart = column_1.selectbox("Select one of them", charts)

    # Conditional selecting for type of charts                  
    if selected_chart == "Line Chart":
        st.line_chart(df)
    elif selected_chart == "Bar Chart":
        st.bar_chart(df)
    else:
        st.table(df)
    
    # Code for making possible others to download the csv file
    st.markdown(download_csv('Filtered Data Frame',df),unsafe_allow_html=True) 
  
    # For removing the ads 
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    # Code for writing the names of authors (with css)
    st.write('<style>body { margin: 0; font-family: Arial, Helvetica, sans-serif;} .header{padding: 10px 16px; background: #555; color: #f1f1f1; position:fixed;bottom:0;right:0;}} </style><div class="header" id="myHeader">'+"Made by Malikakhon and Jasurbek"+'</div>', unsafe_allow_html=True)
