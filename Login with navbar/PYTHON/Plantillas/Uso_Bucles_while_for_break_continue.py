"""
USO DEL WHILE
"""

x = 0
while x < 3: #Mientras se cumpla la condicion
    print(x)
    x += 1

# Salida: 0, 1, 2

"""
USO DEL FOR
"""
#range son las veces a iterar

for i in range(3): #permite iterar la funcion tantas veces como elementos tiene el iterable.
    print(i)

# Salida: 0, 1, 2

"""
USO DEL FOR
    CONTINUE
"""
#El continue salta hasta el final del bloque, dejando sin ejecutar lo restante, pero continúa en la siguiente iteración.

for i in range(5):
    if i == 1: #si i es similar a 1, entonces
        continue #salta dicha expresion
    print(i)

# Salida: 0, 2, 3, 4

"""
USO DEL FOR
    break 
"""
# rompe la ejecución del bucle, saliendo del mismo.

x = 0 #inicializamos la variable
while True: #mientras de como resultado una verdad
    print(x) #imprime x
    if x == 2: #si x es igual a 2
        break # fin del bucle
    x += 1 #caso contrario sigue sumando

# Salida: 0, 1, 2