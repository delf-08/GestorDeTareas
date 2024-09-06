import os
from datetime import datetime
from gestor_tareas import Tareas

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

gestor_tarea = Tareas()

while True:
    clear_screen()
    print("1: Agregar Tarea")
    print("2: Mostrar Tareas")
    print("3: Buscar Tarea")
    print("4: Actualizar Tarea")
    print("5: Eliminar Tarea")
    print("6: Salir")

    opcion = input("Elija Opcion: ")
    clear_screen()

    if opcion == "6":
        break

    if opcion == "1":
        nombre = input("Nombre: ")
        fechaCreacion = datetime.strptime(input("Fecha de Creación (YYYY-MM-DD): "), "%Y-%m-%d").date()
        fechaLimite = datetime.strptime(input("Fecha Límite (YYYY-MM-DD): "), "%Y-%m-%d").date()
        gestor_tarea.añadir(nombre, fechaCreacion, fechaLimite)
        print("Tarea agregada correctamente.")
    
    elif opcion == "2":
        gestor_tarea.mostrar()
    
    elif opcion in ["3", "4", "5"]:
        id = input("Ingrese el ID: ")
        if opcion == "3":
            tabla_resultado = gestor_tarea.buscar(id)
            if tabla_resultado:
                print(" ")
                print("ID   Nombre  FechaCreacion  FechaLimite")
                print(f"{tabla_resultado[0]}    {tabla_resultado[1]}    {tabla_resultado[2]}    {tabla_resultado[3]}")
                print(" ")
            else:
                print("Tarea no encontrada")
        
        elif opcion == "4":
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            nueva_fechaCreacion = datetime.strptime(input("Ingrese nueva fecha de creación (YYYY-MM-DD): "), "%Y-%m-%d").date()
            nueva_fechaLimite = datetime.strptime(input("Ingrese nueva fecha límite (YYYY-MM-DD): "), "%Y-%m-%d").date()
            gestor_tarea.actualizar(id, nuevo_nombre, nueva_fechaCreacion, nueva_fechaLimite)
            print("Tarea actualizada correctamente.")
        
        elif opcion == "5":
            gestor_tarea.eliminar(id)
            print("Tarea eliminada correctamente.")
    
    input("Presione Enter para continuar...")
