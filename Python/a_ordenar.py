#Documento con muchas cosas de Python
print ("hola1")
print ("hola2")
numero_1 = 1
numero_2 = 2
resultado = numero_1 + numero_2
print(resultado)

mensaje = "hola"
mensaje += " "
mensaje += "alvaro"
print (mensaje)


mensaje = "hola bienvenido a Python"
mensaje += ","
espacio = " "
nombre = "Álvaro"
print (mensaje + espacio + nombre)

numero_1 = 1
numero_2 = 2
resultado = numero_1 + numero_2
resultado = str(resultado)
print ("el resultado de la suma es: " + resultado)


mensaje = "Hola Alvaro"
buscar_subcadena = mensaje.find("Alvaro")
print (buscar_subcadena)


mensaje = "hola Alvaro"
extraer_subcadena = mensaje[1:9]
print(extraer_subcadena)


mensaje_uno = "hola"
mensaje_dos = "hola"
print (mensaje_uno == mensaje_dos)



print("suma:")
numero_uno = 1
numero_dos = 2
resultado = numero_uno + numero_dos
print("El resultado de la suma es: " + str(resultado))

print("resta:")
numero_uno = 1
numero_dos = 2
resultado = numero_uno - numero_dos
print("El resultado de la resta es: " + str(resultado))

print("multiplicacion:")
numero_uno = 1
numero_dos = 2
resultado = numero_uno * numero_dos
print("El resultado de la multiplicacion es: " + str(resultado))

print("elevado a:")
numero_uno = 2
numero_dos = 4
resultado = numero_uno ** numero_dos
print("El resultado de elevar a es: " + str(resultado))

print("dividir:")
numero_uno = 2
numero_dos = 4
resultado = numero_uno / numero_dos
print("El resultado de dividir es: " + str(resultado))



numero = 15
print(numero, type(numero))

numero = "hola"
print(numero, type(numero))

numero_decimal = 15.5
print(numero_decimal, type(numero_decimal))

numero_complejo = 5 + 6j
print(numero_complejo, type(numero_complejo))

nombre = "alvaro"
print(nombre, type(nombre))



verdadero_falso = 3 == 3
print(verdadero_falso, type(verdadero_falso))

mayor_que = 3 > 1
print(mayor_que, type(mayor_que))




#interactivo
palabra = input("Introduce una palabra: ")
num_int = int(input("Introduce un numero entero: "))
num_float = float(input ("Introduce un numero con decimales: "))
num_complex = complex(input ("Introduce un numero complejo: "))

print("String: ", palabra)
print("numero entero: ", num_int)
print("flotante: ", num_float)
print("complejo: ", num_complex)



nombre = input("¿Como te llamas? ")
print("hola " + nombre + ", ¿Te apetece hacer una suma? ")
num_uno = int(input("Introduce el primer valor: "))
num_dos = int(input("Introduce el segundo valor: "))
resultado = num_uno + num_dos
print(nombre + " El resultado de la suma es: ", resultado)




num_uno = 5
if num_uno == 2 :
    print("El numero es cinco")




nombre = input("¿Como te llamas?: ")

nota_matematicas = int(input(nombre + ", Que nota sacaste en matematicas: "))
nota_lengua = int(input(nombre + ", Que nota sacaste en lengua: "))

media = (nota_matematicas + nota_lengua) / 2
media = int(media)

if media >= 5 :
    print('Enhorabuena has aprobado ' + nombre + '"aprobaste" con una media de: ', media)




print ("hola1")
print ("hola2")
numero_1 = 1
numero_2 = 2
resultado = numero_1 + numero_2
print(resultado)