import streamlit as st
import pandas as pd

# Title of the web app
t.title('Streamlit Website')

# Add some text
st.write('Hello World!')

st.write({"key": ["value"]})


data = pd.DataFrame([
    {'a': 1, 'b': 2, 'c': 3},
    {'a': 4, 'b': 5, 'c': 6},
    {'a': 7, 'b': 8, 'c': 9},
])

st.write(data)