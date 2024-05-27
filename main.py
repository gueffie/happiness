import plotly.express as px
import streamlit as st
import pandas as pd

st.title("In Search of Happiness")
df = pd.read_csv("happy.csv")
option = [row for row in df]


x = st.selectbox(label="Choose your X -axis", options=option)
y = st.selectbox(label="Choose your Y -axis", options=option)

st.subheader(f"{x} and {y}")

print(df[x])

print(x)


figure = px.scatter(x=df[x], y=df[y], labels={"x": x, "y": y})
st.plotly_chart(figure)