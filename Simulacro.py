while True:
    print()
    print("Opción 1: Pedir dos números y devolver su suma.")
    print("Opción 2: Pedir un nombre y saludar a la persona.")
    print("Opción 3: Pedir un número y devolver su cuadrado.")
    print("Opción 4: Salir del programa.")
    print()
    try:
        opcion = int(input("OPCIÓN: "))
    except:
        opcion = -1
    if opcion == 1:
        print("opcion 1")
    elif opcion == 2:
        print("opcion 2")
    elif opcion == 3:
        print("opcion 3")
    elif opcion == 4:
        break
    else: 
        print("Opción incorrecta.")
print("\nFin del programa")