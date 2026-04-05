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

        # Lista
        self.lista = tk.Listbox(root, width=50)
        self.lista.pack(pady=10)

        # Botones
        tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea).pack()
        tk.Button(root, text="Marcar Completada", command=self.completar_tarea).pack()
        tk.Button(root, text="Eliminar", command=self.eliminar_tarea).pack()

        # ========================
        # EVENTOS DE TECLADO
        # ========================

        # Enter → Agregar tarea
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # Tecla C → Completar tarea
        self.root.bind("c", self.completar_tarea_evento)
        self.root.bind("C", self.completar_tarea_evento)

        # Delete → Eliminar tarea
        self.root.bind("<Delete>", self.eliminar_tarea_evento)

        # Escape → Cerrar app
        self.root.bind("<Escape>", self.cerrar_app)

        # Evento doble clic (extra)
        self.lista.bind("<Double-1>", self.completar_tarea_evento)

    # ========================
    # FUNCIONES PRINCIPALES
    # ========================

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for t in self.servicio.listar_tareas():
            texto = f"{t.id} - {t.descripcion}"
            if t.completada:
                texto += " ✔"
            self.lista.insert(tk.END, texto)

    def agregar_tarea(self):
        texto = self.entry.get()
        if texto:
            self.servicio.agregar_tarea(texto)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()

    def completar_tarea(self):
        try:
            seleccion = self.lista.get(self.lista.curselection())
            id = int(seleccion.split("-")[0])
            self.servicio.completar_tarea(id)
            self.actualizar_lista()
        except:
            messagebox.showwarning("Error", "Selecciona una tarea")

    def eliminar_tarea(self):
        try:
            seleccion = self.lista.get(self.lista.curselection())
            id = int(seleccion.split("-")[0])
            self.servicio.eliminar_tarea(id)
            self.actualizar_lista()
        except:
            messagebox.showwarning("Error", "Selecciona una tarea")

    # ========================
    # EVENTOS (TECLADO)
    # ========================

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def completar_tarea_evento(self, event):
        self.completar_tarea()

    def eliminar_tarea_evento(self, event):
        self.eliminar_tarea()

    def cerrar_app(self, event):
        self.root.destroy()
