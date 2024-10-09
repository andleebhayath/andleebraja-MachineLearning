import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title('👍 Machine Learning  app')

st.info('This App builds a machine learning model')
with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
  st.write('**x**')
  x_raw = df.drop('species', axis=1)
  x_raw
  st.write('**y**')
  y_raw= df.species
  y_raw
with st.expander('Data visualization'):
   st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')
with st.sidebar:
  st.header('Input Feature')
  island = st.selectbox('IsLand',('Biscoe','Dream','Torgerson'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm= st.slider(Bill Depth (mm)', 31.1, 21.6, 17.2)
  
  
   
  
  

