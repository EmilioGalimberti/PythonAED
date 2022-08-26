# Turno 02 – Enunciado 04 [T2E4]:
#
# Desarrolle un programa completo en Python, controlado por menú de opciones, que incluya las siguientes opciones:
#
# 1.) Ingrese por teclado las temperaturas de tres cámaras frigoríficas, tomadas durante el día,
# y el identificador o nombre de cada cámara (tres cadenas de caracteres). Informe el nombre de la camára con la temperatura mayor,
# el nombre de la cámara con la temperatura menor, y la diferencia entre la mayor y la menor.
#
# 2.) Ingrese por teclado una cadena de caracteres. Procese esa cadena a razón de un caracter por vuelta de ciclo,
# y determine cuántos de los caracteres eran letras mayúsculas. Informe también si apareció algún dígito
# (algún valor entre el '0' y el '9') en la cadena.
# Y finalmente muestre cuál es el porcentaje de dígitos encontrados respecto del total de caracteres de la cadena.
#
# 3.) Terminar el programa.

print('      Primer Parcial - Juan Pablo Díaz - 1K05 - 90950')
print('=' * 60)

menu = 'Menu de Opciones\n' \
       '-----------------------------------------\n' \
       '1 ------ Cámaras Frigoríficas\n' \
       '2 ------ Procesar Cadena de Caracteres\n' \
       '3 ------ Salir\n' \
       'Ingrese su opcion: '

opcion = 0
while opcion != 3:
    opcion = int(input(menu))
    if opcion == 1:

        cam1 = input("\nIngrese el nombre de la primer cámara: ")
        tmp1 = int(input("Ingrese la temperatura de la cámara " + str(cam1) + ": "))

        cam2 = input("\nIngrese el nombre de la segunda cámara: ")
        tmp2 = int(input("Ingrese la temperatura de la cámara " + str(cam2) + ": "))

        cam3 = input("\nIngrese el nombre de la tercer cámara: ")
        tmp3 = int(input("Ingrese la temperatura de la cámara " + str(cam3) + ": "))

        # Búsqueda de la cámara con mayor temperatura
        if tmp1 > tmp2 and tmp1 > tmp3:
            may = tmp1
            print("\n>> La cámara con mayor temperatura es: " + str(cam1), sep="")
        elif tmp2 > tmp3:
            may = tmp2
            print("\n>> La cámara con mayor temperatura es: " + str(cam2), sep="")
        else:
            may = tmp3
            print("\n>> La cámara con mayor temperatura es: " + str(cam3), sep="")

        # Búsqueda de la cámara con menor temperatura
        if tmp1 < tmp2 and tmp1 < tmp3:
            men = tmp1
            print("\n>> La cámara con menor temperatura es: " + str(cam1), sep="")
        elif tmp2 < tmp3:
            men = tmp2
            print("\n>> La cámara con menor temperatura es: " + str(cam2), sep="")
        else:
            men = tmp3
            print("\n>> La cámara con menor temperatura es: " + str(cam3), sep="")

        # Cálculo de diferencia entre temperaturas
        diferencia = may - men
        print("\n>> La diferencia entre la camara con mayor temperatura y la de menor temperatura es: ", diferencia, "°", sep="")

    elif opcion == 2:
        texto = input("Ingrese la cadena de caracteres a procesar: ")
        cont_mayus = 0
        digitos = "0123456789"
        cont_digitos = 0
        cont_caracteres = 0
        for car in texto:
            cont_caracteres = cont_caracteres + 1
            # Conteo de cuantos caracteres son mayusculas
            if car > "A" and car < "Z":
                cont_mayus = cont_mayus + 1
            # Conteo de la cantidad de dígitos
            elif car in digitos:
                cont_digitos = cont_digitos + 1

        # Cálculo de porcentaje respecto a caracteres
        porcentaje = cont_digitos * 100 / cont_caracteres

        print("\n>> Hay ", cont_mayus, " caracteres que son mayúsculas.", sep="")
        if cont_digitos > 0:
            print("\n>> Si aparecieron dígitos en la cadena", sep="")
        print("\n>> Los dígitos encontrados representan un ", round(porcentaje, 2), "% del total de caracteres.", sep="")






