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

    # Create checkboxes for each question
    show_q1 = st.checkbox("1.How will you hide the indexes of the dataframe?.")
    show_q2 = st.checkbox("2. How can we set the caption / heading on the dataframe?")
    show_q3 = st.checkbox("3. Show the records related with the districts - New Delhi , Lucknow , Jaipur.")
    show_q4 = st.checkbox("4. Calculate state-wise total number of popluation and population with different religions.")
    show_q5 = st.checkbox("5. How many Male Workers were there in Maharashtra state ?")
    show_q6 = st.checkbox("6. How to set a column as index of the dataframe ?")
    q7a = st.checkbox("7a. Add a Suffix to the column names.")
    q7b = st.checkbox("7b. Add a Prefix to the column names.")
    if show_q1:
        st.write(data.style.hide_index())
    if show_q2:
        st.write(data.style.set_caption('India Census 2011 Dataset'))
    if show_q3:
        st.write(data[data['District_name'].isin(['New Delhi', 'Lucknow', 'Jaipur'])])
    if show_q4:
        st.write(data.groupby('State_name').agg({'Population': 'sum', 'Hindus': 'sum', 'Muslims': 'sum', 'Christians': 'sum', 'Sikhs': 'sum', 'Buddhists': 'sum', 'Jains': 'sum'}).sort_values(by='Population', ascending=False))
    if show_q5:
        st.write(data[data.State_name == 'MAHARASHTRA']['Male_Workers'].sum())
    if show_q6:
        st.write(data.set_index('District_code'))
    if q7a:
        st.write(data.add_suffix('_rightone'))
    if q7b:
        st.write(data.add_prefix('leftone_'))


    # Perform the required operations based on the checkbox selections and display the output
    
   
    
    
    
    
   
    

