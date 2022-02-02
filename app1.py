#import cv2
import numpy as np
import streamlit as st

from PIL import Image

option = st.selectbox('Select the year',('2010', '2011', '2012','2013','2014','2015','2016'))
image = Image.open('output/'+option+'.png')

st.image(image, caption='corelation '+option,width=500,use_column_width=500)
#images = ['output/2010.png', 'output/2011.png', 'output/2012.png']
#st.image(images, use_column_width=True, caption=["some generic text"] * len(images))
