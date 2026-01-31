import streamlit as st
from PIL import Image
import hashlib
import requests
import pandas as pd
import pypdf  # Nueva librería para PDFs

# Configuración profesional
st.set_page_config(page_title="Cyber-Extractor Suite v3", page_icon="🕵️‍♂️", layout="wide")
st.markdown("<style>.main { background-color: #0e1117; color: #00ff41; font-family: 'Courier New', Courier, monospace; }</style>", unsafe_allow_html=True)

# --- BARRA LATERAL ---
st.sidebar.title("🕵️ Cyber-Menu")
opcion = st.sidebar.radio(
    "Selecciona una herramienta:",
    ["🖼️ Extractor de Imágenes", "🌍 Geolocalizador IP", "📄 PDF Inspector"]
)

# --- HERRAMIENTA 1: IMÁGENES ---
if opcion == "🖼️ Extractor de Imágenes":
    st.title("🖼️ Análisis de ADN en Imágenes")
    uploaded_file = st.file_uploader("Sube una imagen (JPG/PNG)", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.code(f"HASH SHA-256: {hashlib.sha256(uploaded_file.getvalue()).hexdigest()}")
        img = Image.open(uploaded_file)
        st.image(img, width=400)
        with st.expander("Metadatos EXIF"):
            st.write(img.getexif() if img.getexif() else "Sin metadatos.")

# --- HERRAMIENTA 2: GEOLOCALIZADOR ---
elif opcion == "🌍 Geolocalizador IP":
    st.title("🌍 IP Stalker: Rastreo Global")
    target = st.text_input("IP o Dominio (ej: nasa.gov):")
    if target:
        res = requests.get(f"http://ip-api.com/json/{target}").json()
        if res["status"] == "success":
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**País:** {res['country']} | **ISP:** {res['isp']}")
                st.write(f"**Ciudad:** {res['city']}")
            with col2:
                st.map(pd.DataFrame({'lat': [res['lat']], 'lon': [res['lon']]}))

# --- HERRAMIENTA 3: PDF INSPECTOR (La nueva joya) ---
elif opcion == "📄 PDF Inspector":
    st.title("📄 PDF Forensics: Inspector de Documentos")
    st.write("Extrae la identidad oculta de cualquier archivo PDF.")
    
    pdf_file = st.file_uploader("Sube un archivo PDF", type=["pdf"])
    
    if pdf_file:
        try:
            reader = pypdf.PdfReader(pdf_file)
            meta = reader.metadata
            
            st.subheader("🕵️ Datos del Autor y Sistema")
            col1, col2 = st.columns(2)
            
            with col1:
                st.info(f"**Autor:** {meta.author if meta.author else 'Anónimo'}")
                st.info(f"**Creador:** {meta.creator if meta.creator else 'Desconocido'}")
                st.info(f"**Software:** {meta.producer if meta.producer else 'No especificado'}")
            
            with col2:
                st.warning(f"**Páginas:** {len(reader.pages)}")
                st.warning(f"**Título:** {meta.title if meta.title else 'Sin título'}")
                st.warning(f"**Asunto:** {meta.subject if meta.subject else 'No definido'}")

            with st.expander("Ver cronología completa (Fechas Técnicas)"):
                st.json(meta)
                
        except Exception as e:
            st.error("No se pudo leer el PDF. Puede que esté protegido o dañado.")