import streamlit as st
import pickle
import pandas as pd


pipe = pickle.load(open('ranit.pkl', 'rb'))

st.title('   \n')
st.title(' \n')
st.title(' \n')
st.title(' \n')
st.title(' \n')
st.title('\n\n IRIS ')


col1, col2, col3, col4 = st.columns(4)

with col1:
    sepal_length = st.number_input(label='sepal_length',step=1.,format="%.1f")
with col2:
    sepal_width = st.number_input(label='sepal_width',step=1.,format="%.1f")
with col3:
    petal_length = st.number_input(label='petal_length',step=1.,format="%.1f")
with col4:
    petal_width = st.number_input(label='petal_width',step=1.,format="%.1f")


if st.button('Get prediction '):

    input_df = pd.DataFrame(
        {'sepal_length': [sepal_length], 'sepal_width': [sepal_width], 'petal_length': [petal_length], 'petal_width': [petal_width]
    })
    result = pipe.predict(input_df)
    b=result[0]
    if b == 3:

        st.header("Iris-versicolor")
    elif b== 2:

        st.header("Iris-setosa")

    else:

        st.header("Iris-virginica")