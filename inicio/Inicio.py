
import json
import hashlib


usuario = "usuario"
contrasena= "SISGESA"

def encriptar_contrasena(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()


def guardar_credenciales():
    credenciales = {
        "usuario": usuario,
        "contrasena": encriptar_contrasena(contrasena)
    }
    with open("contrasena.json", 'w') as archivo:
        json.dump(credenciales, archivo)

def inicio_sesion(usuario, contrasena):
    try:
        with open("passwords.json", "r") as archivo:
            credenciales = json.load(archivo)
            if usuario == credenciales["usuario"] and encriptar_contrasena(contrasena) == credenciales["contrasena"]:
                print("Inicio de sesión exitoso.")
                cambiarPassword(credenciales["usuario"])  
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def cambiarPassword(usuario):
    try:
        nueva_contrasena = input("Ingrese su nueva contraseña: ")
        nueva_contrasena_encriptada = encriptar_contrasena(nueva_contrasena)

        credenciales = {
            'usuario': usuario,
            'contrasena': nueva_contrasena_encriptada
        }
        with open('passwords.json', 'w') as archivo:
            json.dump(credenciales, archivo)

        print("Contraseña cambiada exitosamente.")

    except Exception as e:
        print(f"Ocurrió un error al cambiar la contraseña: {e}")


guardar_credenciales()

