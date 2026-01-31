import streamlit as st
from PIL import Image, ExifTags
import hashlib
import requests
import pandas as pd
import pypdf
import random

# --- CONFIGURACIÓN ESTILO RED OPS (ROJO) ---
st.set_page_config(page_title="RED_OPS_SUITE", page_icon="🚨", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stApp { background-color: #000000; }
    /* Texto en Rojo Neón */
    h1, h2, h3, p, span, label { color: #FF0000 !important; font-family: 'Courier New', monospace !important; text-shadow: 0 0 5px #ff0000; }
    
    [data-testid="stSidebar"] { background-color: #0a0000 !important; border-right: 1px solid #FF0000; }
    [data-testid="stSidebar"] * { color: #FF0000 !important; }
    
    .stButton>button {
        background-color: #000000; color: #FF0000; border: 1px solid #FF0000;
        border-radius: 0px; width: 100%;
    }
    .stButton>button:hover { background-color: #FF0000; color: #000000; box-shadow: 0 0 15px #ff0000; }
    
    input { background-color: #0a0a0a !important; color: #FF0000 !important; border: 1px solid #FF0000 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNCIONES AUXILIARES ---
def get_gps_data(img):
    exif_data = img._getexif()
    if not exif_data: return None
    gps_info = {}
    for tag, value in exif_data.items():
        decoded = ExifTags.TAGS.get(tag, tag)
        if decoded == "GPSInfo":
            for t in value:
                sub_tag = ExifTags.GPSTAGS.get(t, t)
                gps_info[sub_tag] = value[t]
    return gps_info

def convert_to_degrees(value):
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)

# --- BARRA LATERAL ---
st.sidebar.title("🚨 RED_TERMINAL_v5")
opcion = st.sidebar.selectbox("SELECCIONAR MÓDULO:", 
    ["🛰️ GPS_DEEP_TRACKER", "🔍 WHOIS_DETECTIVE", "🖼️ IMAGE_ANALYSIS", "🌍 NETWORK_STALKER", "🎭 ANON_CAMOUFLAGE"])

# --- MÓDULO: GPS DEEP TRACKER ---
if opcion == "🛰️ GPS_DEEP_TRACKER":
    st.title("🛰️ GPS_DEEP_TRACKER: EXTRACCIÓN SATELITAL")
    file = st.file_uploader("CARGAR IMAGEN PARA GEOLOCALIZAR", type=["jpg", "jpeg"])
    if file:
        img = Image.open(file)
        gps_data = get_gps_data(img)
        if gps_data and 'GPSLatitude' in gps_data:
            lat = convert_to_degrees(gps_data['GPSLatitude'])
            if gps_data['GPSLatitudeRef'] == 'S': lat = -lat
            lon = convert_to_degrees(gps_data['GPSLongitude'])
            if gps_data['GPSLongitudeRef'] == 'W': lon = -lon
            
            st.success(f"COORDENADAS DETECTADAS: {lat}, {lon}")
            st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}))
        else:
            st.error("EL OBJETIVO NO CONTIENE COORDENADAS GPS INTEGRADAS.")

# --- MÓDULO: WHOIS DETECTIVE ---
elif opcion == "🔍 WHOIS_DETECTIVE":
    st.title("🔍 WHOIS_DETECTIVE: DNI DE DOMINIOS")
    domain = st.text_input("INTRODUCIR DOMINIO (ej: bbc.com):")
    if domain:
        # Usamos una API de Whois gratuita para el ejemplo
        res = requests.get(f"https://rdap.org/domain/{domain}").json()
        st.subheader(f"REGISTRO TÉCNICO DE {domain}")
        st.json(res)

# --- MÓDULO: CAMUFLAJE ---
elif opcion == "🎭 ANON_CAMOUFLAGE":
    st.title("🎭 MÓDULO DE CAMUFLAJE")
    if st.button("GENERAR IDENTIDAD FANTASMA"):
        st.code("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")

# (Aquí siguen los otros módulos que ya teníamos...)
elif opcion == "🖼️ IMAGE_ANALYSIS":
    st.title("🖼️ ANÁLISIS DE IMAGEN")
    # ... código anterior ...