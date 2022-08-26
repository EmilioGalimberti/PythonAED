from fun import *
from plantas import *

def menu():
    print('1- Cargar')
    print('2- Mostrar/ filtrar por monto minimo')
    print('3- Stock por tipo de plantas')
    print('4- Promedio de plantas disponibles')
    print('5- Buscar por número de identificación')
    print('6- Salir')
    return

def main():

    plantas = None
    opcion = 0

    while opcion != 6:
        menu()
        opcion = int(input('Ingrese la opcion: '))

        if opcion == 1:
            n = int(input('Ingrese la cantidad de plantas '))
            plantas = carga_plantas(n)
        elif opcion == 2:
            if plantas:
             ordenar(plantas)
             mostrar_plantas('Todos las plantas disponibles son', plantas)
             x = int(input('Ingrese el valor de importe de stock que quiera filtrar: '))
             filtrado = filtrar_tipo_importe(plantas,x)
             mostrar_plantas('Listado de alquileres que cumplen con la condicon',filtrado)
            else:
                print('Debe cargar las plantas!')
        elif opcion == 3:
            if plantas:
                totales = acumular_disponibles(plantas)
                for i in  range(len(totales)):
                    if totales[i] != 0 : #evita que se muestren valores con 0
                        print('Stock acumulados para el tipo', i , ':$', totales[i])
            else:
                print('Debe cargar las plantas!')
        elif opcion == 4:
            if plantas:
                x = int(input('ingrese  un valor para saber si  debe realizarse un control de stock de las plantas: '))
                promedio = promedio_disponibles(plantas)
                if promedio < x:
                    print('Debe realizarse un control de stock de las plantas ', round(promedio))
                else:
                    print('NO Debe realizarse un control de stock de las plantas ', round(promedio))
            else:
                print('Debe cargar las plantas!')
        elif opcion == 5:
                x = int(input('Ingrese el numero de identifiacion que desea busacar: '))
                encontrado = buscar(plantas,x)
                if encontrado:
                    print(to_string(encontrado))
                else:
                    print('No se encontro ')
if __name__ == '__main__':
    main()
