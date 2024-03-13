import streamlit as st
import pandas as pd
import plotly.express as px


# Configurações da página
st.set_page_config(layout="wide")


df_reviews = pd.read_csv("./data/customer reviews.csv")
df_top100_books = pd.read_csv("./data/Top-100 Trending Books.csv")


price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

# Input para escolher o preço máximo
max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)

# Definindo o preço máximo
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books


fig1 = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

# Criando colunas
col1, col2 = st.columns(2)

col1.plotly_chart(fig1)
col2.plotly_chart(fig2)
