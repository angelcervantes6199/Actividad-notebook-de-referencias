#en este caso no importa cual de las variables se modifique una afecta a la otra.

x = []
x1 = x
x2 = x1 


while True:
    print("Opciones: 1 agregar a x1, 2 agregar a x2 y 3 salir")
    opcione = int(input("$: "))
    if opcione == 3:
        break
    agregar = input("agrega algo:")
    if opcione == 1:
        x1.append(agregar) 
    elif opcione == 2:
        x2.append(agregar)
    else:
        print("opcion invalidad intenta del 1 al 3")
    print(x)
    print("ID de x:", id(x))
    print("ID de x1:", id(x1))
    print("ID de x2:", id(x2))

