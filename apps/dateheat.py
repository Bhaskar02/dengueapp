import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import leafmap.foliumap as leafmap
import datetime



def app():

    st.title('Heatmaps')

    
    
    df = pd.read_csv('https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/dengue11f.csv')
    
    m = leafmap.Map(location=[20.5937, 78.9629],zoom_start=5,tiles="stamentoner")
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    start_date = st.date_input('Start date', today)
    end_date = st.date_input('End date', tomorrow)
    data=df[(df.dat>=str(start_date)) & (df.dat<=str(end_date))]
    data=data[['lat','lon','cases']]
    #HeatMap(data).add_to(m))
    #folium.LayerControl().add_to(m)
    m.to_streamlit(width=700, height=700)
