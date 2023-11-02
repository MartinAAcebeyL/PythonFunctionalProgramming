# lambda argumentos : cuerpo de la función


def suma_2_numeros(val1,val2): 
    return val1+val2

# lambda para suma de 2 numeros
suma = lambda val1, val2: val1 + val2
print(suma(4,5))#9


# lambda para suma de N numeros
suma_de_n_numeros = lambda l:sum(l)
print(suma_de_n_numeros([45,6,89]))

    
# Usar una funcion anonima para ordenar las tuplas por el 2do elemento
tuplas = [(1, 2), (5, 1), (8, 10), (3, 3)]
tuplas_ordenadas = sorted(tuplas, key=lambda x: x[1])
print(tuplas_ordenadas)
