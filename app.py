import streamlit as st

st.set_page_config(
    page_title="우리집 자산관리",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 우리집 자산관리")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("총 자산", "0원")

with col2:
    st.metric("총 부채", "0원")

with col3:
    st.metric("순자산", "0원")

st.divider()

st.subheader("최근 거래")

st.info("아직 등록된 거래가 없습니다.")