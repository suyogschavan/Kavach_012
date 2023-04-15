""" ================================================== 
 Description     : title1
 Author          : Suyog Chavan
 Reach me here   : https://suyogschavan.github.io 
 Date of creation: Saturday, 15 Apr 2023 
 Copyright       : ©suyogschavan03@gmail.com
================================================== """
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

df = pd.read_excel("./transactions.xlsx")
# print(data)



# SIDEBAR

st.sidebar.header("Please Filter here: ")
TransactionType = st.sidebar.multiselect(
    "Select the Transaction Type: ",
    options=df["transactiontype"].unique(),
    default=df["transactiontype"].unique()
)


Amount = st.sidebar.multiselect(
    "Select the Amount: ",
    options=df["amount"].unique(),
    default=df["amount"].unique()
)


df_selection = df.query(
    'amount == @Amount & transactiontype == @TransactionType'
)
st.dataframe(df_selection)



# MAINPAGE

st.title(":bar_chart: Transactions")
st.markdown("##")

total_transactions = int(df_selection['transactionID'].count())
average_amount = round(df_selection["amount"].mean())
total_amount_transfered = round(df_selection["amount"].sum(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total no. of Transactions: ")
    st.subheader(f"{total_transactions:,}")
with middle_column:
    st.subheader("Average transfered Amount: ")
    st.subheader(f"{average_amount}")
with right_column:
    st.subheader("Total Amount Trasfered: ")
    st.subheader(f"Rs ₹{total_amount_transfered}")
    
    
st.markdown("---")
    

