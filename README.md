# 🍳 Generador Inteligente de Recetas

Una aplicación potenciada por IA que analiza fotos de tu refrigerador o ingredientes y te ayuda a:
- 📸 Identificar ingredientes usando visión por computadora
- 👨‍🍳 Generar recetas creativas basadas en lo que tienes
- 🛒 Sugerir ingredientes adicionales para expandir tus posibilidades culinarias

## Características

- **Carga y Análisis de Imágenes**: Sube fotos de tu refrigerador o ingredientes
- **Reconocimiento con IA Vision**: Usa GPT-4 Vision para identificar alimentos con precisión
- **Generación de Recetas**: Obtén 3 sugerencias de recetas personalizadas con instrucciones paso a paso
- **Sugerencias de Compras**: La IA recomienda ingredientes complementarios para comprar
- **Interfaz Interactiva**: Interfaz web limpia y fácil de usar con Streamlit
- **Resultados Editables**: Ajusta manualmente la lista de ingredientes detectados si es necesario

## Requisitos Previos

- Python 3.8 o superior
- Clave API de OpenAI (con acceso a modelos GPT-4o/Vision)

## 🚀 Instalación y Uso

### Para Usuarios de Windows:

1. **Descarga o clona este proyecto**:
   ```bash
   git clone https://github.com/321david123/smart-fridge-recipe-generator.git
   cd smart-fridge-recipe-generator
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura tu clave API de OpenAI**:
   
   Opción A: Variable de entorno (recomendado):
   ```bash
   set OPENAI_API_KEY=tu-clave-api-aqui
   ```
   
   Opción B: Ingrésala en la barra lateral de la aplicación cuando la ejecutes

4. **Inicia la aplicación**:
   ```bash
   streamlit run app.py
   ```
   
   O usa el script de inicio rápido:
   ```bash
   run.bat
   ```

5. **Abre tu navegador**:
   - La aplicación se abrirá automáticamente en `http://localhost:8501`

---

### Para Usuarios de Mac:

1. **Descarga o clona este proyecto**:
   ```bash
   git clone https://github.com/321david123/smart-fridge-recipe-generator.git
   cd smart-fridge-recipe-generator
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura tu clave API de OpenAI**:
   
   Opción A: Variable de entorno (recomendado):
   ```bash
   export OPENAI_API_KEY='tu-clave-api-aqui'
   ```
   
   Opción B: Ingrésala en la barra lateral de la aplicación cuando la ejecutes

4. **Inicia la aplicación**:
   ```bash
   streamlit run app.py
   ```
   
   O usa el script de inicio rápido:
   ```bash
   ./run.sh
   ```

5. **Abre tu navegador**:
   - La aplicación se abrirá automáticamente en `http://localhost:8501`

---

### Para Usuarios de Linux:

1. **Descarga o clona este proyecto**:
   ```bash
   git clone https://github.com/321david123/smart-fridge-recipe-generator.git
   cd smart-fridge-recipe-generator
   ```

2. **Instala las dependencias**:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Configura tu clave API de OpenAI**:
   
   Opción A: Variable de entorno (recomendado):
   ```bash
   export OPENAI_API_KEY='tu-clave-api-aqui'
   ```
   
   Opción B: Ingrésala en la barra lateral de la aplicación cuando la ejecutes

4. **Inicia la aplicación**:
   ```bash
   streamlit run app.py
   ```
   
   O usa el script de inicio rápido:
   ```bash
   ./run.sh
   ```

5. **Abre tu navegador**:
   - La aplicación se abrirá automáticamente en `http://localhost:8501`

---

## 📖 Cómo Usar la Aplicación

1. **Sube una foto** de tu refrigerador o ingredientes
2. **Haz clic en "Analizar Ingredientes"** para detectar lo que tienes
3. **Revisa y edita** la lista de ingredientes si es necesario
4. **Haz clic en "Generar Recetas"** para obtener ideas de cocina
5. **Haz clic en "Obtener Ideas de Compras"** para sugerencias de ingredientes

## 🔑 Obtener tu Clave API de OpenAI

1. Ve a: https://platform.openai.com/api-keys
2. Inicia sesión o crea una cuenta
3. Haz clic en "Create new secret key"
4. Copia la clave y úsala en la aplicación

**Nota**: Necesitas una cuenta verificada con acceso a GPT-4o Vision. La aplicación cuesta aproximadamente $0.03-0.05 por sesión completa (análisis de imagen + recetas + sugerencias).

## ⚙️ Cómo Funciona

1. **Análisis de Imagen**: La aplicación usa el modelo GPT-4o Vision de OpenAI para analizar tu imagen subida e identificar ingredientes visibles

2. **Generación de Recetas**: Basándose en los ingredientes detectados, la IA genera recetas prácticas que realmente puedes hacer con lo que tienes

3. **Sugerencias Inteligentes**: La IA analiza tu inventario actual y sugiere ingredientes complementarios que desbloquearían muchas más posibilidades de recetas

## 💡 Consejos para Mejores Resultados

- 📸 Toma fotos claras y bien iluminadas
- 🏷️ Asegúrate de que las etiquetas de los ingredientes sean visibles cuando sea posible
- 🔍 Acércate a secciones específicas si tu refrigerador está lleno
- ✏️ Edita la lista de ingredientes para agregar elementos que la IA podría haber pasado por alto

## 🛠️ Tecnologías Utilizadas

- **Streamlit**: Framework de interfaz web
- **OpenAI GPT-4o**: Visión y generación de texto
- **Pillow**: Procesamiento de imágenes
- **Python**: Lenguaje de programación principal

## 💰 Consideraciones de Costo

Esta aplicación usa la API de OpenAI que incurre en costos:
- GPT-4o Vision: ~$0.01-0.02 por análisis de imagen
- GPT-4o Texto: ~$0.005-0.01 por generación de recetas/sugerencias

Una sesión típica (1 imagen + recetas + sugerencias) cuesta aproximadamente $0.03-0.05.

## 🐛 Solución de Problemas

**Error: "Por favor configura tu clave de API de OpenAI"**
- Asegúrate de haber configurado la clave API como variable de entorno o ingrésala en la barra lateral

**El análisis de imagen no funciona**
- Asegúrate de que tu imagen esté en formato PNG, JPG o JPEG
- Verifica que tu clave API de OpenAI tenga acceso a modelos GPT-4o Vision
- Intenta con una imagen más clara o más pequeña

**Las recetas parecen genéricas**
- Edita la lista de ingredientes para ser más específico
- Agrega más detalles sobre cantidades o variedades

## 🌟 Mejoras Futuras

- [ ] Soporte para múltiples imágenes a la vez
- [ ] Filtros de restricciones dietéticas (vegetariano, vegano, sin gluten, etc.)
- [ ] Información de calorías y nutrición
- [ ] Guardar recetas favoritas
- [ ] Exportar listas de compras
- [ ] Integración con servicios de entrega de comestibles

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.

## 🤝 Contribuciones

¡Siéntete libre de hacer fork de este proyecto y enviar pull requests con mejoras!

---

Hecho con ❤️ usando Python, Streamlit y OpenAI
