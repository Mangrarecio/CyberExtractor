import streamlit as st
from PIL import Image
import hashlib
import requests
import pandas as pd
import pypdf
import random

# --- CONFIGURACIÓN ESTILO MATRIX ---
st.set_page_config(page_title="MATRIX OPS SUITE", page_icon="📟", layout="wide")

st.markdown("""
    <style>
    /* Fondo negro y texto verde neón */
    .main { background-color: #000000; }
    .stApp { background-color: #000000; }
    h1, h2, h3, p, span, label { color: #00FF41 !important; font-family: 'Courier New', monospace !important; }
    
    /* Personalización de la barra lateral */
    [data-testid="stSidebar"] { background-color: #050505 !important; border-right: 1px solid #00FF41; }
    [data-testid="stSidebar"] * { color: #00FF41 !important; }
    
    /* Botones estilo terminal */
    .stButton>button {
        background-color: #000000;
        color: #00FF41;
        border: 1px solid #00FF41;
        border-radius: 0px;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #00FF41; color: #000000; }
    
    /* Inputs */
    input { background-color: #0a0a0a !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL ---
st.sidebar.title("📟 OPS_CONTROL_v4")
st.sidebar.markdown("---")

opcion = st.sidebar.selectbox(
    "NIVEL DE ACCESO:",
    ["🖼️ IMAGE_FORENSICS", "🌍 NETWORK_STALKER", "📄 PDF_ANALYSIS", "🎭 ANON_CAMOUFLAGE"]
)

st.sidebar.markdown("---")
st.sidebar.error("ESTADO: MODO OPERACIONES ESPECIALES")

# --- MÓDULO 1: IMÁGENES ---
if opcion == "🖼️ IMAGE_FORENSICS":
    st.title("📂 EXTRACCIÓN DE ADN DIGITAL")
    uploaded_file = st.file_uploader("CARGAR OBJETIVO", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.code(f"HASH_SHA256: {hashlib.sha256(uploaded_file.getvalue()).hexdigest()}")
        st.image(Image.open(uploaded_file), width=500)

# --- MÓDULO 2: GEOLOCALIZADOR ---
elif opcion == "🌍 NETWORK_STALKER":
    st.title("🛰️ RASTREO DE NODOS GLOBALES")
    target = st.text_input("IP_TARGET / DOMAIN:")
    if target:
        res = requests.get(f"http://ip-api.com/json/{target}").json()
        if res["status"] == "success":
            st.map(pd.DataFrame({'lat': [res['lat']], 'lon': [res['lon']]}))
            st.json(res)

# --- MÓDULO 3: PDF ---
elif opcion == "📄 PDF_ANALYSIS":
    st.title("📑 INSPECCIÓN DE DOCUMENTOS SEGURIZADOS")
    pdf_file = st.file_uploader("SUBIR PDF", type=["pdf"])
    if pdf_file:
        reader = pypdf.PdfReader(pdf_file)
        st.write(f"AUTOR DETECTADO: {reader.metadata.author}")
        st.json(reader.metadata)

# --- MÓDULO 4: CAMUFLAJE (ANON_CAMOUFLAGE) ---
elif opcion == "🎭 ANON_CAMOUFLAGE":
    st.title("🎭 MÓDULO DE CAMUFLAJE: USER-AGENT FAKER")
    st.write("Genera identidades digitales falsas para navegar sin ser rastreado.")
    
    dispositivos = {
        "PC Windows (Chrome)": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "iPhone (Safari)": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
        "Linux Workstation (Firefox)": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Android Tablet": "Mozilla/5.0 (Linux; Android 13; SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    seleccion = st.selectbox("ELEGIR DISFRAZ DIGITAL:", list(dispositivos.keys()))
    
    if st.button("GENERAR IDENTIDAD FALSA"):
        ua = dispositivos[seleccion]
        st.subheader("Copia este User-Agent en tu navegador:")
        st.code(ua, language="bash")
        st.success(f"Disfraz de {seleccion} activado.")
        st.info("💡 Tip Hacker: Usa esto en las 'Herramientas de Desarrollador' de tu navegador para simular que eres otro dispositivo.")