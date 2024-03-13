import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

df_reviews = pd.read_csv("./data/customer reviews.csv")
df_top100_books = pd.read_csv("./data/Top-100 Trending Books.csv")

df_reviews
