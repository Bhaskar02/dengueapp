import streamlit as st
from multiapp import MultiApp
from apps import (
    
    heatmap
    
)

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here


apps.add_app("Heatmaps", heatmap.app)


# The main app
apps.run()
