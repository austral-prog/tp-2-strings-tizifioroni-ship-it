def slice_advanced():
    """Lee un texto e imprime los caracteres desde la posición 4
    en adelante, tomando uno de cada dos (paso 2).
    """

    hello = input("Palabra: ")

    slice = hello[4::2]

    print(slice)

