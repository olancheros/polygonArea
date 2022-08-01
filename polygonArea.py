import os
def clear(): return os.system('cls')
clear()

from cProfile import label
import matplotlib.pyplot as plt
import turtle
import math
from colorama import init, Fore
init(autoreset=True)

'''
    --------------Function to calculate the area and plot a Regular Polygon----------------
'''

def areaRegPolygon(nSides, lSide):
    nSides = numberSides
    lSide = lengthSide

    alpha = 360 / nSides

    beta = math.radians(alpha / 2)
    beta = round(beta, 8)

    tanBeta = math.tan(beta)
    tanBeta = round(tanBeta, 3)

    apothem = lSide / (2 * tanBeta)
    apothem = round(apothem, 2)

    areaPolygon = nSides * lSide * apothem / 2
    areaPolygon = round(areaPolygon, 2)

    return print(Fore.LIGHTBLUE_EX+'\nEl área del polígono es:', areaPolygon, Fore.LIGHTBLUE_EX+'unidades cuadradas\n')


def plotPolygon(nSides):
    turtle.resetscreen()
    turtle.setup(0.75,0.75,None,None)
    turtle.screensize(3600, 3600)
    nSides = numberSides
    turtle.title("Polígono Regular de " + str(nSides) + " lados")
    turtle.hideturtle()
    turtle.fillcolor('green')
    angle = 180 - (nSides - 2) * 180 / nSides
    turtle.begin_fill()
    for i in range(nSides):
        turtle.forward(50)
        turtle.right(angle)
    turtle.end_fill()
    turtle.done()

'''
    ------------Function to calculate the area and plot an Irregular Polygon--------------
'''

def areaIrregPolygon(xCoord, yCoord, nSides):
    area = 0.0
    j = nSides - 1
    for i in range(0, nSides):
        area += (xCoord[j] + xCoord[i]) * (yCoord[j] - yCoord[i])
        j = i
    return(print(Fore.LIGHTBLUE_EX+'\nEl área del polígono irregular de', nSides, Fore.LIGHTBLUE_EX+'lados es:', abs(area / 2.0), Fore.LIGHTBLUE_EX + 'unidades cuadradas\n'))


def plotIrregPolygon(xCoord, yCoord, nSides):
    xCoord.insert(len(xCoord), xCoord[0])
    yCoord.insert(len(yCoord), yCoord[0])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(xCoord, yCoord)
    plt.title("Polígono Irregular de " +str(nSides)+ " lados")
    plt.show()

'''
    ----------------------------------Main Program---------------------------------------
'''

print()
print('='*80)
print('')
print(' '*20 +Fore.RED + 'Cálculo del área de un polígono de n lados\n')
print(' '*12 + Fore.RED + 'Para el caso de un polígono regular, se usa la ecuación: ')
print(' '*18 + Fore.RED + 'areaPolygon = (nSides * lSide * apothem) / 2')
print('')
print(' '*7 + Fore.RED + 'Para el caso de un polígono irregular, se usa el algorítmo de Gauss')
print(' '*8 + Fore.RED + 'luego el polígono debe estar proyectado sobre un Plano Cartesiano')
print('')
print('='*80)

print ('\nMenú para seleccionar tipo de polígono')
print ('')
print ('Polígono Regular:   1')
print ('Polígono Irregular: 2')
print ('')

select = input('Ingrese su selección: ')

options = ['1', '2']

try:
    if select not in options:
        print('\nSelección no válida, por favor intente de nuevo\n')
except:
    exit()

if select == '1':
    numberSides = int(input('\n    Ingrese el número de lados del polígono: '))
    lengthSide = float(input('\n    Ingrese la longitud del lado del polígono: '))

    areaRegPolygon(numberSides, lengthSide)
    plotPolygon(numberSides)

elif select == '2':
    xCoord = []
    yCoord = []
    nSides = int(input('\n    Ingrese el número de lados del polígono: '))
    print('\n    Ingrese los', nSides, 'pares de coordenadas x,y del polígono\n')

    for i in range(nSides):
        xVal = int(input("    x{} : ".format(i+1)))
        xCoord.append(xVal)
        yVal = int(input("    y{} : ".format(i+1)))
        yCoord.append(yVal)

    areaIrregPolygon(xCoord, yCoord, nSides)
    plotIrregPolygon(xCoord, yCoord, nSides)
