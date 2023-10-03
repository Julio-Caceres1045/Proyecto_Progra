usuarios = {}

def registrar_usuario():
    print("Registro de nuevo usuario")
    usuario = input("Elija un nombre de usuario: ")
    
    if usuario in usuarios:
        print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
        return

    contrasena = input("Elija una contraseña: ")
    usuarios[usuario] = contrasena
    print("Registro exitoso. Ahora puede iniciar sesión con su nuevo usuario.")

def login():
    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")

        if usuario in usuarios and usuarios[usuario] == contrasena:
            print("Inicio de sesión exitoso. ¡Bienvenido,", usuario, "!")
