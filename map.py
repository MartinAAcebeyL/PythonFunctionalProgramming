# Obtener el cuadrado de todos los elementos en la lista.
def cuadrado(elemento=0):
    return elemento * elemento


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = list(map(cuadrado, lista))
print(resultado)

#usando lambda

cuadrado = lambda elemento: elemento*elemento
resultado = list(map(cuadrado, lista))
print(resultado)




# si es par o no

numeros = [1, 2, 3, 4, 5, 6, 7, 45, 69]
es_par = lambda elemento: elemento%2==0
resultado=list(map(es_par, lista))
print(numeros)
print(resultado)