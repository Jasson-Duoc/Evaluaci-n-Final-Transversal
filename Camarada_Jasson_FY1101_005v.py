import random
import csv
import math

#Diccionarios y Lista
trabajadores = [
    {"nombre ": "JuanPérez"},
    {"nombre": "María García"},
    {"nombre": "Carlos López"} ,
    {"nombre": "Ana Martínez"} ,
    {"nombre":"Pedro Rodríguez"} ,
    {"nombre":"Laura Hernández"} ,
    {"nombre": "Miguel Sánchez"} ,
    {"nombre": "Isabel Gómez"} ,
    {"nombre": "Francisco Díaz"} ,
    {"nombre": "Elena Fernández"} ]

sueldos = []

#Def

def asignar_sueldos():
    global sueldos
    sueldos= [random.randint(300000 , 2000000) for i in range (10) ]
    print("Sueldos asignados")
    
def clasificar_sueldos():
     
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            print(f"Nombre empleado: {trabajador['nombre']}  Sueldo: ${sueldo}")

    for trabajador, sueldo in zip(trabajadores, sueldos):
        if 800000 <= sueldo <= 2000000:
            print(f"Nombre empleado: {trabajador['nombre']}  Sueldo: ${sueldo}")

    print("\nSueldos superiores a $2.000.000 TOTAL:")
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo > 2000000:
            print(f"Nombre empleado: {trabajador['nombre']}  Sueldo: ${sueldo}")

    print("\n Total :", (sueldos))
        
def reporte_sueldos():
    
    salud=sueldos*0.7
    afp=sueldos*1.2
    print(f"Nombre Empleado", "Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido")
    

#Menu
while True:
    print("Menu \n")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa \n")
    opcion=int(input("Seleccione al accion requerida: \n"))
    
    if opcion ==1:
        asignar_sueldos()
    elif opcion==2:
        clasificar_sueldos()
    elif opcion ==3:
        ver_estadistica()
    elif opcion==4:
        reporte_sueldos()
    elif opcion==5:
        print("Finalizando programa \n Desarrollado por Jasson Camarada \n Rut 20789267-K")
        break
    else:
        ("Favor ingresar un numero valido")

 