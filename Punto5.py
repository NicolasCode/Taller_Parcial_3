# github : https://github.com/NicolasCode/Taller_Parcial_3.git

import numpy as np  # libreria para usar matrices y operaciones matematicas
import matplotlib.pyplot as plt  # libreria para graficar las funciones


def f(x):  # declaracion de la funcion
    # le restamos 2 a la funcion para trasladarla
    return (np.log(x) - (x * np.cos(x))) - 2


# declaracion del error 10^-3
error = 10**-3

# declaracion de los limites, ak=inferior, bk=superior
ak = 1
bk = 4

# declaracion de un contador para calcular el numero de iteraciones
count = 0

# declaracion de las tablas
table1 = [["k", "ak", "bk", "pk"]]
table2 = [["k", "f(ak)", "f(bk)", "f(pk)"]]

# declaramos'X' en un rango en el que podamos apreciar la funcion y obtenemos 'Y' para ese rango
x = np.array(range(1000))*0.01
y = [f(i) for i in x]

# Ciclo hasta obtener la aproximacion de c
while bk-ak > error:

    count -= - 1  # aumentar el contador por cada iteracion
    pk = (ak + bk)/2  # punto medio

    tak = f(ak)
    tbk = f(bk)
    tpk = f(pk)

    # Insercion de una nueva fila a la matriz
    table1.append([count, ak, bk, pk])
    table2.append([count, tak, tbk, tpk])

    # teorema de localizacion de raices aplicado a la mitad del intervalo
    if (tpk * tbk < 0):
        ak = pk
    else:
        bk = pk

    # Graficar los axis
    plt.plot([i for i in range(-3, 12)], [0 for i in range(15)], color="black")
    plt.plot([0 for i in range(30)], [
             i for i in range(-10, 20)], color="black")

    # grafucamos la funcion
    plt.plot(x, y, color="green")

    # graficamos los extremos del intervalo
    plt.plot([ak for i in range(30)], [
             i for i in range(-10, 20)], color="red")
    plt.plot([bk for i in range(30)], [
             i for i in range(-10, 20)], color="blue")

    # mostramos las graficas
    plt.title("Iteracion " + str(count))
    plt.show()

# Convertir las tablas en matrcies
Data1 = np.array(table1)
Data2 = np.array(table2)

# imprimir las matrices
print("===============================================================================")
print("                               Datos 1")
print("===============================================================================")
for i in Data1:
    print(
        "|",
        " " * (3),
        i[0],
        " " * (6 - len(str(i[0]))),
        "|",
        " " * (2),
        i[1],
        " " * (14 - len(str(i[1]))),
        "|",
        " " * (2),
        i[2],
        " " * (15 - len(str(i[2]))),
        "|",
        " " * (1),
        i[3],
        " " * (15 - len(str(i[3]))),
        "|"
    )
print("===============================================================================", '\n')
print("=======================================================================================================")
print("                                             Datos 2")
print("=======================================================================================================")
for i in Data2:
    print(
        "|",
        " " * (3),
        i[0],
        " " * (6 - len(str(i[0]))),
        "|",
        " " * (2),
        i[1],
        " " * (23 - len(str(i[1]))),
        "|",
        " " * (2),
        i[2],
        " " * (22 - len(str(i[2]))),
        "|",
        " " * (1),
        i[3],
        " " * (23 - len(str(i[3]))),
        "|"
    )
print("=======================================================================================================\n")

# Imprimir el c aproximado
print("========================================================")
print("                        Output")
print("========================================================")
print("el valor aproximado de c es: ", pk)
# le sumamos 2 para obtener el valor de la funcion antes de ser trasladada
print("el valor aproximado de f(c) es: ", tpk + 2)
print("========================================================")
