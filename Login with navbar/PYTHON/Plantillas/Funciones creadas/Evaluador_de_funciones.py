import time #importamos la libreria time

#creamos un diccionario
tabla_switch = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111',
    }
def usa_switch(decimal):
    return tabla_switch.get(decimal, "NA")

#creamos una funcion con if y elif
def usa_if(decimal):
    if decimal == '0':
        return "000"
    elif decimal == '1':
        return "001"
    elif decimal == '2':
        return "010"
    elif decimal == '3':
        return "011"
    elif decimal == '4':
        return "100"
    elif decimal == '5':
        return "101"
    elif decimal == '6':
        return "110"
    elif decimal == '7':
        return "111"
    else:
        return "NA"

#creamos una funcion para medir el tiempo de ejecucion

def mide_tiempo(funcion): #definimos la funciones mide_tiempo con un parametro
    def funcion_medida(*args, **kwargs): #asignamos parametros
        inicio = time.time() #llamamos a la funcion time
        c = funcion(*args, **kwargs) #enlazamos parametros
        print(f"Entrada: {args[1]}. Tiempo: {time.time() - inicio}") #imprimimos
        return c #retornamos los parametros
    return funcion_medida

#creamos una funcion para iterar
@mide_tiempo
def repite_funcion(funcion, entrada):
    return [funcion(entrada) for i in range(10000000)]

#usamos las funciones para evaluar

for i in range(8):
    repite_funcion(usa_if, str(i))

for i in range(8):
    repite_funcion(usa_switch, str(i))
    