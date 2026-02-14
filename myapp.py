import streamlit as st
import pandas as pd
import numpy as np

st.header("Map")
 
data = {"lat":[28.704060, 28.459497, 13.082680, 17.385044, 23.0225],
        "lon":[77.102493, 77.026634, 80.270721, 78.486671, 72.5714],
        "City": ["Delhi", "Gurgaon", "Chennai", "Hyderabad", "Ahemdabad"]}
 
df = pd.DataFrame(data)
df
st.map(data=df)
