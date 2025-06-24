import streamlit as st
import advertools as adv
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file, encoding='utf-16',sep="\t", header=None, skiprows=2)
    # Step 2: Set the first row as the header
    df.columns = df.iloc[0]       # use row 0 as header
    df = df[1:].reset_index(drop=True)  # drop that header row from data
    df["Avg. monthly searches"] = df["Avg. monthly searches"].astype(int)
    df = df[df['Keyword'].str.contains('django', case=False, na=False)]
    
    word_freq = adv.word_frequency(text_list=df['Keyword'],
                                   num_list=df['Avg. monthly searches'],phrase_len=2, rm_words=[])
    
    # try sorting by 'abs_freq', 'wtd_freq', and 'rel_value':
    word_freq.sort_values(by='wtd_freq',ascending=False).head(50)
