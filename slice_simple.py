def slice_simple():
    """Dado el texto 'Awesome', imprime distintos substrings
    usando slicing y lower().
    """
    texto = "Awesome"

    sliced_texto = texto[0:3]
    print(sliced_texto.lower())

    sliced_texto = texto[2:5]
    print(sliced_texto.lower())

    print(texto.lower())

