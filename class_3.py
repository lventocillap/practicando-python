clientes = 5

for i in range(clientes):
    print("Cliente", i+1)
    
    dni = input("Ingrese su DNI: ")
    
    print("Tipos de servicios disponibles:")
    print("1. Servicio 30 megas - S/ 80")
    print("2. Servicio 50 megas - S/ 110")
    print("3. Servicio 100 megas - S/ 150 con 5'%' de descuento")
    
    tipo_servicio = int(input("Seleccione el tipo de servicio (1, 2 o 3): "))
    
    match tipo_servicio:
        case 1:
            monto = 80
        case 2:
            monto = 110
        case 3:
            monto = 150 * 0.05
        case _:
            monto = 0
            print("Opción no válida")

    if tipo_servicio >= 1 and tipo_servicio <= 3:
        print(f"El monto a pagar por el cliente {dni} es: S/ {monto:.2f}")
    