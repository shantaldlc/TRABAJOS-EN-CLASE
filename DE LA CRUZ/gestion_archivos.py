# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:38:07 2024

@author: Shantal
"""
import os

def crear_archivo(nombre_archivo, contenido):
   archivo = open(nombre_archivo, "wt")
   archivo.write(contenido)
   print(f"Archivo '{nombre_archivo}' creado.")
    

def eliminar_archivo(nombre_archivo):
    if os.remove(nombre_archivo):
        print(f"Archivo '{nombre_archivo}' Se logró eliminar.")
    else:
        print(f"El archivo '{nombre_archivo}' no existe.")



def agregar_contenido_archivo(nombre_archivo, contenido):
    archivo = open(nombre_archivo, "at") 
    archivo.write(contenido)
    print(f"Contenido agregado al archivo '{nombre_archivo}'.")



def leer_archivo(nombre_archivo):
    try: 
        archivo = open(nombre_archivo, "rt")
        contenido = archivo.read()
        print(f"Su contenido es :'{nombre_archivo}':")
        print(contenido)
        
    except:
        print(f"El archivo '{nombre_archivo}' no existe o no se encuentra.")
        
        
