import streamlit as st
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

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


def add_account(owner, bank, account_name, balance, account_type):
    client = get_client()
    sheet = client.open("FamilyFinanceDB").worksheet("Accounts")

    rows = sheet.get_all_values()
    next_id = len(rows)

    sheet.append_row([
        next_id,
        owner,
        bank,
        account_name,
        balance,
        account_type,
    ])