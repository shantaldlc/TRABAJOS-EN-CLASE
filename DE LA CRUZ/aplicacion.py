# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:43:03 2024

@author: Shantal
"""
import sys
import gestion_archivos

def menu():
  
    print("Menú: ")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Agregar contenido")
    print("4. Mostrar contenido de archivo")
    print("5. Salir")

def crear():
    nombre_archivo = input("Ingresa el nombre del archivo  con su extensión .txt, .py etc: ")
    contenido = input("Ingresa el contenido del archivo: ")
    gestion_archivos.crear_archivo(nombre_archivo, contenido)

def eliminar():
    nombre_archivo = input("Ingresa el nombre del archivo a eliminar: ")
    gestion_archivos.eliminar_archivo(nombre_archivo)

def agregar():
    nombre_archivo = input("Ingresa el nombre del archivo: ")
    contenido = input("Ingresa el contenido a agregar: ")
    gestion_archivos.agregar_contenido_archivo(nombre_archivo, contenido)

def listar():
    nombre_archivo = input("Ingresa el nombre del archivo para leer: ")
    gestion_archivos.leer_archivo(nombre_archivo)

def salir():
    print("Cerrando el programa...")
    sys.exit()

def error():
    print("Intenta nuevamente. ERROR")

def main():
    while True:
        menu()
        opcion = input("Selecciona una de las opciones: ")
        
        if opcion == '1':
            crear()
        elif opcion == '2':
            eliminar()
        elif opcion == '3':
            agregar()
        elif opcion == '4':
            listar()
        elif opcion == '5':
            salir()
        else:
            error()

if __name__ == "__main__":
    main()


