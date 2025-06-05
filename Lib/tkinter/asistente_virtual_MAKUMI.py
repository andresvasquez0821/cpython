import tkinter as tk
from tkinter import ttk, messagebox

# Diccionario de respuestas por materia
respuestas = {
    "Matemáticas": [
        "🔹 Representación visual de funciones lineales.",
        "🔹 Gráficas dinámicas usando GeoGebra.",
        "🔹 Organizadores visuales para resolver sistemas de ecuaciones."
    ],
    "Inglés": [
        "🔹 Tarjetas interactivas de verbos regulares e irregulares.",
        "🔹 Videos y ejercicios del presente perfecto y pasado simple.",
        "🔹 Juegos con palabras y frases completas."
    ],
    "Ciencias Sociales": [
        "🔹 Infografías sobre emigraciones y neonazismo.",
        "🔹 Línea de tiempo interactiva.",
        "🔹 Trivia sobre conceptos aprendidos."
    ],
    "Tecnología e Informática": [
        "🔹 Diseño intuitivo con botones e íconos.",
        "🔹 Usabilidad pensada para secundaria.",
        "🔹 Interfaz con chatbots o asistentes simples."
    ],
    "Gestión Empresarial": [
        "🔹 Organigrama empresarial visual.",
        "🔹 Representación del proceso administrativo.",
        "🔹 Ciclo de vida del producto o asistente."
    ],
    "Español": [
        "🔹 Organizadores gráficos como mapas conceptuales.",
        "🔹 Textos informativos con diseño atractivo.",
        "🔹 Cohesión visual para facilitar la lectura."
    ],
    "Lengua Castellana": [
        "🔹 Infografías por fases del proyecto.",
        "🔹 Presentaciones visuales para la exposición.",
        "🔹 Lenguaje técnico con recursos gráficos."
    ]
}

# Función para mostrar la respuesta
def mostrar_temas():
    materia = combo.get()
    if materia in respuestas:
        texto = "\n".join(respuestas[materia])
        salida.config(state='normal')
        salida.delete(1.0, tk.END)
        salida.insert(tk.END, f"{materia}:\n\n{texto}")
        salida.config(state='disabled')
    else:
        messagebox.showwarning("Error", "Por favor, selecciona una materia válida.")

# Crear la ventana
ventana = tk.Tk()
ventana.title("MAKUMI (portada)")
ventana.geometry("600x450")
ventana.configure(bg="#f4f4f4")

# Portada / título principal
tk.Label(ventana, text="MAKUMI (Asistente Educativo)", font=("Arial", 18, "bold"), bg="#f4f4f4", fg="#007acc").pack(pady=10)

# Subtítulo
tk.Label(ventana, text="Selecciona una materia para ver los temas disponibles", font=("Arial", 13), bg="#f4f4f4").pack(pady=5)

# Lista desplegable
combo = ttk.Combobox(ventana, font=("Arial", 12), width=40)
combo['values'] = list(respuestas.keys())
combo.pack(pady=10)

# Botón para mostrar temas
tk.Button(ventana, text="Mostrar Temas", font=("Arial", 12), command=mostrar_temas, bg="#007acc", fg="white").pack(pady=10)

# Cuadro de texto de salida
salida = tk.Text(ventana, height=10, width=70, font=("Arial", 12), state='disabled', wrap='word', bg="#e8e8e8")
salida.pack(pady=10)

# Botón para salir
tk.Button(ventana, text="Salir", font=("Arial", 10), command=ventana.quit).pack(pady=5)

# Ejecutar app
ventana.mainloop()
