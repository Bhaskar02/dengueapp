import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import leafmap.foliumap as leafmap

def app():
  st.title('BarGraph')
  df1 = pd.read_csv('https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/dengue101721f.csv')
  #df = df.groupby(['States/UTs', '2012'])
  columns1 = df1.columns.tolist()
  selected_columns = st.multiselect("select column", columns1, default='2012')
  s = df1[selected_columns[0]]

  trace = go.Bar(x=df1['States/UTs'],y=s.values,showlegend = True)
  layout = go.Layout(title = "test")
  data = [trace]
  fig = go.Figure(data=data,layout=layout)
  st.plotly_chart(fig)
