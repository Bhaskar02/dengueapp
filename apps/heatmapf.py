import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import leafmap.foliumap as leafmap



def app():

    st.title('Heatmaps')

    filepath = "https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/dw.csv"
    url = 'https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/denguef.csv'
    df1 = pd.read_csv(url)
    columns1 = df1.columns.tolist()
    selected_columns = st.multiselect("select column", columns1, default='2012')
    m = leafmap.Map(location=[20.5937, 78.9629],zoom_start=5,tiles="stamentoner")
    m.add_heatmap(
        filepath,
        latitude="lat",
        longitude="lon",
        value="cases",
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(width=700, height=700)
