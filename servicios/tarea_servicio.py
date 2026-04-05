from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.tareas = []
        self.contador_id = 1

    def agregar_tarea(self, descripcion):
        tarea = Tarea(self.contador_id, descripcion)
        self.tareas.append(tarea)
        self.contador_id += 1

    def listar_tareas(self):
        return self.tareas

    def completar_tarea(self, id):
        for t in self.tareas:
            if t.id == id:
                t.marcar_completada()

    def eliminar_tarea(self, id):
        self.tareas = [t for t in self.tareas if t.id != id]
