import tkinter as tk
from tkinter import messagebox

# Diccionario de respuestas por palabras clave
respuestas = {
    "matemáticas": [
        "🔹 Representación visual de funciones lineales.",
        "🔹 Gráficas dinámicas usando GeoGebra.",
        "🔹 Organizadores visuales para resolver sistemas de ecuaciones."
    ],
    "inglés": [
        "🔹 Tarjetas interactivas de verbos regulares e irregulares.",
        "🔹 Videos y ejercicios del presente perfecto y pasado simple.",
        "🔹 Juegos con palabras y frases completas."
    ],
    "ciencias sociales": [
        "🔹 Infografías sobre emigraciones y neonazismo.",
        "🔹 Línea de tiempo interactiva.",
        "🔹 Trivia sobre conceptos aprendidos."
    ],
    "tecnología": [
        "🔹 Diseño intuitivo con botones e íconos.",
        "🔹 Usabilidad pensada para secundaria.",
        "🔹 Interfaz con chatbots o asistentes simples."
    ],
    "gestión empresarial": [
        "🔹 Diseño del organigrama empresarial.",
        "🔹 Proceso administrativo en gráfico.",
        "🔹 Ciclo de vida del producto en infografía."
    ],
    "español": [
        "🔹 Organizadores gráficos como mapas conceptuales.",
        "🔹 Textos informativos con diseño atractivo.",
        "🔹 Cohesión visual para facilitar la lectura."
    ],
    "lengua castellana": [
        "🔹 Infografías temáticas por fases del proyecto.",
        "🔹 Presentaciones visuales para la exposición.",
        "🔹 Lenguaje técnico con recursos gráficos."
    ]
}

# Función para responder
def responder():
    pregunta = entry.get().lower()
    for materia, temas in respuestas.items():
        if materia in pregunta:
            output.config(state='normal')
            output.delete(1.0, tk.END)
            output.insert(tk.END, f"📘 {materia.title()}:\n" + "\n".join(temas))
            output.config(state='disabled')
            return
    messagebox.showinfo("Asistente", "❓ No reconozco esa materia. Prueba con otra.")

# Crear la ventana
root = tk.Tk()
root.title("Asistente Educativo")
root.geometry("500x400")
root.configure(bg="#f4f4f4")

# Widgets
tk.Label(root, text="¿Sobre qué materia quieres aprender?", font=("Arial", 14), bg="#f4f4f4").pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), width=40)
entry.pack(pady=5)

tk.Button(root, text="Preguntar", font=("Arial", 12), command=responder, bg="#007acc", fg="white").pack(pady=10)

output = tk.Text(root, height=10, width=60, font=("Arial", 12), state='disabled', wrap='word', bg="#e8e8e8")
output.pack(pady=10)

# Iniciar la app
root.mainloop()

    
