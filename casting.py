def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio = int(input("Precio: "))
    descuento = int(input("Descuento: "))
    cantidad = int(input("Cantidad: "))
    total = precio - descuento
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio - descuento}")
    print(f"Total: {total * cantidad}")

