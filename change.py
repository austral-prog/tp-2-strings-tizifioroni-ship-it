def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass

    gasto = float(input())
    dinero_recibido = int(input())

    print("Ingresar gasto:")  #67.4
    print(gasto)
    print("Dinero recibido") #200
    print(dinero_recibido)
    #print("\nVuelto\n")
    print("")
    print("Vuelto")
    print("")
    vuelto = dinero_recibido - gasto #132.6
    pesos = int(vuelto)
    print("Pesos:")
    centavos = round((vuelto - pesos) * 100)
    print("Centavos:")
    print(centavos)

