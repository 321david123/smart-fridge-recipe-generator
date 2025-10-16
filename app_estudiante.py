import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import json
import os
from datetime import datetime, date
from openai import OpenAI
from dotenv import load_dotenv
import base64
from io import BytesIO
import threading

# Cargar variables de entorno
load_dotenv()

# Configuración de CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AplicacionEstudiante(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.title("🎓 Student Life - Tu Asistente Personal")
        self.geometry("1200x800")
        
        # Variables
        self.nombre_usuario = None
        self.datos_usuario = self.cargar_datos()
        self.cliente_openai = None
        
        # Mostrar pantalla de login
        self.mostrar_login()
    
    def cargar_datos(self):
        """Cargar datos guardados del usuario"""
        if os.path.exists("datos_estudiante.json"):
            with open("datos_estudiante.json", "r", encoding="utf-8") as f:
                return json.load(f)
        return {}
    
    def guardar_datos(self):
        """Guardar datos del usuario"""
        with open("datos_estudiante.json", "w", encoding="utf-8") as f:
            json.dump(self.datos_usuario, f, indent=2, ensure_ascii=False)
    
    def mostrar_login(self):
        """Pantalla de login inicial"""
        # Limpiar ventana
        for widget in self.winfo_children():
            widget.destroy()
        
        # Frame principal
        login_frame = ctk.CTkFrame(self, corner_radius=20)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Título
        titulo = ctk.CTkLabel(
            login_frame,
            text="🎓 Student Life",
            font=ctk.CTkFont(size=40, weight="bold")
        )
        titulo.pack(pady=(40, 10), padx=60)
        
        subtitulo = ctk.CTkLabel(
            login_frame,
            text="Tu asistente personal para una vida estudiantil equilibrada",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitulo.pack(pady=(0, 30), padx=60)
        
        # Input de nombre
        label_nombre = ctk.CTkLabel(
            login_frame,
            text="¿Cómo te llamas?",
            font=ctk.CTkFont(size=16)
        )
        label_nombre.pack(pady=(20, 10))
        
        self.entry_nombre = ctk.CTkEntry(
            login_frame,
            placeholder_text="Escribe tu nombre...",
            width=300,
            height=40,
            font=ctk.CTkFont(size=14)
        )
        self.entry_nombre.pack(pady=10, padx=60)
        
        # Botón de entrada
        btn_entrar = ctk.CTkButton(
            login_frame,
            text="Entrar",
            command=self.iniciar_sesion,
            width=200,
            height=40,
            font=ctk.CTkFont(size=16, weight="bold"),
            corner_radius=10
        )
        btn_entrar.pack(pady=(20, 40), padx=60)
        
        # Bind Enter key
        self.entry_nombre.bind("<Return>", lambda e: self.iniciar_sesion())
    
    def iniciar_sesion(self):
        """Iniciar sesión con el nombre"""
        nombre = self.entry_nombre.get().strip()
        if nombre:
            self.nombre_usuario = nombre
            
            # Crear datos del usuario si no existen
            if nombre not in self.datos_usuario:
                self.datos_usuario[nombre] = {
                    "registros_diarios": {},
                    "historial_recetas": []
                }
                self.guardar_datos()
            
            self.mostrar_dashboard()
        else:
            messagebox.showwarning("Nombre requerido", "Por favor escribe tu nombre")
    
    def mostrar_dashboard(self):
        """Mostrar dashboard principal"""
        # Limpiar ventana
        for widget in self.winfo_children():
            widget.destroy()
        
        # Frame superior con bienvenida
        header_frame = ctk.CTkFrame(self, height=80, corner_radius=0)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        bienvenida = ctk.CTkLabel(
            header_frame,
            text=f"¡Hola, {self.nombre_usuario}! 👋",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        bienvenida.pack(side="left", padx=30, pady=20)
        
        fecha_label = ctk.CTkLabel(
            header_frame,
            text=datetime.now().strftime("%A, %d de %B %Y"),
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        fecha_label.pack(side="left", padx=10)
        
        # Botón cerrar sesión
        btn_salir = ctk.CTkButton(
            header_frame,
            text="Cerrar Sesión",
            command=self.mostrar_login,
            width=120,
            height=35,
            fg_color="gray30",
            hover_color="gray20"
        )
        btn_salir.pack(side="right", padx=30, pady=20)
        
        # Frame principal con los 3 módulos
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Crear 3 tarjetas para los módulos
        # Módulo 1: Registro Diario
        card1 = self.crear_tarjeta_modulo(
            main_frame,
            "📊 Registro Diario",
            "Registra tu comida, sueño y bienestar",
            "#3b82f6",
            lambda: self.abrir_modulo_registro()
        )
        card1.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        
        # Módulo 2: Generador de Recetas
        card2 = self.crear_tarjeta_modulo(
            main_frame,
            "🍳 Recetas Inteligentes",
            "Sube foto de tu refri y genera recetas",
            "#10b981",
            lambda: self.abrir_modulo_recetas()
        )
        card2.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
        
        # Módulo 3: Asistente de Estudio
        card3 = self.crear_tarjeta_modulo(
            main_frame,
            "🧠 Asistente de Estudio",
            "Tips, motivación y ayuda académica",
            "#f59e0b",
            lambda: self.abrir_modulo_asistente()
        )
        card3.grid(row=0, column=2, padx=15, pady=15, sticky="nsew")
        
        # Configurar grid
        main_frame.grid_columnconfigure((0, 1, 2), weight=1, uniform="column")
        main_frame.grid_rowconfigure(0, weight=1)
    
    def crear_tarjeta_modulo(self, parent, titulo, descripcion, color, comando):
        """Crear tarjeta para cada módulo"""
        frame = ctk.CTkFrame(parent, corner_radius=15, fg_color=color)
        
        # Contenedor interno
        inner_frame = ctk.CTkFrame(frame, fg_color="transparent")
        inner_frame.pack(expand=True, fill="both", padx=30, pady=30)
        
        # Título
        label_titulo = ctk.CTkLabel(
            inner_frame,
            text=titulo,
            font=ctk.CTkFont(size=24, weight="bold"),
            wraplength=250
        )
        label_titulo.pack(pady=(20, 10))
        
        # Descripción
        label_desc = ctk.CTkLabel(
            inner_frame,
            text=descripcion,
            font=ctk.CTkFont(size=14),
            wraplength=250,
            text_color="gray90"
        )
        label_desc.pack(pady=10)
        
        # Botón
        btn = ctk.CTkButton(
            inner_frame,
            text="Abrir",
            command=comando,
            width=150,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="white",
            text_color=color,
            hover_color="gray90"
        )
        btn.pack(pady=(30, 20))
        
        return frame
    
    def abrir_modulo_registro(self):
        """Módulo de registro diario"""
        ventana = ctk.CTkToplevel(self)
        ventana.title("📊 Registro Diario")
        ventana.geometry("800x700")
        
        # Frame principal con scroll
        scroll_frame = ctk.CTkScrollableFrame(ventana)
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        titulo = ctk.CTkLabel(
            scroll_frame,
            text="📊 Registro Diario de Bienestar",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        titulo.pack(pady=20)
        
        fecha_hoy = date.today().isoformat()
        datos_hoy = self.datos_usuario[self.nombre_usuario]["registros_diarios"].get(fecha_hoy, {})
        
        # Horas de sueño
        label_sueno = ctk.CTkLabel(scroll_frame, text="💤 Horas de Sueño:", font=ctk.CTkFont(size=16))
        label_sueno.pack(pady=(20, 5))
        
        entry_sueno = ctk.CTkEntry(
            scroll_frame,
            placeholder_text="Ej: 7.5",
            width=300,
            height=40
        )
        entry_sueno.pack(pady=5)
        entry_sueno.insert(0, datos_hoy.get("sueno", ""))
        
        # Comidas del día
        label_comidas = ctk.CTkLabel(scroll_frame, text="🍽️ Comidas del Día:", font=ctk.CTkFont(size=16))
        label_comidas.pack(pady=(20, 5))
        
        entry_comidas = ctk.CTkTextbox(scroll_frame, width=500, height=100)
        entry_comidas.pack(pady=5)
        entry_comidas.insert("1.0", datos_hoy.get("comidas", ""))
        
        # Vasos de agua
        label_agua = ctk.CTkLabel(scroll_frame, text="💧 Vasos de Agua (8oz):", font=ctk.CTkFont(size=16))
        label_agua.pack(pady=(20, 5))
        
        entry_agua = ctk.CTkEntry(
            scroll_frame,
            placeholder_text="Ej: 8",
            width=300,
            height=40
        )
        entry_agua.pack(pady=5)
        entry_agua.insert(0, datos_hoy.get("agua", ""))
        
        # Ejercicio
        label_ejercicio = ctk.CTkLabel(scroll_frame, text="🏃 Ejercicio (minutos):", font=ctk.CTkFont(size=16))
        label_ejercicio.pack(pady=(20, 5))
        
        entry_ejercicio = ctk.CTkEntry(
            scroll_frame,
            placeholder_text="Ej: 30",
            width=300,
            height=40
        )
        entry_ejercicio.pack(pady=5)
        entry_ejercicio.insert(0, datos_hoy.get("ejercicio", ""))
        
        # Nivel de estrés
        label_estres = ctk.CTkLabel(scroll_frame, text="😰 Nivel de Estrés (1-10):", font=ctk.CTkFont(size=16))
        label_estres.pack(pady=(20, 5))
        
        slider_estres = ctk.CTkSlider(scroll_frame, from_=1, to=10, width=400, number_of_steps=9)
        slider_estres.pack(pady=5)
        slider_estres.set(datos_hoy.get("estres", 5))
        
        valor_estres = ctk.CTkLabel(scroll_frame, text=f"{int(slider_estres.get())}", font=ctk.CTkFont(size=14))
        valor_estres.pack()
        
        def actualizar_valor(value):
            valor_estres.configure(text=f"{int(value)}")
        
        slider_estres.configure(command=actualizar_valor)
        
        # Horas de estudio
        label_estudio = ctk.CTkLabel(scroll_frame, text="📚 Horas de Estudio:", font=ctk.CTkFont(size=16))
        label_estudio.pack(pady=(20, 5))
        
        entry_estudio = ctk.CTkEntry(
            scroll_frame,
            placeholder_text="Ej: 4",
            width=300,
            height=40
        )
        entry_estudio.pack(pady=5)
        entry_estudio.insert(0, datos_hoy.get("estudio", ""))
        
        # Notas adicionales
        label_notas = ctk.CTkLabel(scroll_frame, text="📝 Notas del Día:", font=ctk.CTkFont(size=16))
        label_notas.pack(pady=(20, 5))
        
        entry_notas = ctk.CTkTextbox(scroll_frame, width=500, height=100)
        entry_notas.pack(pady=5)
        entry_notas.insert("1.0", datos_hoy.get("notas", ""))
        
        # Botón guardar
        def guardar_registro():
            self.datos_usuario[self.nombre_usuario]["registros_diarios"][fecha_hoy] = {
                "sueno": entry_sueno.get(),
                "comidas": entry_comidas.get("1.0", "end-1c"),
                "agua": entry_agua.get(),
                "ejercicio": entry_ejercicio.get(),
                "estres": int(slider_estres.get()),
                "estudio": entry_estudio.get(),
                "notas": entry_notas.get("1.0", "end-1c")
            }
            self.guardar_datos()
            messagebox.showinfo("Guardado", "¡Registro guardado exitosamente!")
        
        btn_guardar = ctk.CTkButton(
            scroll_frame,
            text="💾 Guardar Registro",
            command=guardar_registro,
            width=250,
            height=50,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        btn_guardar.pack(pady=30)
    
    def abrir_modulo_recetas(self):
        """Módulo de generador de recetas"""
        ventana = ctk.CTkToplevel(self)
        ventana.title("🍳 Generador de Recetas")
        ventana.geometry("900x800")
        
        # Frame principal con scroll
        scroll_frame = ctk.CTkScrollableFrame(ventana)
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        titulo = ctk.CTkLabel(
            scroll_frame,
            text="🍳 Generador Inteligente de Recetas",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        titulo.pack(pady=20)
        
        # Variable para imagen
        self.imagen_seleccionada = None
        self.label_imagen = None
        
        # Botón subir imagen
        btn_subir = ctk.CTkButton(
            scroll_frame,
            text="📸 Subir Foto del Refrigerador",
            command=lambda: self.seleccionar_imagen(scroll_frame),
            width=300,
            height=50,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        btn_subir.pack(pady=20)
        
        # Frame para mostrar imagen
        self.frame_imagen = ctk.CTkFrame(scroll_frame, width=400, height=400)
        self.frame_imagen.pack(pady=20)
        
        # Frame para resultados
        self.frame_resultados = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        self.frame_resultados.pack(fill="both", expand=True, pady=20)
    
    def seleccionar_imagen(self, parent):
        """Seleccionar y analizar imagen"""
        archivo = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Imágenes", "*.png *.jpg *.jpeg")]
        )
        
        if archivo:
            # Mostrar imagen
            imagen = Image.open(archivo)
            imagen.thumbnail((400, 400))
            photo = ctk.CTkImage(imagen, size=(400, 400))
            
            for widget in self.frame_imagen.winfo_children():
                widget.destroy()
            
            label_img = ctk.CTkLabel(self.frame_imagen, image=photo, text="")
            label_img.image = photo
            label_img.pack()
            
            self.imagen_seleccionada = Image.open(archivo)
            
            # Analizar automáticamente
            threading.Thread(target=self.analizar_imagen_threading, daemon=True).start()
    
    def analizar_imagen_threading(self):
        """Analizar imagen en thread separado"""
        if not self.cliente_openai:
            clave_api = os.getenv("OPENAI_API_KEY")
            if not clave_api:
                self.after(0, lambda: messagebox.showerror(
                    "Error",
                    "Por favor configura tu OPENAI_API_KEY en el archivo .env"
                ))
                return
            self.cliente_openai = OpenAI(api_key=clave_api)
        
        # Limpiar resultados previos
        self.after(0, lambda: self.limpiar_resultados())
        
        # Mostrar loading
        self.after(0, lambda: self.mostrar_loading("Analizando ingredientes..."))
        
        # Analizar
        ingredientes = self.analizar_imagen_openai(self.imagen_seleccionada)
        
        if ingredientes:
            self.after(0, lambda: self.mostrar_resultados("🥗 Ingredientes Detectados", ingredientes))
            
            # Generar recetas
            self.after(0, lambda: self.mostrar_loading("Generando recetas deliciosas..."))
            recetas = self.generar_recetas_openai(ingredientes)
            
            if recetas:
                self.after(0, lambda: self.mostrar_resultados("📖 Tus Recetas", recetas))
    
    def analizar_imagen_openai(self, imagen):
        """Analizar imagen con OpenAI"""
        try:
            buffer = BytesIO()
            imagen.save(buffer, format="PNG")
            imagen_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            
            respuesta = self.cliente_openai.chat.completions.create(
                model="gpt-4o",
                messages=[{
                    "role": "user",
                    "content": [{
                        "type": "text",
                        "text": "Analiza esta imagen y lista todos los ingredientes que veas. Solo nombres, en formato de lista con viñetas."
                    }, {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{imagen_base64}"}
                    }]
                }],
                max_tokens=500
            )
            return respuesta.choices[0].message.content
        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Error", f"Error al analizar: {str(e)}"))
            return None
    
    def generar_recetas_openai(self, ingredientes):
        """Generar recetas con OpenAI"""
        try:
            respuesta = self.cliente_openai.chat.completions.create(
                model="gpt-4o",
                messages=[{
                    "role": "user",
                    "content": f"Con estos ingredientes: {ingredientes}\n\nSugiere 2-3 recetas fáciles para estudiantes. Incluye nombre, ingredientes e instrucciones breves."
                }],
                max_tokens=1000
            )
            return respuesta.choices[0].message.content
        except Exception as e:
            return None
    
    def limpiar_resultados(self):
        """Limpiar frame de resultados"""
        for widget in self.frame_resultados.winfo_children():
            widget.destroy()
    
    def mostrar_loading(self, texto):
        """Mostrar mensaje de loading"""
        self.limpiar_resultados()
        label = ctk.CTkLabel(
            self.frame_resultados,
            text=texto,
            font=ctk.CTkFont(size=16),
            text_color="gray"
        )
        label.pack(pady=20)
    
    def mostrar_resultados(self, titulo, contenido):
        """Mostrar resultados en el frame"""
        # Título
        label_titulo = ctk.CTkLabel(
            self.frame_resultados,
            text=titulo,
            font=ctk.CTkFont(size=20, weight="bold")
        )
        label_titulo.pack(pady=(20, 10))
        
        # Contenido
        textbox = ctk.CTkTextbox(self.frame_resultados, width=700, height=200)
        textbox.pack(pady=10)
        textbox.insert("1.0", contenido)
        textbox.configure(state="disabled")
    
    def abrir_modulo_asistente(self):
        """Módulo de asistente de estudio"""
        ventana = ctk.CTkToplevel(self)
        ventana.title("🧠 Asistente de Estudio")
        ventana.geometry("900x700")
        
        # Frame principal con scroll
        scroll_frame = ctk.CTkScrollableFrame(ventana)
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        titulo = ctk.CTkLabel(
            scroll_frame,
            text="🧠 Tu Asistente Personal de Estudio",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        titulo.pack(pady=20)
        
        # Opciones
        opciones_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        opciones_frame.pack(fill="x", pady=20)
        
        # Botón 1: Técnicas de estudio
        btn1 = ctk.CTkButton(
            opciones_frame,
            text="📚 Técnicas de Estudio",
            command=lambda: self.obtener_consejo("tecnicas de estudio efectivas para estudiantes", scroll_frame),
            width=250,
            height=60,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        btn1.pack(pady=10)
        
        # Botón 2: Motivación
        btn2 = ctk.CTkButton(
            opciones_frame,
            text="💪 Motivación y Ánimo",
            command=lambda: self.obtener_consejo("mensaje motivacional para estudiante estresado", scroll_frame),
            width=250,
            height=60,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#10b981"
        )
        btn2.pack(pady=10)
        
        # Botón 3: Manejo de estrés
        btn3 = ctk.CTkButton(
            opciones_frame,
            text="😌 Manejo de Estrés",
            command=lambda: self.obtener_consejo("técnicas para manejar el estrés académico", scroll_frame),
            width=250,
            height=60,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#f59e0b"
        )
        btn3.pack(pady=10)
        
        # Botón 4: Organización
        btn4 = ctk.CTkButton(
            opciones_frame,
            text="📅 Organización y Productividad",
            command=lambda: self.obtener_consejo("consejos de organización y productividad para estudiantes", scroll_frame),
            width=250,
            height=60,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#8b5cf6"
        )
        btn4.pack(pady=10)
        
        # Botón 5: Pregunta personalizada
        btn5 = ctk.CTkButton(
            opciones_frame,
            text="💬 Hacer una Pregunta",
            command=lambda: self.pregunta_personalizada(scroll_frame),
            width=250,
            height=60,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#ec4899"
        )
        btn5.pack(pady=10)
        
        # Frame para respuestas
        self.frame_respuesta = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        self.frame_respuesta.pack(fill="both", expand=True, pady=20)
    
    def obtener_consejo(self, tema, parent):
        """Obtener consejo de IA"""
        threading.Thread(target=lambda: self.obtener_consejo_threading(tema), daemon=True).start()
    
    def obtener_consejo_threading(self, tema):
        """Obtener consejo en thread separado"""
        if not self.cliente_openai:
            clave_api = os.getenv("OPENAI_API_KEY")
            if not clave_api:
                self.after(0, lambda: messagebox.showerror(
                    "Error",
                    "Por favor configura tu OPENAI_API_KEY en el archivo .env"
                ))
                return
            self.cliente_openai = OpenAI(api_key=clave_api)
        
        # Limpiar respuesta previa
        self.after(0, lambda: self.limpiar_respuesta())
        self.after(0, lambda: self.mostrar_loading_respuesta())
        
        try:
            respuesta = self.cliente_openai.chat.completions.create(
                model="gpt-4o",
                messages=[{
                    "role": "user",
                    "content": f"Como mentor de estudiantes, dame consejos prácticos sobre: {tema}. Sé específico, motivador y útil. Máximo 300 palabras."
                }],
                max_tokens=500
            )
            contenido = respuesta.choices[0].message.content
            self.after(0, lambda: self.mostrar_respuesta(contenido))
        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Error", f"Error: {str(e)}"))
    
    def pregunta_personalizada(self, parent):
        """Ventana para pregunta personalizada"""
        dialogo = ctk.CTkInputDialog(
            text="¿Qué te gustaría saber?",
            title="Pregunta Personalizada"
        )
        pregunta = dialogo.get_input()
        
        if pregunta:
            self.obtener_consejo(pregunta, parent)
    
    def limpiar_respuesta(self):
        """Limpiar frame de respuesta"""
        for widget in self.frame_respuesta.winfo_children():
            widget.destroy()
    
    def mostrar_loading_respuesta(self):
        """Mostrar loading en respuesta"""
        label = ctk.CTkLabel(
            self.frame_respuesta,
            text="🤔 Pensando...",
            font=ctk.CTkFont(size=16),
            text_color="gray"
        )
        label.pack(pady=20)
    
    def mostrar_respuesta(self, contenido):
        """Mostrar respuesta de IA"""
        self.limpiar_respuesta()
        
        textbox = ctk.CTkTextbox(self.frame_respuesta, width=700, height=300)
        textbox.pack(pady=20, padx=20, fill="both", expand=True)
        textbox.insert("1.0", contenido)
        textbox.configure(state="disabled")

if __name__ == "__main__":
    app = AplicacionEstudiante()
    app.mainloop()

