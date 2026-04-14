"""FUNCIONES"""


def saludo(nombre):
    """Funcion para saludar"""
    print("Hola, " + nombre + "!")
    return


saludo("Cesar")


def factorial(n):
    """Función que calcula el factorial de un número entero positivo.
    Parámetros
    n: Es un entero positivo.
    Devuelve el factorial de n.
    """
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp


print(factorial(4))
print(factorial(20))


def calculoiva(cantidad, iva=21):
    """Función para calcular el IVA"""
    total = cantidad + (cantidad * (iva/100))
    return total


print("El total de la factura es: ", calculoiva(100))


def circle_area(radius):
    """Función que calcula el area de un círculo.
    Parámetros
    radius: Es el radio del círculo.
    Devuelve el área del círculo de radio radius.
    """
    pi = 3.1415
    return pi*radius**2


def cilinder_volume(radius, high):
    """Función que calcula el volumen de un cilindro.
    Parámetros
    radius: Es el radio de la base del cilindro.
    high: Es la altura del cilindro.
    Devuelve el volumen del clindro de radio radius y altura high.
    """
    return circle_area(radius)*high


print(cilinder_volume(3, 10))


def media(*numero):
    return sum(numero) / len(numero)


print(media(1, 2, 3, 4, 5, 6))


def square(sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list


print(square([1, 2, 3, 4, 5]))
print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))


def square(sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list


def statistics(sample):
    """Función que calcula la media, varianza y desviación típica de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
    """
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat


print(statistics([1, 2, 3, 4, 5]))
print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))


def mcd(n, m):
    """Función que calcula el máximo común divisor de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m.
    """
    rest = 0
    while (m > 0):
        rest = m
        m = n % m
        n = rest
    return n


def mcm(n, m):
    """Función que calcula el mínimo común múltiplo de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
    """
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater


print(mcd(24, 36))
print(mcm(24, 36))


def to_decimal(n):
    """Función que convierte un número binario en decimal.
    Parámetros:
        - n: Es una cadena de ceros y unos.
    Devuelve:
        El número decimal correspondiente a n.
    """
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal


def to_binary(n):
    """Función que convierte un número decimal en binario.
    Parámetros:
        - n: Es un número entero.
    Devuelve:
        El número binario correspondiente a n.
    """
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)


print(to_decimal('10110'))
print(to_binary(22))
print(to_decimal(to_binary(22)))
print(to_binary(to_decimal('10110')))


def count_words(text):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - text: Es una cadena de caracteres.
    Devuelve: 
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words


def most_repeated(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq


text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(count_words(text))
print(most_repeated(count_words(text)))
