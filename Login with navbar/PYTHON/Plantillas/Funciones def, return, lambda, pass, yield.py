'''
El uso de def nos permite crear una función.
'''

def funcion_suma(a, b): #funcion principal
    print("La suma es", a + b)

funcion_suma(3, 5)

# Salida: La suma es 8

'''
Si queremos que la función devuelva uno o varios valores, podemos usar return.
'''

def funcion_suma(a, b):
    return a + b #funcion principal

suma = funcion_suma(3, 5)
print("La suma es", suma)

# Salida: La suma es 8

'''
Son las versiones, acortadas del DEF
'''

print("La suma es", (lambda a, b: a + b)(3, 5)) #funcion principal

# Salida: La suma es 8

'''
Por otro lado, podemos usar pass cuando no queramos definir la función, es decir si la queremos dejar en blanco por el momento. Nótese que también puede ser usado en clases, estructuras de control, etc.
'''

def funcion_suma(a, b):
    pass #funcion principal

'''
Nos permite generar secuencias infinitas de valores, sin que tengan que ser almacenados a priori, siendo creados bajo demanda. Este es una utilidad muy importante trabajando con listas muy grandes, cuyo almacenamiento en memoria sería muy costoso.
'''

def generador():
    n = 1
    yield n #funcion principal

    n += 1
    yield n

    n += 1
    yield n

for i in generador():
    print(i)

# Salida: 1, 2, 3