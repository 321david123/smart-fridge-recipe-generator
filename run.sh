#!/bin/bash

# Generador Inteligente de Recetas - Script de Inicio Rápido

echo "🍳 Generador Inteligente de Recetas"
echo "===================================="
echo ""

# Verificar si existe el entorno virtual
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Instalar/actualizar dependencias
echo "📥 Instalando dependencias..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Verificar clave API
if [ -z "$OPENAI_API_KEY" ]; then
    echo ""
    echo "⚠️  Advertencia: Variable de entorno OPENAI_API_KEY no configurada"
    echo "Puedes:"
    echo "  1. Configurarla ahora: export OPENAI_API_KEY='tu-clave-aqui'"
    echo "  2. Ingresarla en la barra lateral de la aplicación cuando inicie"
    echo ""
    read -p "Presiona Enter para continuar..."
fi

# Ejecutar la aplicación
echo ""
echo "🚀 Iniciando la aplicación..."
echo "La aplicación se abrirá en tu navegador en http://localhost:8501"
echo ""
streamlit run app.py
