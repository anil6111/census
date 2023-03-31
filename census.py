import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random
from PIL import Image
logo = Image.open('logo.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run streamlit :   streamlit run netflix.py 
st.set_page_config(page_title="INDIA CENSUS  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
# Define the list of names
names = ["21A21A6111-E Jeji Anil", "21A21A6158-Tusha Rahul B ", "21A21A6137-M S R Chandrika","21A21A6166-K Shyam chand","21A21A6101-A Leena","21A21A6140-N Upendra","21A21A6157-T Sumanth Raju","22A25A6105(L5)-T Naveen Babu"]
st.title("Exploratory Data Analysis on India Census Data Set")
# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)
st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.Bomma.Ramakrishna")
# File upload
uploaded_file = st.file_uploader("Choose a India Census Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data)

    st.title("India Census Data Analysis")

    if st.checkbox('1. HOW WILL YOU HIDE THE INDEXES OF THE DATAFRAME?.'):
        st.write(data.style.hide_index())

    if st.checkbox('2. HOW CAN WE SET THE CAPTION / HEADING ON THE DATAFRAME?.'):
        st.write(data.sytle.set_caption('Indian Census 2011 Dataset'))
    
    q7a = st.checkbox("7a. Add a Suffix to the column names.")
    if q7a:
        st.write(data.add_suffix('_rightone'))
    
    q7b = st.checkbox("7b. Add a Prefix to the column names.")
    if q7b:
        st.write(data.add_prefix('leftone_'))
    
    
    
    
    
    
    
    


    
