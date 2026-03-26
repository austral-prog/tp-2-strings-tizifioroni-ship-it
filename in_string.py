def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input("Ingresá su nombre: ")
    nombre_minusculas = nombre.lower()

    print(f"Contiene a: {'a' in nombre_minusculas}")
    print(f"Contiene e: {'e' in nombre_minusculas}")
    print(f"Contiene i: {'i' in nombre_minusculas}")
    print(f"Contiene o: {'o' in nombre_minusculas}")
    print(f"Contiene u: {'u' in nombre_minusculas}")


