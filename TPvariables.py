#variables : las usamos para guardar datos.
#1 Crear dos variables numéricas llamadas a y b con valores a elección. Mostrar ambas en pantalla.
a = 4
b = 3
print (a , b)

# 2 Crear dos variables numéricas, calcular su suma 
# y guardar el resultado en una tercera variable.
#  Mostrar las tres variables en pantalla.

a = 5
b = 6
c= a + b

print (c)

#Definir dos números y calcular suma, resta, multiplicación y división.
#  Mostrar cada resultado en pantalla.

a = 4
b = 3
c= a * b
d = a/b
e = a + b 
f = a - b

print ( c, d , e , f)

#4 Definir tres variables numéricas que representen notas.
#  Calcular el promedio y mostrarlo en pantalla

nota_a = 8
nota_b = 7
nota_c = 10

promedio = (nota_a + nota_b + nota_c)/3
print (f"el promedio es:{promedio}")

# 5 Definir dos números y mostrar en pantalla 
# el resultado de las comparaciones >, < y ==.
g = 8
h = 11
print (f"datos G igual a:{g} y H igual a: {h}\n es G mayor que H? {g > h} \n es G menor que H? {g < h} \n es G igual que H? {g == h}")


#Definir dos números y construir expresiones lógicas usando and.
#  Mostrar en pantalla si ambas condiciones se cumplen.

el_and = 22 > 11 and 11 < 22
print (el_and)

# otro ejemplo con expresión lógica AND
nota = 8
asistencia = 85

promociona = (nota >= 7) and (asistencia > 80)
print(f"¿Promociona la materia?: {promociona}")

# Definir dos números y construir expresiones lógicas usando and.
#  Mostrar en pantalla si ambas condiciones se cumple
unacosa_olaotra = 15 > 10 or 2 > 10 
print (f" {unacosa_olaotra}")
a = 5
b = 20

# 2. Usamos el 'or'
# Condición: ¿a es mayor a 10? O ¿b es mayor a 10?
# (La primera es Falsa, pero la segunda es Verdadera)
resultado = (a > 10) or (b > 10)

# 3. Mostramos en pantalla
print(f"Datos: a={a}, b={b}")
print(f"¿Se cumple que a > 10 o que b > 10?: {resultado}")

#Definir dos números y construir expresiones lógicas usando or. 
# Mostrar en pantalla si al menos una condición se cumple
esta_lloviendo = False
print(f"¿Está lloviendo?: {esta_lloviendo}")
print(f"¿Tengo que salir sin paraguas?: {not esta_lloviendo}")

#Definir una variable numérica y verificar con una expresión lógica 
# si el valor se encuentra dentro de un rango, 
# por ejemplo mayor que 10 y menor que 20. Mostrar el resultado

# 1. Definimos la variable numérica
numero = 15

# 2. Verificamos si está en el rango (10 a 20)
# Tiene que ser mayor a 10 Y menor a 20
esta_en_rango = (numero > 10) and (numero < 20)

# 3. Mostramos el resultado con nuestra f-string
print(f"El número es: {numero}")
print(f"¿Está entre 10 y 20?: {esta_en_rango}")
# Definir varias variables numéricas, realizar operaciones aritméticas entre ellas 
# y luego comparar los resultados usando operadores lógicos. Mostrar todo en pantalla

p = 10
q = 5
r = 20
s = 2

resta = p - q      
divide = r / s 


comparo = (resta < 10) and (divide < 10)

print (f"datos= {p, q,r,s}")
print(f"Resta de {p , q} es \n{resta}\nDivisión de{r, s}: {divide}")
print(f"¿Es la resta < a 10 y la división < a 10?: {comparo}")
#Definir tres variables booleanas con valores True o False. 
# Luego armar dos expresiones lógicas con esas mismas variables, 
# una sin paréntesis y otra con paréntesis,
#  de manera que el resultado final cambie. 
# Mostrar en pantalla las variables utilizadas 
# y el resultado de cada expresión, para observar 
# cómo los paréntesis modifican la evaluación lógica.

m = True
n = False
o = False

sin_parentesis = m or n and o

con_parentesis = (m or n) and o 
print (f"variables: m: {m} n: {n} o: {o}")
print (f"resultado sin parémtesis: {sin_parentesis}")
print (f"resultado con paréntesis: {con_parentesis}")