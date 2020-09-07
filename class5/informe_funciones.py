from pprint import pprint
import sys
import csv
import fileparse

# leer_camion abre un archivo con el contenido de un camión,
# lo lee y devuelve la información como una lista de tuplas


def leer_camion(filename):
    '''Abre un archivo con el contenido de un camión, 
    lo lee y devuelve la información como una lista de tuplas'''

    truckLoad = fileparse.parse_csv(filename, has_headers=False)
    return truckLoad[1:]


def leer_precios(filename):
    '''A partir de un conjunto de precios como éste arme un diccionario donde las claves
    sean los nombres de frutas y verduras, y los valores sean los precios por cajón.'''
    
    list_of_lists = fileparse.parse_csv(filename, has_headers=False, types=[str, float])
    dictionary = {}
    
    for single_list in list_of_lists:
      dictionary[single_list[0]] = single_list[1]

    return dictionary


# completa el programa para que con los precios del camión (Ejercicio 2.13) y los de venta
# en el negocio (Ejercicio 2.14) calcule lo
# que costó el camión, lo que se recaudo con la venta, y la diferencia. ¿Hubo
# ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.

def calcular_gastos(dataCostoCamion, tablaDePrecios):
    costoTotal = 0
    headings = dataCostoCamion[0]
    for cajones in dataCostoCamion:
        try:
            cajonesFormat = dict(zip(headings, cajones))
            costoTotal += int(cajonesFormat['cajones']) * \
                float(cajonesFormat['precio'])
        except:
            pass

    facturacionTotal = 0
    for cajones in dataCostoCamion:
        try:
            cajonesFormat = dict(zip(headings, cajones))
            facturacionTotal += int(cajonesFormat['cajones']) * \
                tablaDePrecios[cajonesFormat['nombre']]
        except:
            pass
    gananciaNeta = round(facturacionTotal - costoTotal, 2)

    print(f'En total se gasto {costoTotal} y se facturó\
    {facturacionTotal} dejando una ganancia neta de\
    {gananciaNeta} \n')
    return facturacionTotal, gananciaNeta


def hacer_informe(cajones, precios):
    tabla = []
    for cajon in cajones[1:]:
        accu = (cajon[0], int(cajon[1]), float(cajon[2]), precios[cajon[0]],
                precios[cajon[0]] - float(cajon[2]))
        tabla.append(accu)
    return tabla


def imprimir_informe(dataCostoCamion, tablaDePrecios):
    headers = ('Nombre', 'Cajones', 'Precio', 'Precio Venta', 'Cambio')
    print('%15s %15s %15s %15s %15s' % headers)
    print('   ------------ '*5)
    for row in hacer_informe(dataCostoCamion, tablaDePrecios):
        print('%15s %15d $%15.2f $%15.2f $%15.2f' % row)


def informe_camion(dataCamion, dataPrecios):
    imprimir_informe(leer_camion(dataCamion),
                     leer_precios(dataPrecios))


informe_camion('../Data/camion.csv', '../Data/precios.csv')
