from plantas import *

import random

#CARGA DE PLANTAS
nombres = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] #vector con descripciones para que puede elegir una descripcion alateoria el programa

def carga_plantas(n):  #carga automatica
    v = [None] * n
    for i in range(n):
        num = random.randint(1,10)
        nombre = random.choice(nombres)
        tipo = random.randint(0,18)
        importe = random.uniform(10,100)
        disponibles = random.randint(0,10)
        v[i] = planta(num, nombre, tipo, importe, disponibles)
    return v

def mostrar_plantas (titulo, v):     #siempre va a ser igual para mostrar un vector completo
    print(titulo)
    print('-'* len(titulo))
    for plantas in v:
        print(to_string(plantas))


#2) orden

def ordenar(v): #para ordenar va a ser siempre igual de forma directa de menor  a mayor
    n = len(v) # n = 4
    # 1er ciclo se utiliza para considerar el elemento pivot en la pasada.
    for i in range(n-1):# Rango: 0 1 2
        # 2do ciclo se utiliza para comparar con los demás elementos del arreglo.
        for j in range(i+1, n): # Rango: 1 2 3 \ es i+1 porque no toma en cuneta el pivot
            if v[i].nombre > v[j].nombre: # v[i]=pivot v[j]:elem. actual con el cual estoy comparando. en este caso comporamos los importes para el punto 2)
               v[i] , v[j] = v[j] , v[i] # Intercambio.-

#filtrado
def filtrar_tipo_importe(v,x):
    filtrado = []

    for plan in v:
        if (plan.precio)*(plan.disponibles) > x:
            filtrado.append(plan)

    return filtrado


#3)
def acumular_disponibles(v):
    acumulador = [0] * 19
    for plan in  v:
        acumulador[plan.tipo] += plan.disponibles  #tiene en cuenta de que tipo y acumula son honorarios
    return acumulador

#4)
def promedio_disponibles(v): #promedio general de un vector
    suma = 0
    # por cada alq del vector v hago tal cosa, alq se puede cambiar por cualquier otra variable
    for alq in v:                                                                               #este for es para un recorrido comun de 0 a
        suma += alq.disponibles
    return suma / len(v)


# 5)
def buscar(v,x):
    for alq in v:
        if alq.numero == x:
            return alq
    return None
