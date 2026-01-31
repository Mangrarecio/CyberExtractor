import streamlit as st
from PIL import Image, ExifTags
import hashlib
import requests
import pandas as pd
import re
import yt_dlp
import os

# --- CONFIGURACIÓN RED OPS v9 ---
st.set_page_config(page_title="RED_OPS_v9_MEDIA", page_icon="📥", layout="wide")

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
st.sidebar.title("🚨 RED_TERMINAL_v9")
cat = st.sidebar.radio("NIVEL DE ACCESO:", ["🎯 INTEL_GATHERING", "🕵️ DEEP_RECON", "📄 DATA_ANALYSIS", "📥 MEDIA_ACQUISITION"])

# --- CATEGORÍA 4: MEDIA_ACQUISITION (NUEVA) ---
if cat == "📥 MEDIA_ACQUISITION":
    opcion = st.sidebar.selectbox("MÓDULO:", ["VIDEO_DOWNLOADER", "EXTRACT_AUDIO"])
    
    if opcion == "VIDEO_DOWNLOADER":
        st.title("📥 VIDEO_DOWNLOADER: EXTRACCIÓN DE EVIDENCIA")
        st.write("Introduce la URL del video (YouTube, Twitter, etc.) para generar el enlace de descarga.")
        
        video_url = st.text_input("URL DEL VIDEO:")
        
        if st.button("ANALIZAR VIDEO"):
            if video_url:
                try:
                    with st.spinner("Buscando flujos de datos..."):
                        ydl_opts = {'format': 'best', 'quiet': True}
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            info = ydl.extract_info(video_url, download=False)
                            video_title = info.get('title', 'video_operativo')
                            direct_url = info.get('url', None)
                            
                            st.success(f"OBJETIVO DETECTADO: {video_title}")
                            st.video(video_url)
                            
                            st.markdown(f"### [🔗 CLIC AQUÍ PARA DESCARGAR VIDEO]( {direct_url} )")
                            st.info("Nota: Haz clic derecho en el link y selecciona 'Guardar como' si no inicia solo.")
                except Exception as e:
                    st.error(f"Error en la extracción: {str(e)}")
            else:
                st.warning("Introduce una URL válida.")

# (Aquí mantienes el resto de las categorías: INTEL_GATHERING, DEEP_RECON, DATA_ANALYSIS con sus respectivos if/elif)
# Nota: Por brevedad no repito todo el código anterior, pero asegúrate de pegarlo debajo.