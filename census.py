import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
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
    
    if st.checkbox("checking weather the data is preprocessed or NOT !?"):
        st.write(data.isnull().sum())
    if st.checkbox("NO OF COLUMNS :"):
        st.write("no of columns in this dataset :",data.columns)
    if st.checkbox("PERFORM SOME STATISTICAL OPERATIONS ---"):
        st.write(data.describe())
    if st.checkbox("Calculate the total population of India according to the 2011 Census?"):
        total_population = data['Population'].sum()
        st.write("Total Population of India according to the 2011 Census is:", total_population)
    if st.checkbox("Find the statewise total population  of India "):
        state_options = data['State_name'].unique()
        selected_state = st.selectbox("Select a state", state_options)
        state_pop_data = data[data['State_name'] == selected_state]
        st.write(f"Total population of {selected_state} in 2011: {state_pop_data.iloc[0]['Population']:,}")
    if st.checkbox("Calculate the correlation coefficient between two Attributes"):
        corr = data['Male_Workers'].corr(data['Female_Workers'])
        st.write("Correlation coefficient:", corr)

    if st.checkbox("Population of Top 10 Cities in India (Census 2011)"):
        data = data.sort_values('Population', ascending=False).head(20)
        fig, ax = plt.subplots()
        ax.bar(data['State_name'], data['Population'])
        ax.set_title('Population of Top 10 Cities in India (Census 2011)')
        ax.set_xlabel('State_name')
        ax.set_ylabel('Population')
        plt.xticks(rotation=20)
        st.pyplot(fig)
    if st.checkbox("pie chart"):
        column_name = st.selectbox('Select a column for the pie chart', data.columns)
        value_counts = data[column_name].value_counts()
        fig = px.pie(values=value_counts.values, names=value_counts.index)
        st.plotly_chart(fig)


    if st.checkbox("line plot "):
        sns.lineplot(x=data['Male_Workers'],y=data['Female_Workers'])
        plt.title("LINE PLOT ")
        st.pyplot.show()

    if st.checkbox("pie chart of female workers vs male workers :"):
        fig,ax=plt.subplots()
        x=[data['State_name']==HARYANA.value_counts(),data['State_name']==ORISSA.value_counts(),data['State_name']==KERALA.value_counts()]
        mylabels=['GUJARAT','ORISSA','ANDHRA PRADESH']
        sns.pie(x,labels=mylabels)
        st.pyplot(fig)
        
        
    
    
    if st.checkbox("How will you hide the indexes of the dataframe?"):
        st.write(data.style.hide_index())
    if st.checkbox("How can we set the caption / heading on the dataframe?"):
        st.write(data.style.set_caption('India Census 2011 Dataset'))
    if st.checkbox("Show the records related with the districts - New Delhi , Lucknow , Jaipur"):
        st.write(data[data['District_name'].isin(['New Delhi', 'Lucknow', 'Jaipur'])])
    if st.checkbox("Calculate state-wise total number of popluation and population with different religions"):
        st.write(data.groupby('State_name').agg({'Population': 'sum', 'Hindus': 'sum', 'Muslims': 'sum', 'Christians': 'sum', 'Sikhs': 'sum', 'Buddhists': 'sum', 'Jains': 'sum'}).sort_values(by='Population', ascending=False))
    if st.checkbox("How many Male Workers were there in Maharashtra state ?"):
        st.write(data[data.State_name == 'MAHARASHTRA']['Male_Workers'].sum())
    if st.checkbox(" How to set a column as index of the dataframe ?"):
        st.write(data.set_index('District_code'))
    if st.checkbox("Add a Suffix to the column names"):
        st.write(data.add_suffix('_rightone'))
    if st.checkbox("Add a Prefix to the column names"):
        st.write(data.add_prefix('leftone_'))

    if st.checkbox("data Visualizations"):
        def load_data():
            return data
        def main():
            df = load_data()
            st.title("My Data visualization Web Application")
            
            st.subheader("Data Visualization 1")
            fig, ax = plt.subplots(figsize = (30,10))
            sns.histplot(data=data,x='State_name')
            st.pyplot(fig)
            
            #st.subheader("Data Visualization 2")
            #fig = px.scatter(data, x="Literate", y="Workers")
            #st.plotly_chart(fig)
        if __name__ == "__main__":
            main()
    
    if st.checkbox("Correlation heatmap between two similar columns"):
        corr_matrix = data.iloc[:,3:7].corr()
        fig,ax=plt.subplots()
        sns.heatmap(corr_matrix)
        plt.title("Correlation Heatmap :")
        st.pyplot(fig)
    
            
            
        
    
        
