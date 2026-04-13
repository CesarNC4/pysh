"""CONDICIONALES"""
age = int(input("Ingrese su edad: "))
if age >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

contra = (str(input("Ingrese su contraseña: ")).lower())
correct = "123Ce$$".lower()
if contra == correct:
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")

div = int(input("Digite primer numero: "))
div2 = int(input("Digite segundo numero: "))
if div2 > 0:
    print(div / div2)
else:
    print("Error: No se puede dividir entre 0")

parimpar = int(input("Ingrese un numero: "))
if parimpar % 2 == 0:
    print("Es par")
else:
    print("Es impar")

age2 = int(input("Ingrese su edad: "))
sueldo = int(input("Ingrese sus ingresos mensuales: "))
if age2 > 16 and sueldo >= 1000:
    print("Puede tributar")
else:
    print("No puede tributar")

nom = input("Ingrese su nombre: ")
se = input("Ingrese su sexo (m o f): ")
if se.lower() == "m":
    if nom.lower() > "n":
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")
elif se.lower() == "f":
    if nom.lower() < "m":
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")

print("Procesa a su grupo")

renta = int(input("Ingrese su renta anual: "))
if renta < 10000:
    print("Su imposito es del 5%")
elif renta >= 10000 and renta < 20000:
    print("Su imposito es del 15%")
elif renta >= 20000 and renta < 35000:
    print("Su imposito es del 20%")
elif renta >= 35000 and renta <= 60000:
    print("Su imposito es del 30%")
elif renta > 60000:
    print("Su imposito es del 45%")

bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))
# Clasifiación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))

edad = int(input("Ingrese su edad: "))
if edad < 4:
    print("Gratis.")
elif edad >= 4 and edad <= 18:
    print("Paga 5$")
else:
    print("Pagar 10$")

pizza = (input("¿Quiere una pizza vegetariana (v) o no vegetariana(nv)?")).lower()
if pizza == "v":
    ingre = int(input("Elija los ingredientes:\n1. Pimiento\n2. Tofu"))
    if ingre == 1:
        print("Su pizza vegetariana tiene Mozarrella, Tomate y Pimiento")
    elif ingre == 2:
        print("Su pizza vegetariana tiene Mozarrella, Tomate y Tofu")
    else:
        print("Ingrediente no disponible")
elif pizza == "nv":
    ingre = int(
        input("Elija los ingredientes:\n1. Peperoni\n2. Salmón\n3. Jamón"))
    if ingre == 1:
        print("Su pizza no vegetariana tiene Mozarrella, Tomate y Peperoni")
    elif ingre == 2:
        print("Su pizza no vegetariana tiene Mozarrella, Tomate y Salmón")
    elif ingre == 3:
        print("Su pizza no vegetariana tiene Mozarrella, Tomate y Jamón")
    else:
        print("Ingrediente no disponible")
