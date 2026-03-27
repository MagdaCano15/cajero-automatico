print("---- BIENVENIDO(A) AL CAJERO AUTOMATICO ----")

# Datos iniciales
pin_secreto = 1234
saldo = 100000
nombre = "Magda"
intentos = 0
es_usuario_valido = False

# Nuevas funcionalidades
historial = []              # Guarda movimientos
limite_diario = 50000       # Límite de retiro diario
retirado_hoy = 0            # Control de retiro diario

# Validación de PIN
while intentos < 3 and not es_usuario_valido:
    try:
        entrada = int(input(f"Intento {intentos+1}/3 - Ingrese su PIN: "))

        if entrada == pin_secreto:
            print(f"\nBienvenido(a) {nombre}!")
            es_usuario_valido = True
            historial.append("Inicio de sesión exitoso")
        else:
            print("PIN incorrecto")
            intentos += 1

    except ValueError:
        print("Error: debe ingresar solo números")

# Menú principal
if es_usuario_valido:
    opcion = ""

    while opcion != "5":
        print("\n" + "=" * 25)
        print(f"SALDO ACTUAL: ₡{saldo}")
        print(f"RETIRADO HOY: ₡{retirado_hoy} / ₡{limite_diario}")
        print("=" * 25)
        print("1. Consultar saldo")
        print("2. Retirar efectivo")
        print("3. Depositar fondos")
        print("4. Ver historial")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        # 1. Consultar saldo
        if opcion == "1":
            print(f">> Su saldo disponible es: ₡{saldo}")
            historial.append("Consulta de saldo")

        # 2. Retirar efectivo
        elif opcion == "2":
            try:
                retiro = int(input("Ingrese monto a retirar: ₡"))

                if retiro <= 0:
                    print("Error: monto inválido")

                elif retiro > saldo:
                    print("Error: fondos insuficientes")

                elif retiro % 1000 != 0:
                    print("Error: solo se permiten múltiplos de ₡1000")

                elif retirado_hoy + retiro > limite_diario:
                    print("Error: supera el límite diario de retiro")

                else:
                    saldo -= retiro
                    retirado_hoy += retiro
                    historial.append(f"Retiro realizado: ₡{retiro}")
                    print(f"Retiro exitoso. Nuevo saldo: ₡{saldo}")

            except ValueError:
                print("Error: debe ingresar un número válido")

        # 3. Depositar fondos
        elif opcion == "3":
            try:
                deposito = int(input("Ingrese monto a depositar: ₡"))

                if deposito > 0:
                    saldo += deposito
                    historial.append(f"Depósito realizado: ₡{deposito}")
                    print(f"Depósito exitoso. Nuevo saldo: ₡{saldo}")
                else:
                    print("Error: el depósito debe ser mayor que cero")

            except ValueError:
                print("Error: debe ingresar un número válido")

        # 4. Ver historial
        elif opcion == "4":
            print("\n--- HISTORIAL DE TRANSACCIONES ---")
            if not historial:
                print("No hay movimientos registrados.")
            else:
                for movimiento in historial:
                    print("-", movimiento)

        # 5. Salir
        elif opcion == "5":
            print("¡Gracias por usar nuestro cajero!")
            historial.append("Salida del sistema")

        # Opción inválida
        else:
            print("Opción inválida. Intente de nuevo.")

# Acceso denegado
else:
    print("\nACCESO DENEGADO")
