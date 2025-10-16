import streamlit as st
import base64
from io import BytesIO
from PIL import Image
import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv()

# Configuración de la página
st.set_page_config(
    page_title="Generador Inteligente de Recetas",
    page_icon="🍳",
    layout="wide"
)

# Inicializar cliente de OpenAI
@st.cache_resource
def obtener_cliente_openai():
    clave_api = os.getenv("OPENAI_API_KEY")
    if not clave_api:
        st.error("⚠️ Por favor configura tu clave de API de OpenAI (OPENAI_API_KEY)")
        st.stop()
    return OpenAI(api_key=clave_api)

def codificar_imagen(imagen):
    """Convertir imagen PIL a cadena base64"""
    buffer = BytesIO()
    imagen.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode('utf-8')

def analizar_imagen_para_ingredientes(cliente, imagen):
    """Usar GPT-4 Vision para identificar ingredientes en la imagen"""
    imagen_base64 = codificar_imagen(imagen)
    
    try:
        respuesta = cliente.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """Analiza esta imagen de un refrigerador o alimentos. 
                            Lista todos los ingredientes y alimentos que puedas identificar.
                            Formatea tu respuesta como una lista simple con viñetas con solo los nombres de los ingredientes.
                            Sé específico pero conciso (ej: 'pechuga de pollo', 'pimiento rojo', 'leche entera').
                            Solo lista elementos que puedas identificar claramente."""
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{imagen_base64}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=500
        )
        return respuesta.choices[0].message.content
    except Exception as error:
        st.error(f"Error al analizar imagen: {str(error)}")
        return None

def generar_recetas(cliente, ingredientes):
    """Generar recetas basadas en ingredientes disponibles"""
    try:
        respuesta = cliente.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un asistente chef útil que crea recetas prácticas y deliciosas."
                },
                {
                    "role": "user",
                    "content": f"""Basándote en estos ingredientes disponibles:
                    
{ingredientes}

Por favor sugiere 3 recetas que se puedan hacer con estos ingredientes. Para cada receta:
1. Dale un nombre atractivo
2. Lista los ingredientes necesarios (de la lista disponible)
3. Proporciona instrucciones breves paso a paso
4. Menciona el tiempo aproximado de cocción

Formatea cada receta claramente con encabezados y hazla fácil de seguir."""
                }
            ],
            max_tokens=1500
        )
        return respuesta.choices[0].message.content
    except Exception as error:
        st.error(f"Error al generar recetas: {str(error)}")
        return None

def sugerir_ingredientes_adicionales(cliente, ingredientes_actuales):
    """Sugerir ingredientes para comprar para más variedad de recetas"""
    try:
        respuesta = cliente.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un asesor culinario útil."
                },
                {
                    "role": "user",
                    "content": f"""Basándote en estos ingredientes actuales:
                    
{ingredientes_actuales}

Sugiere 5-7 ingredientes adicionales que:
1. Complementen lo que ya está disponible
2. Permitan muchas más posibilidades de recetas
3. Sean prácticos y de uso común
4. Tengan buena vida útil

Para cada sugerencia, explica brevemente (en 1 oración) por qué es útil."""
                }
            ],
            max_tokens=800
        )
        return respuesta.choices[0].message.content
    except Exception as error:
        st.error(f"Error al sugerir ingredientes: {str(error)}")
        return None

# Aplicación principal
def main():
    # Encabezado
    st.title("🍳 Generador Inteligente de Recetas")
    st.markdown("""
    Sube una foto de tu refrigerador o ingredientes, y deja que la IA te ayude a:
    - 📸 Identificar qué ingredientes tienes
    - 👨‍🍳 Generar recetas deliciosas que puedes hacer
    - 🛒 Sugerir qué comprar para aún más recetas
    """)
    
    # Barra lateral para configuración
    with st.sidebar:
        st.header("⚙️ Configuración")
        if not os.getenv("OPENAI_API_KEY"):
            clave_api = st.text_input("Clave API de OpenAI", type="password")
            if clave_api:
                os.environ["OPENAI_API_KEY"] = clave_api
        
        st.markdown("---")
        st.markdown("""
        ### 💡 Consejos
        - Toma una foto clara de tu refrigerador o ingredientes
        - Asegúrate de que los artículos sean visibles y estén bien iluminados
        - También puedes subir fotos existentes
        """)
    
    # Inicializar cliente
    cliente = obtener_cliente_openai()
    
    # Cargador de archivos
    st.header("📸 Sube la Foto de tu Refrigerador")
    archivo_subido = st.file_uploader(
        "Elige una imagen...", 
        type=['png', 'jpg', 'jpeg'],
        help="Sube una foto de tu refrigerador o ingredientes"
    )
    
    if archivo_subido is not None:
        # Mostrar la imagen subida
        imagen = Image.open(archivo_subido)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Tu Imagen")
            st.image(imagen, use_column_width=True)
        
        with col2:
            st.subheader("🔍 Análisis")
            
            # Botón para analizar
            if st.button("🔍 Analizar Ingredientes", type="primary"):
                with st.spinner("Analizando tus ingredientes..."):
                    ingredientes = analizar_imagen_para_ingredientes(cliente, imagen)
                    
                    if ingredientes:
                        st.session_state.ingredientes = ingredientes
                        st.success("✅ ¡Análisis completo!")
        
        # Mostrar ingredientes si fueron analizados
        if 'ingredientes' in st.session_state:
            st.markdown("---")
            st.header("🥗 Ingredientes Detectados")
            st.markdown(st.session_state.ingredientes)
            
            # Permitir edición manual
            with st.expander("✏️ Editar Lista de Ingredientes"):
                ingredientes_editados = st.text_area(
                    "Puedes modificar la lista de ingredientes:",
                    value=st.session_state.ingredientes,
                    height=150
                )
                if st.button("Actualizar Ingredientes"):
                    st.session_state.ingredientes = ingredientes_editados
                    st.success("✅ ¡Ingredientes actualizados!")
                    st.rerun()
            
            # Dos columnas para recetas y sugerencias
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.markdown("---")
                st.header("👨‍🍳 Sugerencias de Recetas")
                if st.button("Generar Recetas", type="primary"):
                    with st.spinner("Creando recetas deliciosas para ti..."):
                        recetas = generar_recetas(cliente, st.session_state.ingredientes)
                        if recetas:
                            st.session_state.recetas = recetas
            
            with col2:
                st.markdown("---")
                st.header("🛒 Sugerencias de Compras")
                if st.button("Obtener Ideas de Compras", type="primary"):
                    with st.spinner("Encontrando excelentes sugerencias de ingredientes..."):
                        sugerencias = sugerir_ingredientes_adicionales(cliente, st.session_state.ingredientes)
                        if sugerencias:
                            st.session_state.sugerencias = sugerencias
            
            # Mostrar resultados
            if 'recetas' in st.session_state:
                st.markdown("---")
                st.subheader("📖 Tus Recetas")
                st.markdown(st.session_state.recetas)
            
            if 'sugerencias' in st.session_state:
                st.markdown("---")
                st.subheader("💡 Ingredientes Sugeridos para Comprar")
                st.markdown(st.session_state.sugerencias)

if __name__ == "__main__":
    main()
