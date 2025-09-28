# frameworks_assignment.py
# CORD-19 Metadata Analysis with Sample Dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st
import os

# Load or generate sample dataset 
if not os.path.exists("metadata.csv"):
    st.write(" metadata.csv not found. Generating a small sample dataset")
    data = {
        "cord_uid": range(1, 21),
        "title": [f"COVID-19 Paper {i}" for i in range(1, 21)],
        "authors": ["Author A, Author B"]*20,
        "abstract": ["Sample abstract text"]*20,
        "journal": ["Journal A", "Journal B", "Journal C", "Journal D"]*5,
        "publish_time": pd.date_range("2020-01-01", periods=20, freq="M")
    }
    df = pd.DataFrame(data)
else:
    df = pd.read_csv("metadata.csv")

# Data Cleaning
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

# Analysis
year_counts = df['year'].value_counts().sort_index()
top_journals = df['journal'].value_counts().head(10)
titles_text = " ".join(df['title'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles_text)

# Streamlit App
def plot_publications_by_year():
    plt.figure(figsize=(8,5))
    sns.barplot(x=year_counts.index, y=year_counts.values)
    plt.title("Publications by Year")
    plt.xlabel("Year")
    plt.ylabel("Count")
    st.pyplot(plt.gcf())

def plot_top_journals():
    plt.figure(figsize=(8,5))
    sns.barplot(y=top_journals.index, x=top_journals.values)
    plt.title("Top Journals Publishing COVID-19 Research")
    plt.xlabel("Count")
    plt.ylabel("Journal")
    st.pyplot(plt.gcf())

def show_wordcloud():
    plt.figure(figsize=(10,6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Paper Titles")
    st.pyplot(plt.gcf())

def main():
    st.title("CORD-19 Data Explorer (Sample Dataset)")
    st.write("Exploration of COVID-19 papers using a small sample dataset")
    
    if st.checkbox("Show sample data"):
        st.write(df.head())
    
    min_year, max_year = int(df['year'].min()), int(df['year'].max())
    year_range = st.slider("Select year range", min_year, max_year, (min_year, max_year))
    filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
    st.write(f"Number of papers between {year_range[0]} and {year_range[1]}: {filtered.shape[0]}")
    
    st.subheader("Publications Over Time")
    plot_publications_by_year()
    
    st.subheader("Top Journals")
    plot_top_journals()
    
    st.subheader("Word Cloud of Titles")
    show_wordcloud()

if __name__ == "__main__":
    main()
