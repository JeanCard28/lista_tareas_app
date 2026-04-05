class Tarea:
    def __init__(self, id, descripcion):
        self.id = id
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True
