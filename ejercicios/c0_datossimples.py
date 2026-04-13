"""EJERCICIOS BASICOS"""
print("Hola Mundo")

saludo = "Hola Mundo"
print(saludo)

nombre = input("¿Cual es tu nombre?: ")
print("Hola, " + nombre)

arit = ((3+2)/(2*5))**2
print(arit)

horast = int(input("¿Cuantas horas trabajo?: "))
horasv = int(input("¿Cual es el valor por hora?: "))
horasp = horast * horasv
print("La paga es de: ", horasp)

entero = int(input("Ingrese un entero positivo: "))
suma = entero * (entero + 1) / 2
print(suma)

peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese la altura (m): "))
imc = peso * altura**2
IMC = round(imc, 2)
print("Tu indice de masa corporal es: ", IMC)

n = int(input("Ingrese primer numero: "))
m = int(input("Ingrese segundo numero: "))

div = n/m
c = n//m
r = n % m
print(f"La división es {div}, el cosciente es {c} y el resto es {r}")

inv = float(input("¿Cuanto va a invertir?: "))
inte = float(input("¿Cuanto es el interes anual?: "))
years = float(input("¿Por cuantos años?: "))
capital = round(inv * (inte / 100 + 1) ** years, 2)
print("Su capital es de ", capital)

payaso = int(input("¿Cuantos payasos fueron vendidos?: "))
mucas = int(input("¿Cuantas muñecas fueron vendidas?: "))
pesop = 112
pesom = 75
peso = (payaso * pesop) + (mucas * pesom)
print("El peso total del paquete es de ", peso)

depo = float(input('¿Cuanto dinero deposito inicialmente?: '))
inte = float(4.0)
primer = round(depo * (inte / 100 + 1), 2)
segundo = round(depo * (inte / 100 + 1) ** 2, 2)
tercero = round(depo * (inte / 100 + 1) ** 3, 2)
print(
    f"El monto con intereses el primer año es {primer}, el segundo año es {segundo} y el tercer año es {tercero}")

panes = float(input("Numero de barras de pan vendidas que no son de día: "))
precio = float(3.49)
descu = 0.6
total = round((precio * descu) * panes, 2)
print(
    f"""El precio habitual de una barra de pan es de {precio}$. 
    Sin embargo, como no es fresca tiene un descuento del 60% 
    por lo que el coste de su compra de hoy será de: {total}""")
