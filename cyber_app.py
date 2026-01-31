import streamlit as st
from PIL import Image
from PIL.ExifTags import TAGS
import hashlib
import datetime
import os

# Configuración de estilo "Cyber"
st.set_page_config(page_title="Cyber-Extractor Pro", page_icon="🕵️‍♂️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ff41; }
    .stHeader { color: #00ff41; }
    </style>
    """, unsafe_allow_html=True)

st.title("🕵️‍♂️ Cyber-Extractor: Analizador Forense")
st.write("Sube un archivo para extraer su ADN digital y metadatos ocultos.")

uploaded_file = st.file_uploader("Arrastra aquí tu archivo", type=["jpg", "jpeg", "png", "pdf", "txt"])

if uploaded_file is not None:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📁 Información del Sistema")
        file_details = {
            "Nombre": uploaded_file.name,
            "Tamaño": f"{uploaded_file.size / 1024:.2f} KB",
            "Tipo": uploaded_file.type
        }
        st.json(file_details)
        
        # Generar Huella Digital (Hash SHA-256)
        bytes_data = uploaded_file.getvalue()
        hash_repro = hashlib.sha256(bytes_data).hexdigest()
        st.warning(f"**Huella Digital (SHA-256):** \n\n {hash_repro}")

    with col2:
        st.subheader("🔍 Metadatos Ocultos (EXIF)")
        if uploaded_file.type in ["image/jpeg", "image/png"]:
            try:
                img = Image.open(uploaded_file)
                info = img._getexif()
                if info:
                    exif_data = {}
                    for tag, value in info.items():
                        decoded = TAGS.get(tag, tag)
                        exif_data[decoded] = str(value)
                    st.write(exif_data)
                else:
                    st.info("Este archivo no tiene metadatos EXIF (está 'limpio').")
            except Exception as e:
                st.error("No se pudo leer la metadata de la imagen.")
        else:
            st.info("Sube una imagen JPG para ver datos de cámara y GPS.")

    st.divider()
    st.success("Análisis completado con éxito.")