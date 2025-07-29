import streamlit as st
import pandas as pd

st.title("📊 간단한 Streamlit 대시보드")
df = pd.DataFrame({
    "이름": ["철수", "영희", "민수"],
    "점수": [87, 92, 75]
})
st.dataframe(df)