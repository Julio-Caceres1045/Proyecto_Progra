usuarios = {}

def registrar_usuario():
    print("Registro de nuevo usuario")
    usuario = input("Elija un nombre de usuario: ")

    # Verificar si el usuario ya existe
    if usuario in usuarios:
        print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
        return

    contrasena = input("Elija una contraseña: ")
    usuarios[usuario] = contrasena
    print("Registro exitoso. Ahora puede iniciar sesión con su nuevo usuario.")
