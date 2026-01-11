import streamlit as st
import requests

# 1. Configuración visual
st.set_page_config(page_title="Noticias Espaciales", layout="centered")

# Título
st.title("Noticias del Espacio")
st.write("")
st.markdown("---")

url = "https://api.spaceflightnewsapi.net/v4/articles/?limit=5"

# Botón de carga
if st.button("🔄 Cargar Noticias"):
    
    with st.spinner("Conectando con la base espacial..."):
        try:
            # Hacemos la petición
            response = requests.get(url)
            data = response.json()

            # Esta API guarda las noticias dentro de una lista llamada "results"
            if "results" in data:
                noticias = data["results"]
                
                st.success(f"✅ ¡Conexión Exitosa! Se encontraron {len(noticias)} noticias.")
                st.markdown("---")

                for noticia in noticias:
                    with st.container():
                        # Título
                        st.subheader(noticia['title'])
                        
                        col1, col2 = st.columns([1, 2])
                        
                        with col1:
                            # En esta API la imagen se llama 'image_url'
                            if noticia.get('image_url'):
                                st.image(noticia['image_url'], use_container_width=True)
                            else:
                                st.info("Sin imagen")
                        
                        with col2:
                            # El resumen se llama 'summary'
                            st.write(noticia['summary'])
                            
                            # La fuente se llama 'news_site'
                            st.caption(f"Fuente: {noticia['news_site']}")
                            
                            # El link se llama 'url'
                            st.link_button("Leer artículo original 🔗", noticia['url'])
                    
                    st.divider()
            else:
                st.error("La API respondió, pero no trajo resultados.")

        except Exception as e:
            st.error(f"Error de conexión: {e}")