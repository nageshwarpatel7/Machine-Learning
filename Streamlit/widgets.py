import streamlit as st
import pandas as pd 
import numpy as np


## title
st.title("Streamlit text Input")

name = st.text_input("Enter your name:")
age = st.slider("Select your age",0,50)

options =["Python","Java", "C++","JavaScript"]
choice = st.selectbox("select your favourite language:",options=options)
if name:
    st.write(f"Hello {name}")
    st.write(f"your age is {age}")
    st.write(f"your favourite language is {choice}")
    
    
data ={"Name":["John","jane","Jake","Jill"],
       "Age":[28,24,35,40],
       "City": ["New York","Loss Angles","Chicago","Huston"]
    }
df = pd.DataFrame(data)
st.write(df)
    
uploaded_file = st.file_uploader("Choose a csv file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)