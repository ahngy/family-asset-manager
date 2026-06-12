import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


@st.cache_resource
def get_client():
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=SCOPES,
    )
    return gspread.authorize(creds)


def get_accounts():
    client = get_client()

    sheet = client.open("FamilyFinanceDB").worksheet("Accounts")

    data = sheet.get_all_records()

    return pd.DataFrame(data)