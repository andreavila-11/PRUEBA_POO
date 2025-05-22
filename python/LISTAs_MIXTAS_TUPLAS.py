import numpy as np


lista_mixta = [10, "hola", 3.14, True, [1, 2, 3]]

lista_numerica = np.array([1, 2, 3, 4, 5])

tupla_mixta = tuple(lista_mixta)
tupla_numerica = tuple(lista_numerica)


conjunto_mixto = tuple (lista_mixta)  
conjunto_numerico = tuple (lista_numerica)


diccionario = {
    "nombre": "Andrea",
    "edad": 18,
    "estatura": 3.14,
    "estudiante": True,
    "materias": ["POO1", "Algebra", "Calculo" "IR"]
}

print("Lista mixta:", lista_mixta)
print("Lista numérica (numpy):", lista_numerica)
print("Tupla mixta:", tupla_mixta)
print("Tupla numérica:", tupla_numerica)
print("Conjunto mixto:", conjunto_mixto)
print("Conjunto numérico:",conjunto_numerico)
print("Diccionario:", diccionario)