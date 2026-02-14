import streamlit as st

st.header('Exemple : st.button')

if st.button('say hello'):
     
     st.write('why hello?')
else:
     st.write('goodbye')
