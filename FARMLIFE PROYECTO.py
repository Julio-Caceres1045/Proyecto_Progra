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
            import random
            import time

            tiempo = 0
            while True:
                print(f"Ha pasado {tiempo} días desde el inicio del juego.")
                time.sleep(1) 
                
                print("Bienvenido a la granja de Iván y Julio")
                time.sleep(2)
                print("---------FARMLIFE---------")
                print("----- Menú Principal -----")
                print("1. Ver mis Cultivos")
                print("2. Ver mis Animales")
                print("3. Acciones del granjero")
                print("4. Ver Area de Comercio")
                print("5. Salir")

                opcion = input("Selecciona una opción: ")

                if opcion == '1':
                    tiempo += 1
                    class Cultivo:
                        def __init__(self, nombre, etapas_crecimiento, producto_cosecha):
                            self.nombre = nombre
                            self.etapas_crecimiento = etapas_crecimiento
                            self.etapa_actual = 0
                            self.producto_cosecha = producto_cosecha
                            self.plaga = False  
                            self.rendimiento = 1  

                        def crecer(self):
                            if self.etapa_actual < len(self.etapas_crecimiento) - 1:
                                self.etapa_actual += 1

                        def esta_maduro(self):
                            return self.etapa_actual == len(self.etapas_crecimiento) - 1

                        def aplicar_fertilizante(self):
                            
                            self.rendimiento += 0.2

                        def aplicar_plagicida(self):
                            
                            self.plaga = False
                
                    class Jugador:
                        def __init__(self):
                            self.inventario = {}
                            self.dinero = 1000

                        def plantar_cultivo(self, cultivo, cantidad):
                            if cultivo.nombre in self.inventario and self.inventario[cultivo.nombre] >= cantidad:
                                self.inventario[cultivo.nombre] -= cantidad
                                return Cultivo(cultivo.nombre, cultivo.etapas_crecimiento, cultivo.producto_cosecha)
                            else:
                                print("No tienes suficientes semillas para plantar.")

                        def cosechar_cultivo(self, cultivo):
                            if cultivo.esta_maduro():
                                cantidad_cosechada = int(1 * cultivo.rendimiento)  
                                self.inventario[cultivo.producto_cosecha] = self.inventario.get(cultivo.producto_cosecha, 0) + cantidad_cosechada
                                return True
                            else:
                                print("El cultivo aún no está maduro para la cosecha.")
                                return False

                        def comprar_fertilizante(self):
                            precio_fertilizante = 50
                            if self.dinero >= precio_fertilizante:
                                self.dinero -= precio_fertilizante
                                return True
                            else:
                                print("No tienes suficiente dinero para comprar fertilizante.")
                                return False

                        def comprar_plagicida(self):
                            precio_plagicida = 30
                            if self.dinero >= precio_plagicida:
                                self.dinero -= precio_plagicida
                                return True
                            else:
                                print("No tienes suficiente dinero para comprar plagicida.")
                                return False

                    

                    class CultivoTomate(Cultivo):
                        def __init__(self):
                            super().__init__("Tomate", ["Brote", "Crecimiento", "Maduración"], "Tomate")

                    class CultivoZanahoria(Cultivo):
                        def __init__(self):
                            super().__init__("Zanahoria", ["Brote", "Crecimiento", "Maduración"], "Zanahoria")

                    class CultivoMaiz(Cultivo):
                        def __init__(self):
                            super().__init__("Maíz", ["Brote", "Crecimiento", "Maduración"], "Maíz")

                    class CultivoPapa(Cultivo):
                        def __init__(self):
                            super().__init__("Papa", ["Brote", "Crecimiento", "Maduración"], "Papa")

                    class CultivoLechuga(Cultivo):
                        def __init__(self):
                            super().__init__("Lechuga", ["Brote", "Crecimiento", "Maduración"], "Lechuga")


                    def avanzar_tiempo(cultivos):
                        for cultivo in cultivos:
                            cultivo.crecer()
                            if random.random() < 0.1:  
                                cultivo.plaga = True

                    def regar_cultivos(cultivos):
                        for cultivo in cultivos:
                            if not cultivo.esta_maduro():
                                cultivo.crecer()

                    def main():
                        jugador = Jugador()
                        cultivos = []

                        
                        cultivo_tomate = CultivoTomate()
                        cultivo_zanahoria = CultivoZanahoria()
                        cultivo_maiz = CultivoMaiz()
                        cultivo_papa = CultivoPapa()
                        cultivo_lechuga = CultivoLechuga()

                    
                        jugador.inventario[cultivo_tomate.nombre] = 10
                        jugador.inventario[cultivo_zanahoria.nombre] = 5
                        jugador.inventario[cultivo_maiz.nombre] = 7
                        jugador.inventario[cultivo_papa.nombre] = 8
                        jugador.inventario[cultivo_lechuga.nombre] = 6

                        while True:
                            print("\nAcciones disponibles:")
                            print("1. Plantar cultivo")
                            print("2. Cosechar cultivo")
                            print("3. Aplicar fertilizante")
                            print("4. Aplicar plaguicida")
                            print("5. Regar cultivos")
                            print("6. Avanzar en el tiempo")
                            print("7. Salir")
                            eleccion = input("Selecciona una acción: ")

                            if eleccion == "1":
                                print("\nCultivos disponibles para plantar:")
                                print("1. Tomate")
                                print("2. Zanahoria")
                                print("3. Maíz")
                                print("4. Papa")
                                print("5. Lechuga")
                                eleccion_cultivo = input("Selecciona un cultivo: ")

                                if eleccion_cultivo == "1":
                                    cantidad = int(input("Cantidad de tomates para plantar: "))
                                    cultivo = jugador.plantar_cultivo(cultivo_tomate, cantidad)
                                    if cultivo:
                                        cultivos.append(cultivo)
                                        print(f"Se plantaron {cantidad} semillas de Tomate")
                                elif eleccion_cultivo == "2":
                                    cantidad = int(input("Cantidad de zanahorias para plantar: "))
                                    cultivo = jugador.plantar_cultivo(cultivo_zanahoria, cantidad)
                                    if cultivo:
                                        cultivos.append(cultivo)
                                        print(f"Se plantaron {cantidad} semillas de Zanahoria")
                                elif eleccion_cultivo == "3":
                                    cantidad = int(input("Cantidad de maíz para plantar: "))
                                    cultivo = jugador.plantar_cultivo(cultivo_maiz, cantidad)
                                    if cultivo:
                                        cultivos.append(cultivo)
                                        print(f"Se plantaron {cantidad} semillas de Maiz")
                                elif eleccion_cultivo == "4":
                                    cantidad = int(input("Cantidad de papas para plantar: "))
                                    cultivo = jugador.plantar_cultivo(cultivo_papa, cantidad)
                                    if cultivo:
                                        cultivos.append(cultivo)
                                        print(f"Se plantaron {cantidad} semillas de Papa")
                                elif eleccion_cultivo == "5":
                                    cantidad = int(input("Cantidad de lechugas para plantar: "))
                                    cultivo = jugador.plantar_cultivo(cultivo_lechuga, cantidad)
                                    if cultivo:
                                        cultivos.append(cultivo)
                                        print(f"Se plantaron {cantidad} semillas de Lechuga")
                                else:
                                    print("Opción inválida.")

                            elif eleccion == "2":
                                for cultivo in cultivos:
                                    if jugador.cosechar_cultivo(cultivo):
                                        cultivos.remove(cultivo)
                                        print(f"Has cosechado {cultivo.producto_cosecha}.")
                                
                            elif eleccion == "3":
                                print("Dinero disponible:", jugador.dinero)
                                if jugador.dinero >= 50:
                                    print("1. Comprar fertilizante (50 monedas)")
                                    print("2. Aplicar fertilizante a cultivos")
                                    eleccion_fertilizante = input("Selecciona una opción: ")
                                    if eleccion_fertilizante == "1":
                                        jugador.dinero -= 50
                                        print("Has comprado fertilizante.")
                                    elif eleccion_fertilizante == "2":
                                        if jugador.dinero >= 50:
                                            jugador.comprar_fertilizante()
                                            for cultivo in cultivos:
                                                cultivo.aplicar_fertilizante()
                                            print("Has aplicado fertilizante a tus cultivos.")
                                        else:
                                            print("No tienes suficiente dinero para aplicar fertilizante.")
                                    else:
                                        print("Opción no válida.")

                            elif eleccion == "4":
                                print("Dinero disponible:", jugador.dinero)
                                if jugador.dinero >= 30:
                                    print("1. Comprar plaguicida (30 monedas)")
                                    print("2. Aplicar plaguicida a cultivos")
                                    eleccion_plaguicida = input("Selecciona una opción: ")
                                    if eleccion_plaguicida == "1":
                                        jugador.dinero -= 30
                                        print("Has comprado plaguicida.")
                                    elif eleccion_plaguicida == "2":
                                        if jugador.dinero >= 30:
                                            jugador.comprar_plagicida()
                                            for cultivo in cultivos:
                                                if cultivo.plaga:
                                                    cultivo.aplicar_plagicida()
                                            print("Has aplicado plaguicida a tus cultivos.")
                                        else:
                                            print("No tienes suficiente dinero para aplicar plaguicida.")
                                    else:
                                        print("Opción no válida.")
                            elif eleccion == "5":
                                regar_cultivos(cultivos)
                                print("Has regado tus cultivos. ¡Crecerán más rápido!")

                            elif eleccion == "6":
                                avanzar_tiempo(cultivos)
                                print("El tiempo ha avanzado.")
                            
                            elif eleccion == "7":
                                print("¡Gracias por jugar!")
                                break

                    if __name__ == "__main__":
                        main()
                elif opcion == '2':
                    class Animal:
                        def __init__(self, nombre, salud_maxima, hambre_maxima, felicidad_maxima, produccion):
                            self.nombre = nombre
                            self.salud = salud_maxima
                            self.hambre = hambre_maxima
                            self.felicidad = felicidad_maxima
                            self.produccion = produccion
                            self.leche = 0
                            self.huevos = 0
                            self.lana = 0
            
                        def alimentar(self):
                            if comida_disponible[self.nombre] > 0:
                                comida_disponible[self.nombre] -= 1
                                self.hambre -= 10
                                self.salud += 5
                                self.felicidad += 5
                                print(f"Se ha alimentado a {self.nombre}")
                            else:
                                print(f"No tienes suficiente comida para {self.nombre}.")
            
                        def acariciar(self):
                            self.felicidad += 10
                            print(f"Se ha acariciado a {self.nombre}")
            
                        def limpiar(self):
                            self.salud += 10
                            print(f"Se ha limpiado a {self.nombre}")
            
                        def enfermar(self):
                            self.salud -= random.randint(5, 15)
            
                        def recolectar_leche(self):
                            if self.nombre in ["Vaca"]:
                                self.leche += 1
                                print(f"Has recolectado leche de {self.nombre}.")
                            else:
                                print(f"{self.nombre} no produce leche.")
            
                        def recolectar_huevos(self):
                            if self.nombre in ["Gallina"]:
                                self.huevos += 1
                                print(f"Has recolectado huevos de {self.nombre}.")
                            else:
                                print(f"{self.nombre} no pone huevos.")
            
                        def recolectar_lana(self):
                            if self.nombre in ["Oveja"]:
                                self.lana += 1
                                print(f"Has recolectado lana de {self.nombre}.")
                            else:
                                print(f"{self.nombre} no produce lana.")
            
                    def comprar_comida():
                        print("\n----- Comprar Comida -----")
                        print("1. Comida para Vaca")
                        print("2. Comida para Oveja")
                        print("3. Comida para Gallina")
                        opcion = input("Elige el tipo de comida que deseas comprar (1/2/3) o 'q' para salir: ")
                        if opcion == 'q':
                            return
                        elif opcion.isdigit():
                            indice_comida = int(opcion) - 1
                            tipos_comida = list(comida_disponible.keys())
                            if 0 <= indice_comida < len(tipos_comida):
                                comida_disponible[tipos_comida[indice_comida]] += 1
                                print(f"Has comprado comida para {tipos_comida[indice_comida]}.")
            
                    def seleccionar_animal():
                        print("\n----- Seleccionar Animal -----")
                        for i, animal in enumerate(animales):
                            print(f"{i + 1}. {animal.nombre}")
            
                        opcion = input("Elige un animal con el que interactuar (1/2/3) o 'q' para salir: ")
                        if opcion == 'q':
                            return None
                        elif opcion.isdigit():
                            indice_animal = int(opcion) - 1
                            if 0 <= indice_animal < len(animales):
                                return animales[indice_animal]
                        return None
            
                    if __name__ == "__main__":
                        comida_disponible = {"Vaca": 5, "Oveja": 5, "Gallina": 5}  
            
                        
                        animales = [Animal("Vaca", 100, 50, 70, 10),
                                    Animal("Oveja", 80, 40, 60, 5),
                                    Animal("Gallina", 60, 30, 50, 2)]
            
                        while True:
                            print("\n----- Granja de Animales -----")
                            animal_seleccionado = seleccionar_animal()
                            if animal_seleccionado is None:
                                break
            
                            print(f"{animal_seleccionado.nombre} - Salud: {animal_seleccionado.salud}, Hambre: {animal_seleccionado.hambre}, Felicidad: {animal_seleccionado.felicidad}")
            
                            print("\nInventario de Comida:")
                            for nombre, cantidad in comida_disponible.items():
                                print(f"{nombre}: {cantidad}")
            
                        
                            accion = input("\nElige una acción: "
                                        "1. Alimentar, 2. Acariciar, 3. Limpiar, 4. Recolectar recursos, 5. Comprar comida, 'q' para cambiar de animal: ")
            
                            if accion == 'q':
                                continue
                            elif accion.isdigit():
                                accion = int(accion)
                                if 1 <= accion <= 5:
                                    if accion == 1:
                                        animal_seleccionado.alimentar()
                                    elif accion == 2:
                                        animal_seleccionado.acariciar()
                                    elif accion == 3:
                                        animal_seleccionado.limpiar()
                                    elif accion == 4:
                                        animal_seleccionado.recolectar_leche()
                                        animal_seleccionado.recolectar_huevos()
                                        animal_seleccionado.recolectar_lana()
                                    elif accion == 5:
                                        comprar_comida()
            
                                    
                                    animal_seleccionado.hambre += 10
                                    if animal_seleccionado.hambre >= 80:
                                        animal_seleccionado.enfermar()
                                        print(f"{animal_seleccionado.nombre} está hambriento y se ha enfermado!")
            
                                    
                                    if animal_seleccionado.salud <= 0:
                                        print(f"{animal_seleccionado.nombre} ha muerto.")
                                        animales.remove(animal_seleccionado)
                            
