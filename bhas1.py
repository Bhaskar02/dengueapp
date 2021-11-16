import streamlit as st
from multiapp import MultiApp
from apps import (
    
    h1,
    line1,
    line,
    heatmapf,
    dateheat
    
)

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here


apps.add_app("Heatmaps", h1.app)
apps.add_app("Bargraph", line1.app)
apps.add_app("Bargraph1", line.app)
apps.add_app("heatmapf", heatmapf.app)
apps.add_app("dateheat", dateheat.app)


# The main app
apps.run()
