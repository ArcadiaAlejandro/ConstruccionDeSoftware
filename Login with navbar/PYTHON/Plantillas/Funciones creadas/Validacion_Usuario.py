import secrets
import string

def validador_de_contraseñas(contraseña):
    while True:  # Bucle para la contraseña
        if len(contraseña) < 8:  # Definimos la cantidad mínima de caracteres que debe tener
            print("Contraseña muy corta, debe tener más de 8 caracteres")
            continue

        # Validación de minúsculas
        if not any(char.islower() for char in contraseña):
            print("La contraseña debe tener al menos una minúscula")
            continue

        # Validación de mayúsculas
        if not any(char.isupper() for char in contraseña):
            print("La contraseña debe tener al menos una mayúscula")
            continue

        # Validación de números
        if not any(char.isdigit() for char in contraseña):
            print("La contraseña debe tener al menos un número")
            continue

        # Validación de espacios en blanco
        if " " in contraseña:
            print("La contraseña no debe tener espacios en blanco")
            continue

        # Validación de caracteres alfanuméricos
        if not any(char.isalnum() for char in contraseña):
            print("La contraseña no debe tener un carácter alfanumérico")
            continue

        print("La contraseña es segura")
        break

def Generador_de_contraseñas():
    generador_letras = string.ascii_letters
    generador_numeros = string.digits
    generador_caracteres_especiales = string.punctuation

    # Concatenamos los caracteres generados
    contraseña_concatenada = generador_letras + generador_numeros + generador_caracteres_especiales

    # Validador de longitud
    while True:
        try:
            longitud_contraseña = int(input("Ingrese la longitud de la contraseña: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero.")

    # Generamos la contraseña
    while True:
        contraseña_generada = ''.join(secrets.choice(contraseña_concatenada) for _ in range(longitud_contraseña))
        
        # Verificamos que cumpla con criterios la contraseña
        if (
            any(char in generador_caracteres_especiales for char in contraseña_generada) and  # Que exista al menos 1 caracter especial
            sum(char in generador_numeros for char in contraseña_generada) >= 2  # Que existan al menos 2 números
        ):
            return contraseña_generada

def validar_usuario_contraseña(usuario_correcto, contraseña_correcta):
    intentos_maximos = 3
    intentos = 0

    while intentos < intentos_maximos:
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        if usuario == usuario_correcto and contraseña == contraseña_correcta:
            print("Inicio de sesión exitoso. ¡Bienvenido!")
            break
        else:
            print("Nombre de usuario o contraseña incorrectos. Inténtelo de nuevo.")
            intentos += 1

    if intentos == intentos_maximos:
        print("Número máximo de intentos alcanzado. Acceso denegado.")

#creamos un constructor

if __name__ == "__main__":
    print("Bienvenido al Módulo de validación y generación de contraseñas de Python")
    contraseña_generada = Generador_de_contraseñas()
    print(f"Contraseña generada: {contraseña_generada}")

    validador_de_contraseñas(contraseña_generada)

    usuario_correcto = "usuario"
    contraseña_correcta = contraseña_generada  # Use the generated password for validation
    validar_usuario_contraseña(usuario_correcto, contraseña_correcta)