# Obtener la cantidad de elementos mayores a 5 en la tupla.

def mayor_a_cinco(elemento):
    return elemento >= 5


tupla = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)
resultado = tuple(filter(mayor_a_cinco, tupla))
print(resultado)

