# EJERCICIO 10 — Pendientes con prioridad

class Pendientes:
    def __init__(self):
        self.tareas = []

    def agregar(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def urgentes(self):
        return [
            tarea for tarea in self.tareas
            if tarea[1].lower() == "alta"
        ]

    def eliminar(self, descripcion):
        self.tareas = [
            tarea for tarea in self.tareas
            if tarea[0] != descripcion
        ]


pendientes = Pendientes()
pendientes.agregar("Entregar tarea", "alta")
pendientes.agregar("Ordenar escritorio", "baja")
pendientes.agregar("Estudiar Python", "alta")
print(pendientes.urgentes())
pendientes.eliminar("Ordenar escritorio")
print(pendientes.tareas)
