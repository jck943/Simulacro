# Simulacro

## Índice
1. [Crear el menú](#Menu)
2. [Primera función](#Primera)
2. [Segunda función](#Segunda)
3. [Tercera función](#Tercera)
4. [Resumen](#Resumen)

## Crear el menú
Los primeros pasos para crear el *menú* has sido:
1. Hacer un `while True` para que el menú este en **bucle** 
2. Hacer un `print` de cada opción 
3. Hacer un `try except` para comprobar si la opción era correcta
4. Mandar al usuario a su respectiva función con un `if, elif y else`
El código que he utilizado ha sido el siguiente: 
```py
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
```
> Después de este avance voy a hacer un ***`git push origin`*** con su respectivo ***`git add.`*** y su "foto" ***`git commit -m "mensaje"`***

## Primera función