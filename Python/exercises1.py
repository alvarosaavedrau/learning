#https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/

#1 Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("¡Hola mundo!")

#2 Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
saludo = "Hola mundo"
print(saludo)


#3 Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
# donde <nombre> es el nombre que el usuario haya introducido.
nombre = input("¿Como te llamas? ")
print("Hola " + nombre)


#4 Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética
print(((3 + 2) / (2 * 5)) ** 2)


#5 Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas = float(input("¿Cuantas horas has trabajado?: "))
coste = float(input("¿Cuanto cuesta la hora hombre?: "))

solucion = horas * coste

print("Te corresponde la siguiente paga: ", solucion )


#6 Escribir un programa que lea un entero positivo,n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n .
# La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
n = int(input("Introduce un número entero: "))
suma = n * (n + 1) / 2
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))


#7 Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla
# la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")

imc = round(float(peso)/float(estatura)**2,2)

print("Tu índice de masa corporal es " + str(imc))


#8 Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números
#introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")

print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))


#9 Escribir un programa que pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años, y muestre por pantalla el capital obtenido en la
# inversión redondeado con dos decimales.
cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))

print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))