import streamlit as st
from multiapp import MultiApp
from apps import (
    
    h1,
    line1,
    line,
    heatmapf,
    dateheat,
    ras
    
)

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here


apps.add_app("Hmaps", h1.app)
apps.add_app("Bargraph", line1.app)
apps.add_app("Bargraph1", line.app)
apps.add_app("heatmapf", heatmapf.app)
apps.add_app("dateheat", dateheat.app)
apps.add_app("ras", ras.app)


# The main app
apps.run()
