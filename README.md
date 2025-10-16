# 🎓 Student Life - Tu Asistente Personal Estudiantil

Una aplicación de escritorio moderna potenciada por IA que ayuda a estudiantes a:
- 📊 Registrar su bienestar diario (sueño, comida, ejercicio, estrés)
- 🍳 Generar recetas inteligentes desde fotos de su refrigerador
- 🧠 Obtener ayuda académica, motivación y consejos de productividad

## ✨ Características

### 1. 📊 Registro Diario de Bienestar
- Registro de horas de sueño
- Control de comidas y vasos de agua
- Seguimiento de ejercicio
- Medición de niveles de estrés
- Horas de estudio
- Notas personales del día

### 2. 🍳 Generador Inteligente de Recetas
- Sube fotos de tu refrigerador
- IA identifica ingredientes automáticamente
- Genera recetas fáciles para estudiantes
- Todo automático con streaming en tiempo real

### 3. 🧠 Asistente de Estudio
- Técnicas de estudio efectivas
- Mensajes motivacionales
- Manejo de estrés académico
- Consejos de organización y productividad
- Pregunta lo que quieras al asistente IA

## 🚀 Instalación y Uso

### Requisitos Previos

- Python 3.8 o superior
- Clave API de OpenAI (con acceso a modelos GPT-4o/Vision)

---

### Para Windows:

1. **Clona o descarga el proyecto**:
   ```bash
   git clone https://github.com/321david123/smart-fridge-recipe-generator.git
   cd smart-fridge-recipe-generator
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura tu clave API de OpenAI**:
   
   Crea un archivo `.env` en la carpeta del proyecto:
   ```
   OPENAI_API_KEY=tu-clave-api-aqui
   ```

4. **Ejecuta la aplicación**:
   ```bash
   python app_estudiante.py
   ```

---

### Para Mac:

1. **Clona o descarga el proyecto**:
   ```bash
   git clone https://github.com/321david123/smart-fridge-recipe-generator.git
   cd smart-fridge-recipe-generator
   ```

2. **Instala las dependencias**:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Configura tu clave API de OpenAI**:
   
   Crea un archivo `.env` en la carpeta del proyecto:
   ```bash
   echo "OPENAI_API_KEY=tu-clave-api-aqui" > .env
   ```

4. **Ejecuta la aplicación**:
   ```bash
   python3 app_estudiante.py
   ```

---

### Para Linux:

1. **Clona o descarga el proyecto**:
   ```bash
   git clone https://github.com/321david123/smart-fridge-recipe-generator.git
   cd smart-fridge-recipe-generator
   ```

2. **Instala las dependencias**:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Configura tu clave API de OpenAI**:
   
   Crea un archivo `.env` en la carpeta del proyecto:
   ```bash
   echo "OPENAI_API_KEY=tu-clave-api-aqui" > .env
   ```

4. **Ejecuta la aplicación**:
   ```bash
   python3 app_estudiante.py
   ```

---

## 🎮 Cómo Usar la Aplicación

### Primera Vez:
1. **Ingresa tu nombre** en la pantalla de bienvenida
2. Verás el **dashboard principal** con 3 módulos

### Módulo 1: Registro Diario 📊
1. Haz clic en "📊 Registro Diario"
2. Llena los campos:
   - Horas de sueño
   - Comidas del día
   - Vasos de agua
   - Minutos de ejercicio
   - Nivel de estrés (1-10)
   - Horas de estudio
   - Notas del día
3. Haz clic en "💾 Guardar Registro"
4. ¡Tus datos se guardan localmente!

### Módulo 2: Generador de Recetas 🍳
1. Haz clic en "🍳 Recetas Inteligentes"
2. Haz clic en "📸 Subir Foto del Refrigerador"
3. Selecciona una imagen
4. **Automáticamente:**
   - La IA analiza los ingredientes
   - Genera recetas deliciosas
   - Todo en tiempo real

### Módulo 3: Asistente de Estudio 🧠
1. Haz clic en "🧠 Asistente de Estudio"
2. Elige una opción:
   - 📚 Técnicas de Estudio
   - 💪 Motivación y Ánimo
   - 😌 Manejo de Estrés
   - 📅 Organización y Productividad
   - 💬 Hacer una Pregunta
3. ¡Recibe consejos personalizados de IA!

## 🔑 Obtener tu Clave API de OpenAI

1. Ve a: https://platform.openai.com/api-keys
2. Inicia sesión o crea una cuenta
3. Haz clic en "Create new secret key"
4. Copia la clave y agrégala al archivo `.env`

**Nota**: Necesitas una cuenta verificada con acceso a GPT-4o Vision.

## 💾 Almacenamiento de Datos

- Todos tus datos se guardan **localmente** en `datos_estudiante.json`
- **No se envía información personal** a ningún servidor
- Solo las imágenes y preguntas se envían a OpenAI para análisis
- Puedes borrar `datos_estudiante.json` para empezar de nuevo

## 🛠️ Tecnologías Utilizadas

- **CustomTkinter**: Interfaz moderna y hermosa
- **OpenAI GPT-4o**: IA para análisis de imágenes y generación de contenido
- **Pillow**: Procesamiento de imágenes
- **Python 3**: Lenguaje de programación

## 💰 Consideraciones de Costo

Esta aplicación usa la API de OpenAI que tiene los siguientes costos aproximados:
- Análisis de imagen: ~$0.01-0.02 por foto
- Generación de recetas: ~$0.005-0.01
- Consejos del asistente: ~$0.003-0.008

Uso típico: $0.02-0.05 por sesión completa.

## 🐛 Solución de Problemas

**La aplicación no abre**
- Verifica que Python esté instalado: `python --version`
- Reinstala dependencias: `pip install -r requirements.txt`

**Error de clave API**
- Verifica que el archivo `.env` exista en la carpeta del proyecto
- Asegúrate de que la clave API sea válida
- Formato correcto: `OPENAI_API_KEY=sk-...`

**Error al analizar imágenes**
- Verifica que tu cuenta de OpenAI tenga acceso a GPT-4o Vision
- Usa imágenes en formato PNG, JPG o JPEG
- Intenta con una imagen más pequeña

**La interfaz se ve mal**
- Actualiza CustomTkinter: `pip install --upgrade customtkinter`
- Cierra y vuelve a abrir la aplicación

## 🌟 Características Próximamente

- [ ] Gráficas de progreso y estadísticas
- [ ] Recordatorios y alarmas
- [ ] Modo claro/oscuro personalizable
- [ ] Exportar datos a PDF
- [ ] Temporizador Pomodoro integrado
- [ ] Calendario de tareas

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.

## 🤝 Contribuciones

¡Siéntete libre de hacer fork de este proyecto y enviar pull requests con mejoras!

---

## 🎨 Capturas de Pantalla

La aplicación cuenta con:
- ✨ Interfaz moderna con tema oscuro
- 🎯 Diseño intuitivo y fácil de usar
- 🚀 Animaciones suaves
- 📱 Organización clara por módulos
- 💜 Colores vibrantes y atractivos

---

**Hecho con ❤️ para estudiantes que quieren una vida más equilibrada**

Desarrollado usando Python, CustomTkinter y OpenAI GPT-4o
