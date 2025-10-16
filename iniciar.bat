@echo off
REM Student Life - Script de Inicio para Windows

echo 🎓 Student Life - Tu Asistente Personal
echo ========================================
echo.

REM Verificar si existe el archivo .env
if not exist ".env" (
    echo ⚠️  No se encontró el archivo .env
    echo.
    echo Por favor crea un archivo .env con tu clave de OpenAI:
    echo OPENAI_API_KEY=tu-clave-aqui
    echo.
    pause
)

echo 📦 Instalando dependencias...
pip install -q -r requirements.txt

echo.
echo 🚀 Iniciando Student Life...
echo.

python app_estudiante.py

