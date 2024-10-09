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
  bill_depth_mm= st.slider('Bill Depth (mm)', 31.1, 21.6, 17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
  gender= st.selectbox('Gender',('male','female'))
  Date = {'Island':island,
          'bill_length_mm' : Bill_length_(mm),
          'bill_depth_mm'  : Bill_Depth_(mm),
          'flipper_length_mm' :Flipper_length_(mm),
          'body_mass_g'      : Body_mass_(g),
          'Sex':Gender}
 input_df = pd.DataFrame(data, index=[0])
 input_df
 
          
       
  
  
   
  
  

