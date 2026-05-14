import pandas as pd
import re

def clean_phone(phone):
    if not phone: return None
    return re.sub(r'\D', '', str(phone))

def clean_email(email):
    if not email: return None
    return email.strip().lower()

def clean_crm_data(df):
    """
    Standardizes phone numbers and emails for RevOps data integrity.
    Follows the Financial Pivot Law: Clean data = Accurate Revenue Attribution.
    """
    df['phone'] = df['phone'].apply(clean_phone)
    df['email'] = df['email'].apply(clean_email)
    return df
