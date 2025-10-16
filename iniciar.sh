#!/bin/bash

# Student Life - Script de Inicio

echo "🎓 Student Life - Tu Asistente Personal"
echo "========================================"
echo ""

# Verificar si existe el archivo .env
if [ ! -f ".env" ]; then
    echo "⚠️  No se encontró el archivo .env"
    echo ""
    echo "Por favor crea un archivo .env con tu clave de OpenAI:"
    echo "OPENAI_API_KEY=tu-clave-aqui"
    echo ""
    read -p "Presiona Enter cuando hayas creado el archivo .env..."
fi

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    exit 1
fi

echo "📦 Instalando dependencias..."
pip3 install -q -r requirements.txt

echo ""
echo "🚀 Iniciando Student Life..."
echo ""

python3 app_estudiante.py

