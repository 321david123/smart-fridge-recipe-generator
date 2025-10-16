@echo off
REM Generador Inteligente de Recetas - Script de Inicio Rápido para Windows

echo 🍳 Generador Inteligente de Recetas
echo ====================================
echo.

REM Verificar si existe el entorno virtual
if not exist "venv" (
    echo 📦 Creando entorno virtual...
    python -m venv venv
)

REM Activar entorno virtual
echo 🔧 Activando entorno virtual...
call venv\Scripts\activate.bat

REM Instalar/actualizar dependencias
echo 📥 Instalando dependencias...
pip install -q --upgrade pip
pip install -q -r requirements.txt

REM Verificar clave API
if "%OPENAI_API_KEY%"=="" (
    echo.
    echo ⚠️  Advertencia: Variable de entorno OPENAI_API_KEY no configurada
    echo Puedes:
    echo   1. Configurarla ahora: set OPENAI_API_KEY=tu-clave-aqui
    echo   2. Ingresarla en la barra lateral de la aplicacion cuando inicie
    echo.
    pause
)

REM Ejecutar la aplicación
echo.
echo 🚀 Iniciando la aplicacion...
echo La aplicacion se abrira en tu navegador en http://localhost:8501
echo.
streamlit run app.py
