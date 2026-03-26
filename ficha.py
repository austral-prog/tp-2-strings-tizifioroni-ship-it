

def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)



    nombre: str = input("Nombre: ")
    email = input("Email: ")
    nota_1 = int(input("Nota 1: "))
    nota_2 = int(input("Nota 2: "))
    nota_3 = int(input("Nota 3: "))
    nombre_limpio = nombre.strip().title()

    multilinea = """========================
    FICHA DEL ALUMNO
========================"""

    print(multilinea)
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email.lower()}")
    print(f"Caracteres en nombre: {len(nombre_limpio)}")
    encontrar = nombre_limpio.find(" ")
    iniciales = nombre_limpio[0] + nombre_limpio[encontrar + 1]
    print(f"Iniciales: {iniciales}")
    punto = nombre.lower()
    dado_vuelta = ".".join(punto.split()[::-1])
    punto_p = dado_vuelta.replace(" ", ".")
    print(f"Usuario: {punto_p}")
    print(f"Email valido: {"@" in email}")
    dominio = email.split('@', 1)[-1]
    print(f"Dominio: {dominio.lower()}")
    nombre_archivo = nombre_limpio.replace(" ", "_")
    print(f"Nombre para archivo: {nombre_archivo}")
    nombre_minusculas = nombre.lower()
    print(f"Cantidad de a: {nombre_minusculas.count('a')}")
    codigo = nombre_limpio [::-1]
    print(f"Codigo secreto: {codigo.upper()}")
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")
    print(f"Suma: {nota_1 + nota_2 + nota_3}")
    print(f"Promedio: {(nota_1 + nota_2 + nota_3) / 3}")
    print(f"Promedio entero: {(nota_1 + nota_2 + nota_3) // 3}")
    print("========================")


