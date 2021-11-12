import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import leafmap.foliumap as leafmap

def app():

    st.title('Heatmaps1')

    filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    url = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
    df1 = pd.read_csv(url)
    columns1 = df1.columns.tolist()
    selected_columns = st.multiselect("select column", columns1, default='2012')
    s = df1[selected_columns[0]]
    m = leafmap.Map(tiles="Heatmap")
    m.add_heatmap(
        filepath,
        latitude="lat",
        longitude="long",
        value="2012",
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(width=700, height=500)
