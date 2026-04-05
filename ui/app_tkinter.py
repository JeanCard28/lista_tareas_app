import tkinter as tk
from tkinter import messagebox
from servicios.tarea_servicio import TareaServicio

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.servicio = TareaServicio()

        # Entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Evento teclado (ENTER)
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # Lista
        self.lista = tk.Listbox(root, width=50)
        self.lista.pack(pady=10)

        # Evento doble clic
        self.lista.bind("<Double-1>", self.completar_tarea_evento)

        # Botones
        tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea).pack()
        tk.Button(root, text="Marcar Completada", command=self.completar_tarea).pack()
        tk.Button(root, text="Eliminar", command=self.eliminar_tarea).pack()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for t in self.servicio.listar_tareas():
            texto = f"{t.id} - {t.descripcion}"
            if t.completada:
                texto += " [Hecho]"
            self.lista.insert(tk.END, texto)

    def agregar_tarea(self):
        texto = self.entry.get()
        if texto:
            self.servicio.agregar_tarea(texto)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def completar_tarea(self):
        try:
            seleccion = self.lista.get(self.lista.curselection())
            id = int(seleccion.split("-")[0])
            self.servicio.completar_tarea(id)
            self.actualizar_lista()
        except:
            messagebox.showwarning("Error", "Selecciona una tarea")

    def completar_tarea_evento(self, event):
        self.completar_tarea()

    def eliminar_tarea(self):
        try:
            seleccion = self.lista.get(self.lista.curselection())
            id = int(seleccion.split("-")[0])
            self.servicio.eliminar_tarea(id)
            self.actualizar_lista()
        except:
            messagebox.showwarning("Error", "Selecciona una tarea")
