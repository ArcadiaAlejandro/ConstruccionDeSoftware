import pyodbc

def consultar_base_de_datos():
    try: 
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-8BN7C2N;DATABASE=dbInkaRoca;UID=Alejandro De La Cruz;PWD=123')  # hacemos la conexión con la base de datos
        print("Conexión Exitosa!!")  # identificador para conocer que se realizó de forma correcta con la base de datos
        cursor = connection.cursor()  # creamos un cursor para la conexión
        cursor.execute("SELECT @@version;")  # obtiene la versión necesaria para poder conectarse a la base de datos
        row = cursor.fetchone()  # creamos un iterador

        cursor.execute(
            'SELECT * FROM [dbInkaRoca].[dbo].[tblCliente]'
        )
        rows = cursor.fetchall()  # creamos un puntero
        for row in rows:
            print(rows)
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
        print("Conexión finalizada")

# Llamamos a la función para ejecutar el código
#consultar_base_de_datos()