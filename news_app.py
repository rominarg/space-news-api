import streamlit as st
import requests
from deep_translator import GoogleTranslator

# 1. Configuración visual
st.set_page_config(page_title="Noticias Espaciales", layout="centered")

# Título
st.title("Noticias de la NASA")
st.write("Últimas novedades oficiales")
st.markdown("---")

url = "https://api.spaceflightnewsapi.net/v4/articles/?limit=13&news_site=NASA"
# -------------------

# Botón de carga
if st.button("🔄 Cargar Noticias"):
    
    with st.spinner("Conectando con la base de la NASA..."):
        try:
            # Hacemos la petición
            response = requests.get(url)
            data = response.json()

            # Esta API guarda las noticias dentro de una lista llamada "results"
            if "results" in data:
                noticias = data["results"]
                
                st.success(f"✅ ¡Conexión Exitosa! Se encontraron {len(noticias)} noticias de la NASA.")
                st.markdown("---")
                
                # Inicializamos el traductor
                traductor = GoogleTranslator(source='auto', target='es')

                for noticia in noticias:
                    with st.container():
                        # Título ORIGINAL (Inglés)
                        st.subheader(noticia['title'])
                        
                        col1, col2 = st.columns([1, 2])
                        
                        with col1:
                            if noticia.get('image_url'):
                                st.image(noticia['image_url'], use_container_width=True)
                            else:
                                st.info("Sin imagen")
                        
                        with col2:
                            # Resumen ORIGINAL (Inglés)
                            st.write(noticia['summary'])
                            
                            # --- TRADUCTOR ---
                            with st.expander("🇪🇸 Ver traducción al Español"):
                                title_es = traductor.translate(noticia['title'])
                                summary_es = traductor.translate(noticia['summary'])
                                
                                st.markdown(f"**Título:** {title_es}")
                                st.markdown(f"**Resumen:** {summary_es}")
                            # ---------------------------------------------

                            st.caption(f"Fuente: {noticia['news_site']}")
                            
                            st.link_button("Leer artículo original 🔗", noticia['url'])
                    
                    st.divider()
            else:
                st.error("La API respondió, pero no trajo resultados.")

        except Exception as e:
            st.error(f"Error de conexión: {e}")