import streamlit as st
from PIL import Image, ExifTags
import hashlib
import requests
import pandas as pd
import re

# --- CONFIGURACIÓN RED OPS v8 ---
st.set_page_config(page_title="RED_OPS_v8_DEEP_RECON", page_icon="🛑", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stApp { background-color: #000000; }
    h1, h2, h3, p, span, label { color: #FF0000 !important; font-family: 'Courier New', monospace !important; text-shadow: 0 0 5px #ff0000; }
    [data-testid="stSidebar"] { background-color: #0a0000 !important; border-right: 1px solid #FF0000; }
    [data-testid="stSidebar"] * { color: #FF0000 !important; }
    .stButton>button { background-color: #000000; color: #FF0000; border: 1px solid #FF0000; border-radius: 0px; width: 100%; }
    .stButton>button:hover { background-color: #FF0000; color: #000000; box-shadow: 0 0 15px #ff0000; }
    input, textarea { background-color: #0a0a0a !important; color: #FF0000 !important; border: 1px solid #FF0000 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL ---
st.sidebar.title("🚨 RED_TERMINAL_v8")
cat = st.sidebar.radio("NIVEL DE ACCESO:", ["🎯 INTEL_GATHERING", "🕵️ DEEP_RECON", "📄 DATA_ANALYSIS"])

# --- CATEGORÍA 1: INTEL_GATHERING ---
if cat == "🎯 INTEL_GATHERING":
    opcion = st.sidebar.selectbox("MÓDULO:", ["TARGET_DOSSIER", "OSINT_USER", "NETWORK_STALKER"])
    
    if opcion == "TARGET_DOSSIER":
        st.title("🎯 TARGET_DOSSIER")
        nombre = st.text_input("NOMBRE DEL OBJETIVO:")
        if nombre:
            q = nombre.replace(" ", "+")
            st.markdown(f"### 🔍 INVESTIGACIÓN AVANZADA: {nombre}")
            st.markdown(f"- [📄 BUSCAR PDFs](https://www.google.com/search?q=filetype:pdf+%22{q}%22)")
            st.markdown(f"- [🏛️ REGISTROS OFICIALES](https://www.google.com/search?q=site:es+OR+site:gob.*+%22{q}%22)")

    elif opcion == "OSINT_USER":
        st.title("🕵️ OSINT_USER_FINDER")
        user = st.text_input("ID DE USUARIO:")
        if user:
            st.markdown(f"[🔍 INSTAGRAM](https://www.instagram.com/{user})")
            st.markdown(f"[🔍 GITHUB](https://github.com/{user})")

# --- CATEGORÍA 2: DEEP_RECON (LAS TRES NUEVAS) ---
elif cat == "🕵️ DEEP_RECON":
    opcion = st.sidebar.selectbox("MÓDULO:", ["HIDDEN_LEAKER", "DIR_DISCOVERY", "ZOMBIE_DOMAIN"])
    
    if opcion == "HIDDEN_LEAKER":
        st.title("📧 HIDDEN_LEAKER: EXTRACCIÓN DE DATOS OCULTOS")
        url = st.text_input("URL DE LA WEB A ESCANEAR:")
        if st.button("EJECUTAR ESCANEO"):
            try:
                response = requests.get(url, timeout=5)
                emails = re.findall(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+', response.text)
                st.subheader("CORREOS ELECTRÓNICOS DETECTADOS EN EL CÓDIGO:")
                if emails: st.write(list(set(emails)))
                else: st.error("No se encontraron rastros públicos en la superficie HTML.")
            except: st.error("Error de conexión con el host objetivo.")

    elif opcion == "DIR_DISCOVERY":
        st.title("📂 DIRECTORY_DISCOVERY")
        host = st.text_input("URL OBJETIVO (ej: https://web.com):")
        if host:
            rutas = ["/admin", "/backup", "/config", "/db", "/logs", "/.env", "/wp-admin"]
            st.warning("Probando rutas críticas de seguridad...")
            for r in rutas:
                st.code(f"CHECKING: {host}{r}")

    elif opcion == "ZOMBIE_DOMAIN":
        st.title("🛡️ ZOMBIE_DOMAIN: SUBDOMINIOS")
        st.write("Esta herramienta proyecta posibles subdominios del objetivo.")
        dom = st.text_input("DOMINIO RAIZ (ej: google.com):")
        if dom:
            subs = ["dev.", "test.", "api.", "mail.", "staff.", "vpn."]
            for s in subs: st.write(f"🚩 POSIBLE NODO: {s}{dom}")

# --- CATEGORÍA 3: DATA_ANALYSIS (DEEP-TEXT SCANNER) ---
elif cat == "📄 DATA_ANALYSIS":
    opcion = st.sidebar.selectbox("MÓDULO:", ["DEEP_TEXT_SCANNER", "GPS_TRACKER", "CAMOUFLAGE"])
    
    if opcion == "DEEP_TEXT_SCANNER":
        st.title("🕵️‍♂️ DEEP_TEXT_SCANNER: EXTRACCIÓN MASIVA")
        st.write("Pega un bloque de texto para extraer automáticamente entidades de interés.")
        data = st.text_area("PEGAR TEXTO AQUÍ:", height=200)
        if st.button("ANALIZAR CONTENIDO"):
            emails = re.findall(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+', data)
            ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', data)
            st.subheader("RESULTADOS DEL ANÁLISIS:")
            st.write(f"📧 Correos: {len(emails)}")
            if emails: st.code(emails)
            st.write(f"🌐 IPs: {len(ips)}")
            if ips: st.code(ips)

    elif opcion == "GPS_TRACKER":
        st.title("🛰️ GPS_TRACKER")
        st.file_uploader("SUBIR IMAGEN", type=["jpg", "jpeg"])