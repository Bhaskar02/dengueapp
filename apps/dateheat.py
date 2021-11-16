import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import leafmap.foliumap as leafmap
import datetime



def app():

    st.title('Heatmaps')

    filepath = "https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/denguelatdata.csv"
    url = 'https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/denguelatdata.csv'
    m = leafmap.Map(location=[20.5937, 78.9629],zoom_start=5,tiles="stamentoner")
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    start_date = st.date_input('Start date', today)
    end_date = st.date_input('End date', tomorrow)
    m.to_streamlit(width=700, height=700)
