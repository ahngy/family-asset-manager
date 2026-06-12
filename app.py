import streamlit as st

from utils.sheets import get_accounts

st.set_page_config(
    page_title="우리집 자산관리",
    page_icon="🏠",
    layout="wide",
)

st.title("🏠 우리집 자산관리")

st.subheader("계좌 목록")

df = get_accounts()

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
)