from functools import reduce


lista = [1, 2, 3, 4]
def funcion_acumulador(acumulador=0, elemento=0):
    return acumulador + elemento


resultado = reduce(funcion_acumulador, lista)
print(resultado)


# Concatenar todos los elementos de la lista

lista = ['Python', 'Java', 'Ruby', 'Elixir']
resultado = reduce(lambda acumulador='',
                   elemento='': acumulador + " - " + elemento, lista)
print(resultado)
