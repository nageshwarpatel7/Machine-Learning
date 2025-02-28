import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlit")

### Display a simple text
st.write("Hey this is my first Streamlit app")

## Create a simple dataFrame
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'Second Column':[10,20,30,40]
})


## Display the Dataframe
st.write("Hey this the dataframe")
st.write(df)

## create a line chat 
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)