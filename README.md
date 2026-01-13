# 🚀 Noticias del Espacio — Space News App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://space-news.streamlit.app/)

Aplicación web desarrollada en **Python + Streamlit** que consume una API pública para mostrar las últimas noticias del espacio en tiempo real, filtrando contenido oficial de la NASA.

🔗 **Demo en vivo:** [https://space-news.streamlit.app/](https://space-news.streamlit.app/)

## 🔧 Tecnologías utilizadas

- Python 3
- Streamlit
- Requests
- **Deep Translator** (Nueva funcionalidad de traducción)
- Spaceflight News API

## ✨ Funcionalidades

- Consulta de noticias espaciales de la NASA en tiempo real.
- **Traducción instantánea:** Opción desplegable para traducir títulos y resúmenes de inglés a español.
- Visualización de títulos, imágenes y resúmenes.
- Enlaces directos a la fuente original.
- Manejo de errores de conexión.
- Interfaz simple y responsiva.

## ⚙️ Instalación y Configuración

## 1. Create a virtual environment  
```
python -m venv venv 
```

## 2. Activate the virtual environment (Windows)  

```
.\venv\Scripts\activate
```

## 3. Run the application  

```
streamlit run news_app.py
```

## Install dependencies 

```
pip install -r requirements.txt
```