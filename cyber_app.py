import streamlit as st
from PIL import Image, ExifTags
import hashlib
import requests
import pandas as pd
import pypdf
import random

# --- CONFIGURACIÓN ESTILO RED OPS (ROJO NEÓN) ---
st.set_page_config(page_title="RED_OPS_SUITE_v6", page_icon="🚨", layout="wide")

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
st.sidebar.title("🚨 RED_TERMINAL_v6")
opcion = st.sidebar.selectbox("SELECCIONAR MÓDULO:", 
    ["🕵️ OSINT_USER_FINDER", "🛰️ GPS_DEEP_TRACKER", "🔍 WHOIS_DETECTIVE", "🖼️ IMAGE_ANALYSIS", "🌍 NETWORK_STALKER", "🎭 ANON_CAMOUFLAGE"])

# --- MÓDULO 6: OSINT USER FINDER (NUEVO) ---
if opcion == "🕵️ OSINT_USER_FINDER":
    st.title("🕵️ OSINT_USER_FINDER: RASTREO DE IDENTIDAD")
    st.write("Investiga la presencia de un nombre de usuario en múltiples plataformas.")
    username = st.text_input("INTRODUCIR NOMBRE DE USUARIO (ej: hackerman2024):")
    if username:
        redes = {
            "Instagram": f"https://www.instagram.com/{username}",
            "Twitter/X": f"https://twitter.com/{username}",
            "GitHub": f"https://github.com/{username}",
            "Reddit": f"https://www.reddit.com/user/{username}",
            "YouTube": f"https://www.youtube.com/@{username}",
            "TikTok": f"https://www.tiktok.com/@{username}"
        }
        st.subheader(f"AUDITORÍA DE HUELLA DIGITAL PARA: {username}")
        for nombre, url in redes.items():
            st.markdown(f"[🔍 RASTREAR EN {nombre}]({url})")

# --- MÓDULO: GPS DEEP TRACKER ---
elif opcion == "🛰️ GPS_DEEP_TRACKER":
    st.title("🛰️ GPS_DEEP_TRACKER: EXTRACCIÓN SATELITAL")
    file = st.file_uploader("CARGAR IMAGEN PARA GEOLOCALIZAR", type=["jpg", "jpeg"])
    if file:
        img = Image.open(file)
        gps_data = get_gps_data(img)
        if gps_data and 'GPSLatitude' in gps_data:
            lat = convert_to_degrees(gps_data['GPSLatitude'])
            if gps_data.get('GPSLatitudeRef') == 'S': lat = -lat
            lon = convert_to_degrees(gps_data['GPSLongitude'])
            if gps_data.get('GPSLongitudeRef') == 'W': lon = -lon
            st.success(f"COORDENADAS DETECTADAS: {lat}, {lon}")
            st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}))
        else:
            st.error("EL OBJETIVO NO CONTIENE COORDENADAS GPS.")

# --- MÓDULO: WHOIS DETECTIVE ---
elif opcion == "🔍 WHOIS_DETECTIVE":
    st.title("🔍 WHOIS_DETECTIVE: DNI DE DOMINIOS")
    domain = st.text_input("DOMINIO A INVESTIGAR:")
    if domain:
        res = requests.get(f"https://rdap.org/domain/{domain}").json()
        st.json(res)

# --- MÓDULO: IMAGE ANALYSIS ---
elif opcion == "🖼️ IMAGE_ANALYSIS":
    st.title("🖼️ ANÁLISIS DE ADN DIGITAL")
    file = st.file_uploader("SUBIR ARCHIVO", type=["jpg", "png", "jpeg"])
    if file:
        st.code(f"HASH_SHA256: {hashlib.sha256(file.getvalue()).hexdigest()}")
        st.image(Image.open(file), width=400)

# --- MÓDULO: NETWORK STALKER ---
elif opcion == "🌍 NETWORK_STALKER":
    st.title("🌍 NETWORK_STALKER: RASTREO DE NODOS")
    target = st.text_input("IP_TARGET:")
    if target:
        res = requests.get(f"http://ip-api.com/json/{target}").json()
        if res["status"] == "success":
            st.map(pd.DataFrame({'lat': [res['lat']], 'lon': [res['lon']]}))
            st.json(res)

# --- MÓDULO: CAMUFLAJE ---
elif opcion == "🎭 ANON_CAMOUFLAGE":
    st.title("🎭 MÓDULO DE CAMUFLAJE")
    if st.button("GENERAR IDENTIDAD FANTASMA"):
        st.code("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")