import streamlit as st
import pandas as pd 

st.header('Super Sales')
data = pd.read_csv('mentornow/superSales.csv')
a = data['Product_line'].unique() 
st.write('Top Stats')

c1,c2,c3 =st.columns(3)

with st.sidebar:
    option = st.selectbox('Select Product_line',(a))

b=data[data['Product_line'] ==option]
c1.metric(label='Total Invoice',value = b['Invoice_ID'].size) 
c2.metric(label='Average Rating',value=round(b['Rating'].mean(),2))