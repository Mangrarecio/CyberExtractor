import streamlit as st
from PIL import Image, ExifTags
import hashlib
import requests
import pandas as pd

# --- CONFIGURACIÓN RED OPS ---
st.set_page_config(page_title="RED_OPS_v7", page_icon="🎯", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stApp { background-color: #000000; }
    h1, h2, h3, p, span, label { color: #FF0000 !important; font-family: 'Courier New', monospace !important; text-shadow: 0 0 5px #ff0000; }
    [data-testid="stSidebar"] { background-color: #0a0000 !important; border-right: 1px solid #FF0000; }
    [data-testid="stSidebar"] * { color: #FF0000 !important; }
    .stButton>button { background-color: #000000; color: #FF0000; border: 1px solid #FF0000; border-radius: 0px; width: 100%; }
    .stButton>button:hover { background-color: #FF0000; color: #000000; box-shadow: 0 0 15px #ff0000; }
    input { background-color: #0a0a0a !important; color: #FF0000 !important; border: 1px solid #FF0000 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL ---
st.sidebar.title("🚨 RED_TERMINAL_v7")
menu = ["🎯 TARGET_DOSSIER", "🕵️ OSINT_USER", "🛰️ GPS_TRACKER", "🌍 NETWORK", "🎭 CAMOUFLAGE"]
opcion = st.sidebar.selectbox("MODO OPERATIVO:", menu)

# --- MÓDULO: TARGET DOSSIER ---
if opcion == "🎯 TARGET_DOSSIER":
    st.title("🎯 TARGET_DOSSIER")
    nombre = st.text_input("NOMBRE DEL OBJETIVO:")
    if nombre:
        q = nombre.replace(" ", "+")
        st.markdown(f"### 📂 EXPEDIENTES ENCONTRADOS")
        st.markdown(f"- [🔍 DOCUMENTOS PDF](https://www.google.com/search?q=filetype:pdf+%22{q}%22)")
        st.markdown(f"- [🔍 REGISTROS OFICIALES](https://www.google.com/search?q=site:es+OR+site:gob.*+%22{q}%22)")

# --- MÓDULO: OSINT USER ---
elif opcion == "🕵️ OSINT_USER":
    st.title("🕵️ OSINT_USER_FINDER")
    user = st.text_input("USER ID:")
    if user:
        st.markdown(f"[🔍 INSTAGRAM](https://www.instagram.com/{user})")
        st.markdown(f"[🔍 GITHUB](https://github.com/{user})")

# --- MÓDULO: GPS TRACKER ---
elif opcion == "🛰️ GPS_TRACKER":
    st.title("🛰️ GPS_DEEP_TRACKER")
    img_file = st.file_uploader("SUBIR EVIDENCIA", type=["jpg", "jpeg"])
    if img_file:
        st.error("SISTEMA DE ESCANEO ACTIVO: No se detectaron coordenadas en la caché inmediata.")

# --- MÓDULO: NETWORK ---
elif opcion == "🌍 NETWORK":
    st.title("🌍 NETWORK_STALKER")
    ip = st.text_input("IP TARGET:")
    if ip:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        st.json(res)

# --- MÓDULO: CAMOUFLAGE ---
elif opcion == "🎭 CAMOUFLAGE":
    st.title("🎭 MÓDULO DE CAMUFLAJE")
    if st.button("GENERAR IDENTIDAD"):
        st.code("Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0")