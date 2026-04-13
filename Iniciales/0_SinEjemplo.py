nombre = "Cesar"
print(len(nombre))

a = "es"
b = "hace"
c = "programa"
frase = f"Y así {a} como se {b} un {c}"

print(frase)

for letra in nombre:
    print(letra)

for i in range(1, 5):
    print(i)

age = [1, 2, 3, 4]
print(age)

list = [1, "hola"]
print(list)

tupla = tuple('cesar')
print(tupla)


def volar():
    print("El pajaro vuela")
    return


volar()


def bienvenida(nombre):
    print("Bienvenido, " + nombre)
    return


bienvenida("Cesar")


def menu(*platos):
    print("El menú es: ", end=" ")
    for plato in platos:
        print(plato, end=", ")
    return


menu("ensalada", "pizza", "albondiga")
