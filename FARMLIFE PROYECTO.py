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
    elif opcion == '3':
        class JuegoCalendario:
                def __init__(self):
                    self.hora = 7
                    self.minuto = 0
                    self.dia = 1

                def avanzar_tiempo(self, minutos_avance):
                    self.minuto += minutos_avance

                    if self.minuto >= 60:
                        self.hora += self.minuto // 60
                        self.minuto %= 60

                    if self.hora >= 24:
                        self.dia += 1
                        self.hora %= 24

                def mostrar_tiempo(self):
                    print(f"Día {self.dia}, Hora: {self.hora:02}:{self.minuto:02}")

                def planificar_actividades(self):
                    while True:
                        self.mostrar_tiempo()
                        print("1. Trabajar")
                        print("2. Ver mi lista de avtividades")
                        print("3. Descansar")
                        print("4. Dormir")
                        print("5. Salir")
                        opcion = input("Elige una actividad: ")

                        if opcion == '1':
                            self.avanzar_tiempo(60) 
                        elif opcion == '2':
                            
                            actividades_pendientes = []

                            while True:
                        
                                print("----- Menú Principal -----")
                                print("1. Agregar actividad pendiente")
                                print("2. Ver actividades pendientes")
                                print("3. Realizar una actividad")
                                print("4. Salir")

                                
                                opcion = input("Selecciona una opción: ")

                        
                                if opcion == '1':
                                    
                                    actividad = input("Ingrese una nueva actividad pendiente: ")
                                    actividades_pendientes.append(actividad)
                                    print("Actividad agregada correctamente.")

                                elif opcion == '2':
                            
                                    print("\n----- Actividades Pendientes -----")
                                    for i, actividad in enumerate(actividades_pendientes, 1):
                                        print(f"{i}. {actividad}")
                                    
                                elif opcion == '3':
                                    
                                    print("\n----- Realizar una Actividad -----")
                                    if not actividades_pendientes:
                                        print("No hay actividades pendientes.")
                                    else:
                                        print("Selecciona una actividad para marcar como realizada:")
                                        for i, actividad in enumerate(actividades_pendientes, 1):
                                            print(f"{i}. {actividad}")
                                        indice = input("Ingrese el número de la actividad realizada: ")
                                        if indice.isdigit():
                                            indice = int(indice)
                                            if 1 <= indice <= len(actividades_pendientes):
                                                actividad_realizada = actividades_pendientes.pop(indice - 1)
                                                print(f"Has realizado la siguiente actividad: {actividad_realizada}")
                                            else:
                                                print("Número de actividad no válido.")
                                        else:
                                            print("Entrada no válida. Ingrese un número válido.")

                                elif opcion == '4':
                                    print("¡Gracias por usar la lista de actividades!")
                                    break

                                else:
                                    print("Opción no válida. Por favor, seleccione una opción válida del menú.")

                        elif opcion == '3':
                            self.avanzar_tiempo(30)
                            print("Descansaste")  
                        elif opcion == '4':
                            self.avanzar_tiempo(480)
                            print("Dormiste")  
                        elif opcion == '5':
                            print("¡Hasta luego!")
                            break
                        else:
                            print("Opción no válida. Introduce una opción válida.")

        if __name__ == "__main__":
            juego = JuegoCalendario()
            juego.planificar_actividades()

    elif opcion == '4':
        import random

        class Moneda:
            def __init__(self):
                self.valor = 1000

            def agregar_dinero(self, cantidad):
                self.valor += cantidad

            def restar_dinero(self, cantidad):
                if self.valor >= cantidad:
                    self.valor -= cantidad
                    return True
                else:
                    print("No tienes suficiente dinero.")
                    return False

        class ProductoAgricola:
            def __init__(self, nombre, precio_venta):
                self.nombre = nombre
                self.precio_venta = precio_venta
                self.cantidad = 0

            def comprar(self, cantidad, moneda):
                costo_total = self.precio_venta * cantidad
                if moneda.restar_dinero(costo_total):
                    self.cantidad += cantidad
                    print(f"Has comprado {cantidad} unidades de {self.nombre}.")
                else:
                    print(f"No tienes suficiente dinero para comprar {self.nombre}.")

            def vender(self, cantidad, moneda):
                if self.cantidad >= cantidad:
                    ingreso_total = self.precio_venta * cantidad
                    moneda.agregar_dinero(ingreso_total)
                    self.cantidad -= cantidad
                    print(f"Has vendido {cantidad} unidades de {self.nombre} por {ingreso_total} monedas.")
                else:
                    print(f"No tienes suficientes unidades de {self.nombre} para vender.")

        class MejoraGranja:
            def __init__(self, nombre, costo, aumento_produccion):
                self.nombre = nombre
                self.costo = costo
                self.aumento_produccion = aumento_produccion
                self.comprada = False

            def comprar(self, moneda):
                if not self.comprada:
                    if moneda.restar_dinero(self.costo):
                        self.comprada = True
                        print(f"Has comprado la mejora '{self.nombre}' por {self.costo} monedas.")
                    else:
                        print(f"No tienes suficiente dinero para comprar la mejora '{self.nombre}'.")
                else:
                    print(f"Ya has comprado la mejora '{self.nombre}' previamente.")

        class Jugador:
            def __init__(self):
                self.moneda = Moneda()
                self.productos_agricolas = {
                    "Tomate": ProductoAgricola("Tomate", 20),
                    "Maíz": ProductoAgricola("Maíz", 15),
                    "Papa": ProductoAgricola("Papa", 25),
                    "Zanahoria": ProductoAgricola("Zanahoria", 18),
                    "Lechuga": ProductoAgricola("Lechuga", 22),
                    "Leche": ProductoAgricola("Leche", 8),
                    "Huevos": ProductoAgricola("Huevos", 12),
                    "Lana": ProductoAgricola("Lana", 10)
                }
                self.mejoras_granja = [
                    MejoraGranja("Riego automático", 100, 0.2),  
                    MejoraGranja("Fertilizante avanzado", 150, 0.3)  
                ]

            def comprar_producto(self, nombre_producto, cantidad):
                if nombre_producto in self.productos_agricolas:
                    self.productos_agricolas[nombre_producto].comprar(cantidad, self.moneda)

            def vender_producto(self, nombre_producto, cantidad):
                if nombre_producto in self.productos_agricolas:
                    self.productos_agricolas[nombre_producto].vender(cantidad, self.moneda)

            def comprar_mejora(self, nombre_mejora):
                for mejora in self.mejoras_granja:
                    if mejora.nombre == nombre_mejora:
                        mejora.comprar(self.moneda)

        def mostrar_inventario_jugador(jugador):
            print("\nInventario del jugador:")
            for producto, info_producto in jugador.productos_agricolas.items():
                print(f"{producto}: {info_producto.cantidad} unidades")
            print(f"Dinero: {jugador.moneda.valor} monedas")

        def mostrar_opciones_mercado(productos_agricolas, jugador):
            while True:
                print("\n----- Mercado de la Granja -----")
                print("Productos disponibles:")
                for i, (nombre, info_producto) in enumerate(productos_agricolas.items(), start=1):
                    print(f"{i}. {nombre} - Precio: {info_producto.precio_venta} monedas")

                print("M. Volver al menú principal")
                opcion = input("Selecciona un producto para comprar (1-M): ")

                if opcion == "M" or opcion == "m":
                    break
                elif opcion.isdigit() and 1 <= int(opcion) <= len(productos_agricolas):
                    nombre_producto = list(productos_agricolas.keys())[int(opcion) - 1]
                    cantidad = int(input(f"¿Cuántas unidades de {nombre_producto} deseas comprar? "))
                    jugador.comprar_producto(nombre_producto, cantidad)
                else:
                    print("Opción no válida. Introduce un número del 1 al M.")

        def mostrar_opciones_venta(productos_agricolas, jugador):
            while True:
                print("\n----- Venta de Productos -----")
                print("Productos disponibles para vender:")
                for i, (nombre, info_producto) in enumerate(productos_agricolas.items(), start=1):
                    if info_producto.cantidad > 0:
                        print(f"{i}. {nombre} - Cantidad: {info_producto.cantidad} unidades")

                print("V. Volver al menú principal")
                opcion = input("Selecciona un producto para vender (1-V): ")

                if opcion == "V" or opcion == "v":
                    break
                elif opcion.isdigit() and 1 <= int(opcion) <= len(productos_agricolas):
                    nombre_producto = list(productos_agricolas.keys())[int(opcion) - 1]
                    cantidad = int(input(f"¿Cuántas unidades de {nombre_producto} deseas vender? "))
                    jugador.vender_producto(nombre_producto, cantidad)
                else:
                    print("Opción no válida. Introduce un número del 1 al V.")

        def mostrar_opciones_mejoras(mejoras_granja, jugador):
            while True:
                print("\n----- Comprar Mejoras para la Granja -----")
                print("Mejoras disponibles:")
                for i, mejora in enumerate(mejoras_granja, start=1):
                    if not mejora.comprada:
                        print(f"{i}. {mejora.nombre} - Precio: {mejora.costo} monedas")

                print("M. Volver al menú principal")
                opcion = input("Selecciona una mejora para comprar (1-M): ")

                if opcion == "M" or opcion == "m":
                    break
                elif opcion.isdigit() and 1 <= int(opcion) <= len(mejoras_granja):
                    nombre_mejora = mejoras_granja[int(opcion) - 1].nombre
                    jugador.comprar_mejora(nombre_mejora)
                else:
                    print("Opción no válida. Introduce un número del 1 al M.")

        def main():
            jugador = Jugador()

            while True:
                print("\n----- Granja de Jugador -----")
                print("1. Mostrar Inventario")
                print("2. Mercado de la Granja (Comprar Productos)")
                print("3. Venta de Productos")
                print("4. Comprar Mejoras para la Granja")
                print("5. Salir")

                opcion = input("Selecciona una opción (1-5): ")

                if opcion == "1":
                    mostrar_inventario_jugador(jugador)
                elif opcion == "2":
                    mostrar_opciones_mercado(jugador.productos_agricolas, jugador)
                elif opcion == "3":
                    mostrar_opciones_venta(jugador.productos_agricolas, jugador)
                elif opcion == "4":
                    mostrar_opciones_mejoras(jugador.mejoras_granja, jugador)
                elif opcion == "5":
                    print("¡Gracias por jugar!")
                    break
                else:
                    print("Opción no válida. Introduce un número del 1 al 5.")

        if __name__ == "__main__":
            main()
    elif opcion == '5':
        print("Saliendo...")
        time.sleep(1) 
        print("Saliendo...")
        time.sleep(1) 
        print("Saliendo...")
        time.sleep(1) 
        print("Gracias por jugar nuestro juego!")

        break
    else:
        
        print("Opción no válida. Por favor, selecciona una opción válida.")
        # Iván Ordoñez carnet: 1567523
        #Julio Cáceres carnet: 
