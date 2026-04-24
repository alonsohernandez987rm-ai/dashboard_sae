import streamlit as st
import pandas as pd
from db import get_connection

st.title("Dashboard SAE 🔥")

if st.button("Probar conexión"):
    try:
        conn = get_connection()
        st.success("Conectado a SAE correctamente 😎")
        conn.close()
    except Exception as e:
        st.error(f"Error: {e}")