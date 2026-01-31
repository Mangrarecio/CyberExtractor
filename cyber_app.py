import streamlit as st
from PIL import Image
import hashlib
import requests
import pandas as pd

# Configuración de la página (Modo Hacker)
st.set_page_config(page_title="Cyber-Extractor Suite", page_icon="🕵️‍♂️", layout="wide")
st.markdown("<style>.main { background-color: #0e1117; color: #00ff41; }</style>", unsafe_allow_html=True)

# --- BARRA LATERAL (Menú de Navegación) ---
st.sidebar.title("🕵️ Cyber-Menu")
opcion = st.sidebar.radio(
    "Selecciona una herramienta:",
    ["🖼️ Extractor de Metadatos", "🌍 Geolocalizador de IP/Servidores"]
)

st.sidebar.info("Versión 2.0 - Suite de Ciberseguridad")

# --- HERRAMIENTA 1: EXTRACTOR DE METADATOS (Tu herramienta original) ---
if opcion == "🖼️ Extractor de Metadatos":
    st.title("🖼️ Extractor de ADN Digital")
    st.write("Sube una imagen para analizar sus secretos técnicos.")
    
    uploaded_file = st.file_uploader("Arrastra tu imagen aquí", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        sha256_hash = hashlib.sha256(bytes_data).hexdigest()
        
        st.subheader("🔍 ADN Digital (Hash)")
        st.code(f"SHA-256: {sha256_hash}")
        
        img = Image.open(uploaded_file)
        st.image(img, caption="Imagen analizada", width=400)
        
        with st.expander("Ver Metadatos EXIF"):
            info = img.getexif()
            if info:
                st.write(dict(info.items()))
            else:
                st.write("No se encontraron metadatos ocultos.")

# --- HERRAMIENTA 2: GEOLOCALIZADOR DE SERVIDORES (La nueva opción potente) ---
elif opcion == "🌍 Geolocalizador de IP/Servidores":
    st.title("🌍 IP Stalker: Localizador Global")
    st.write("Rastrea la ubicación física de una dirección IP o un dominio (ej: google.com).")

    target = st.text_input("Introduce IP o dominio a rastrear:", placeholder="8.8.8.8 o google.com")

    if target:
        try:
            # Consultar API de geolocalización (gratuita para pruebas)
            response = requests.get(f"http://ip-api.com/json/{target}").json()
            
            if response["status"] == "success":
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📍 Datos de Ubicación")
                    st.write(f"**País:** {response['country']} ({response['countryCode']})")
                    st.write(f"**Ciudad:** {response['city']}, {response['regionName']}")
                    st.write(f"**Proveedor (ISP):** {response['isp']}")
                    st.write(f"**Coordenadas:** {response['lat']}, {response['lon']}")
                
                with col2:
                    st.subheader("🗺️ Mapa del Servidor")
                    # Crear mapa con los datos
                    map_data = pd.DataFrame({'lat': [response['lat']], 'lon': [response['lon']]})
                    st.map(map_data)
                    
            else:
                st.error("No se pudo localizar ese objetivo. Verifica la dirección.")
        except Exception as e:
            st.error(f"Error en el rastreo: {e}")