#!/usr/bin/python3
#coding: utf-8

#calcular nota media

nombre = input("Escribe tu número de expediente o nombre y apellidos: ")
nota_matematicas = float(input(nombre + ", ¿Que nota sacaste en matematicas:? "))
nota_lengua = float(input(nombre + ", ¿Que nota sacaste en lengua:? "))
nota_filosofia = float(input(nombre + ", ¿Que nota sacaste en filosofia:? "))

resultado = (nota_filosofia + nota_lengua + nota_matematicas) / 3

resultado = int(resultado)

print('Tu nota media en estas 3 asignaturas es: ', resultado)

if resultado <= 4.9:
    print(nombre, "No has llegado al 5, deberás presentarte a la recuperación ")
if resultado >=5:
    print(nombre, "¡Enhorabuena has aprobado!")