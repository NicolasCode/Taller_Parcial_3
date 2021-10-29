import numpy as np  # libreria para usar matrices


def f(x):  # declaracion de la funcion
    return np.e**x - (x * np.sin(x))


# declaracion del error 10^-3
error = 10**-3

# declaracion de los limites, ak=inferior, bk=superior
ak = -2
bk = 1

# declaracion de un contador para calcular el numero de iteraciones
count = 0

# declaracion de las tablas
table1 = [["k", "ak", "bk", "pk"]]
table2 = [["k", "f(ak)", "f(bk)", "f(pk)"]]

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
        " " * (12 - len(str(i[1]))),
        "|",
        " " * (2),
        i[2],
        " " * (15 - len(str(i[2]))),
        "|",
        " " * (1),
        i[3],
        " " * (17 - len(str(i[3]))),
        "|"
    )
print("===============================================================================", '\n')
print("=====================================================================================================")
print("                                             Datos 2")
print("=====================================================================================================")
for i in Data2:
    print(
        "|",
        " " * (3),
        i[0],
        " " * (6 - len(str(i[0]))),
        "|",
        " " * (2),
        i[1],
        " " * (21 - len(str(i[1]))),
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
print("=====================================================================================================\n")

# Imprimir el c aproximado
print("========================================================")
print("                        Output")
print("========================================================")
print("el valor aproximado de c es: ", pk)
print("el valor aproximado de f(c) es: ", tpk)
print("========================================================")
