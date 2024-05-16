def ingresar_datos_trabajador():
    nombre = input("Ingrese el nombre del trabajador: ")
    while not nombre or len(nombre) > 30:
        print("El nombre no puede estar vacío y debe tener máximo 30 caracteres.")
        nombre = input("Ingrese el nombre del trabajador: ")

    while True:
        try:
            sueldo_base = float(input("Ingrese el sueldo base del trabajador: "))
            if sueldo_base <= 0:
                print("El sueldo base debe ser un valor numérico positivo.")
            else:
                break
        except ValueError:
            print("El sueldo base debe ser un valor numérico.")

    while True:
        try:
            horas_extras = float(input("Ingrese el número de horas extras trabajadas: "))
            if horas_extras < 0:
                print("El número de horas extras debe ser un valor numérico positivo.")
            else:
                break
        except ValueError:
            print("El número de horas extras debe ser un valor numérico.")

    return nombre, sueldo_base, horas_extras

def calcular_liquidacion(sueldo_base, horas_extras):
    pago_horas_extras = horas_extras * (sueldo_base / 160) * 1.5
    total_ingresos = sueldo_base + pago_horas_extras
    descuento_fonasa = total_ingresos * 0.07
    descuento_afp = total_ingresos * 0.1
    sueldo_neto = total_ingresos - descuento_fonasa - descuento_afp
    return pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto

def mostrar_desglose(nombre, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto):
    print("\n=== Desglose de Liquidación ===")
    print("Nombre del trabajador:", nombre)
    print("Sueldo base:", sueldo_base)
    print("Pago por horas extras:", pago_horas_extras)
    print("Total de ingresos:", total_ingresos)
    print("Descuento por FONASA (7%):", descuento_fonasa)
    print("Descuento por AFP (10%):", descuento_afp)
    print("Sueldo neto a pagar:", sueldo_neto)

def generar_archivo(nombre, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto):
    nombre_archivo = f"liquidacion_{nombre}.txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write("=== Desglose de Liquidación ===\n")
        archivo.write(f"Nombre del trabajador: {nombre}\n")
        archivo.write(f"Sueldo base: {sueldo_base}\n")
        archivo.write(f"Pago por horas extras: {pago_horas_extras}\n")
        archivo.write(f"Total de ingresos: {total_ingresos}\n")
        archivo.write(f"Descuento por FONASA (7%): {descuento_fonasa}\n")
        archivo.write(f"Descuento por AFP (10%): {descuento_afp}\n")
        archivo.write(f"Sueldo neto a pagar: {sueldo_neto}\n")
    print(f"Se ha generado el archivo {nombre_archivo}")

while True:
    nombre, sueldo_base, horas_extras = ingresar_datos_trabajador()
    pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto = calcular_liquidacion(sueldo_base, horas_extras)
    mostrar_desglose(nombre, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)
    generar_archivo(nombre, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)

    respuesta = input("¿Desea calcular la liquidación para otro trabajador? (s/n): ")
    if respuesta.lower() != "s":
        break