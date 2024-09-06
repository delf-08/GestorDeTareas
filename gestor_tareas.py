import sqlite3
from tasks import Tasks  

class Tareas:
    def __init__(self, db_name="tasks.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            fechaCreacion Date,
            fechaLimite Date
        )
        ''')
        self.conn.commit()

    def añadir(self, nombre, fechaCreacion, fechaLimite):
        self.c.execute("INSERT INTO tasks (nombre, fechaCreacion, fechaLimite) VALUES (?, ?, ?)",
                       (nombre, fechaCreacion, fechaLimite))
        self.conn.commit()
        print("Añadido con éxito")

    def mostrar(self):
        self.c.execute("SELECT * FROM tasks")
        datos = self.c.fetchall()
        headers = ["ID", "Nombre", "FechaCreacion", "FechaLimite"]
        print(" ")
        print(f"{headers[0]:<10} {headers[1]:<20} {headers[2]:<15} {headers[3]:<15}")
        if not datos:
            print("No hay tareas en el gestor.")
        for fila in datos:
            print(f"{fila[0]:<10} {fila[1]:<20} {fila[2]:<15} {fila[3]:<15}")
        
        print(" ")

    def buscar(self, id):
        self.c.execute("SELECT * FROM tasks WHERE id = ?", (id,))
        tabla_resultado = self.c.fetchone()
        return tabla_resultado
        

    def actualizar(self, id, nuevo_nombre, nuevo_fechaCreacion, nueva_fechaLimite):
        task = self.buscar(id)
        if task:
            self.c.execute('''
            UPDATE tasks
            SET nombre = ?, fechaCreacion = ?, fechaLimite = ?
            WHERE id = ?
            ''', (nuevo_nombre, nuevo_fechaCreacion, nueva_fechaLimite, id))
            self.conn.commit()
            print("Tarea actualizada con éxito")

    def eliminar(self, id):
        task = self.buscar(id)
        if task:
            self.c.execute("DELETE FROM tasks WHERE id=? ", (id))
            print("La tarea fue eliminada")
