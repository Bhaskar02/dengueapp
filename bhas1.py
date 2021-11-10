import streamlit as st
from multiapp import MultiApp
from apps import (
    
    heatmap,
    line1,
    line
    
)

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here


apps.add_app("Heatmaps", heatmap.app)
apps.add_app("Bargraph", line1.app)
apps.add_app("Bargraph1", line.app)


# The main app
apps.run()
