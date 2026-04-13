"""CADENAS"""
import re
nombre = str(input("Ingrese su nombre: "))
num = int(input("Digite un numero: "))
print((nombre + "\n") * num)

nombrec = input("Ingrese su nombre completo: ")
print(nombrec.upper())
print(nombrec.lower())
print(nombrec.title())

nombreC = str(input("Ingrese nombre: "))
print(nombreC.upper() + " tiene " + str(len(nombreC)) + " cantidad de letras")

telefono = str(input("Ingrese numero telefonico (+34-913724710-56): "))
print(telefono[4:16])

frase = input("Ingrese una frase: ")
print(frase[::-1])

frase2 = input("Ingrese una frase: ")
vocal = (input("Ingrese una vocal: ").lower())
print(frase2.replace(vocal, vocal.upper()))

email = input("Ingrese su email: ")
print(re.sub(r'@.*', '@ceus.us', email))
print(email[:email.find('@')] + '@ceu.es')

euros = input("Ingrese el valor en euros con dos decimales: ")
print(euros[:euros.find('.')])
print(euros[euros.find('.'):])

date = str(input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: "))
print('Día', date[:2])
print('Mes', date[3:5])
print('Año', date[6:])

cesta = input(
    'Introduce los productos de la cesta de la compra separados por comas: ')
print(cesta.replace(',', '\n'))
cesta = input(
    'Introduce los productos de la cesta de la compra separados por comas: ')
print('\n'.join(cesta.split(',')))

nombrep = input("Ingrese el nombre del producto: ")
preciop = round(float(input("Ingrese el precio del producto: ")), 2)
numerop = int(input("Ingrese el numero de unidades: "))
print('{producto}: {unidades:3d} unidades x {precio:09.2f}€ = {total:011.2f}€'.format(
    producto=nombrep, unidades=numerop, precio=preciop, total=numerop * preciop))
