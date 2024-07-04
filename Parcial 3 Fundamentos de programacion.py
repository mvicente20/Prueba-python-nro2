# Definición de la clase Reserva
class Reserva:
    def __init__(self, nombre, ciudad_origen, tour, cantidad_personas):
        self.nombre = nombre
        self.ciudad_origen = ciudad_origen
        self.tour = tour
        self.cantidad_personas = cantidad_personas

    def __str__(self):
        # Formato de salida de la reserva
        return f"{self.nombre} {self.ciudad_origen} {self.tour} {self.cantidad_personas}"


# Lista para almacenar las reservas
reservas = []

# Lista de destinos disponibles
destinos = ["Torres del Paine", "Carretera Austral", "Chiloé"]

# Función para registrar una nueva reserva
def registrar_reserva():
    # Solicitar los datos del cliente
    nombre = input("Nombre del cliente: ")
    apellido = input("Apellido del cliente: ")
    ciudad_origen = input("Ciudad de origen: ")

    # Mostrar las opciones de tours
    print("Seleccione un tour:")
    for i, destino in enumerate(destinos, 1):
        print(f"{i}. {destino}")

    # Solicitar la selección del tour y la cantidad de personas
    tour_index = int(input("Ingrese el número del tour: ")) - 1
    cantidad_personas = int(input("Cantidad de personas: "))

    # Validar que todos los datos sean válidos
    if nombre and apellido and ciudad_origen and 0 <= tour_index < len(destinos) and cantidad_personas > 0:
        # Crear una nueva reserva y agregarla a la lista
        reserva = Reserva(f"{nombre} {apellido}", ciudad_origen, destinos[tour_index], cantidad_personas)
        reservas.append(reserva)
        print("Reserva registrada con éxito.")
    else:
        print("Error: Todos los datos son requeridos y deben ser válidos.")

# Función para listar todas las reservas
def listar_reservas():
    # Comprobar si hay reservas registradas
    if reservas:
        # Mostrar todas las reservas
        for reserva in reservas:
            print(reserva)
    else:
        print("No hay reservas registradas.")

# Función para imprimir el detalle de las reservas por destino
def imprimir_detalle_por_destino():
    # Mostrar las opciones de destinos
    print("Seleccione un destino para imprimir el detalle de las reservas:")
    for i, destino in enumerate(destinos, 1):
        print(f"{i}. {destino}")

    # Solicitar la selección del destino
    tour_index = int(input("Ingrese el número del destino: ")) - 1

    # Validar la selección del destino
    if 0 <= tour_index < len(destinos):
        destino_seleccionado = destinos[tour_index]
        # Crear y abrir un archivo de texto para el destino seleccionado
        with open(f"reservas_{destino_seleccionado}.txt", "w") as file:
            # Escribir las reservas correspondientes al destino en el archivo
            for reserva in reservas:
                if reserva.tour == destino_seleccionado:
                    file.write(str(reserva) + "\n")
        print(f"Detalle de reservas para {destino_seleccionado} impreso en 'reservas_{destino_seleccionado}.txt'.")
    else:
        print("Destino inválido.")

# Función para mostrar el menú principal
def mostrar_menu():
    print("\nMenú:")
    print("1. Registrar Reserva")
    print("2. Listar Todas las Reservas")
    print("3. Imprimir Detalle de Reservas por Destino")
    print("4. Salir")

# Función principal del programa
def main():
    while True:
        # Mostrar el menú y solicitar la opción del usuario
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # Ejecutar la función correspondiente según la opción seleccionada
        if opcion == "1":
            registrar_reserva()
        elif opcion == "2":
            listar_reservas()
        elif opcion == "3":
            imprimir_detalle_por_destino()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

# Ejecutar la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()