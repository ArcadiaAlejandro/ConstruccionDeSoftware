from flask import Flask, render_template
from Conection import consultar_base_de_datos

app = Flask(__name__)

@app.route('/')
def index():
    # Llamas a tu función de Python aquí
    mensaje = "¡Hola desde Python!"

    # Devuelves el resultado como HTML utilizando una plantilla
    return render_template('/HTML/index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)