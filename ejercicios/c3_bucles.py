"""BUCLES"""
palabra = input("Escriba una palabra: ")
n = 1
for range in range(0, 10):
    print(n, palabra)
    n += 1

edadc = int(input("Ingrese su edad: "))
i = 0
while i < edadc:
    print(i+1)
    i += 1

n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")

amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))

entero = int(input("Escriba un numero entero: "))
d = 0
while d <= entero:
    print("*" * d)
    d += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

contraseña = "1234cesar"
contra = ' '
while contra != contraseña:
    contra = str(input("Escribe la contraseña: "))
print("Contraseña correcta")

n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])

frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." %
      (letra, contador, frase))

while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)
