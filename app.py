import streamlit as st
import pandas as pd 
import plotly.express as px

st.header('Super Sales')
data = pd.read_csv('mentornow/superSales.csv')
a = data['Product_line'].unique() 
st.write('Top Stats')

with st.sidebar:
    option = st.selectbox('Select Product_line',(a))

c1,c2,c3 =st.columns(3)

b=data[data['Product_line'] ==option]

c1.metric(label='Total Invoice',value =b['Invoice_ID'].size) 
c2.metric(label='Average Rating',value=round(b['Rating'].mean(),2))
c3.metric(label='Total Price',value=round(b['Total_price'].sum(),2))

cl1,cl2,cl3 =st.columns(3)

incom = round(b['Total_price'].sum(),2)
cl1.metric(label='Total_price',value=incom)

cost = round(b['costs'].sum(),2)
cl2.metric(label='Costs',value=cost)

d=(incom-cost)
cl3.metric(label='Profit',value=d)

b['Order_date'] = pd.to_datetime(b['Order_date'])

b1=b[b['Order_date'].dt.month==3]

b1['date']=b1['Order_date'].dt.day

grp = b1.groupby('date')['Quantity'].sum().reset_index()
st.write(grp)

fig = px.line(grp,x='date', y='Quantity',title='Total Quantity by Date')
st.write(fig)