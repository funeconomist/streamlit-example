
import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

path1 = 'https://raw.githubusercontent.com'
path2 = '/dataprofessor/data/master/'
path3 = 'penguins_cleaned.csv'
df = pd.read_csv(path1+path2+path3)
pr = df.profile_report()
st_profile_report(pr)