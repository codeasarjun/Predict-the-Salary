import streamlit as st
from show_prediction import  show_prediction_page
from know_more import show_more_info

page=st.sidebar.selectbox('Explore or Predict',('Predict','Explore'))

if page=='Predict':
    show_prediction_page()
else:
    show_more_info()


