"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from time import process_time
assert cf
import sys
from datetime import datetime

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

catalog = None
def printMenu():
    print ("Bienvenido")
    print ("1. Cargar archivos.")
    print ("2. Ordenar por orden de adquisición de las obras")
    print ("3. Listar cronológicamente los artistas")
    print ("4. Listar cronológicamente las adquisiciones.")
    print ("5. Clasificar las obras de un artista por técnica")
    print ("6. Clasificar las obras por la nacionalidad de sus creadores.")
    print ("7. Costo de transportar las obras de un departamento a otro")
    print ("8. Proponer una nueva exposción en el museo")
    print ("0. Salir")



def initCatalog(tipolista: str):
    """
    Inicializa el catalogo del museo
    """
    return controller.initCatalog(tipolista)

def loadData(catalog):
    """
    Carga los datos en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

def printsortartist(lista):
    for artists in lt.iterator(lista):
        print("Nombre: " + artists["DisplayName"])
        print("Fecha de Nacimiento: " + artists["BeginDate"])
        print("Fecha de fallecimiento: " + artists["EndDate"])
        print("Nacionalidad: " + artists["Nationality"])
        print("Género: " + artists["Gender"])
        print("-" * 100)

def printsortartworks(lista, listaartistas):
    print("-" * 100)
    for artworks in lt.iterator(lista):
        print ("Titulo: " + artworks["Title"])
        print ("Fecha: " + artworks["Date"])
        print ("Medio: " + artworks ["Medium"])
        print ("Dimensiones: " + artworks["Dimensions"])
        print ("Artistas: ")
        artworks["ConstituentID"] = artworks["ConstituentID"].replace(" ", "")
        artworks["ConstituentID"] = artworks["ConstituentID"].replace("[", "")
        artworks["ConstituentID"] = artworks["ConstituentID"].replace("]", "")
        if len(artworks["ConstituentID"]) > 4:
            lista = artworks["ConstituentID"].split(",")
            for artista in lista:
                posartista = lt.isPresent(listaartistas, artista)
                posartista = posartista - 1
                nombre = lt.getElement(listaartistas,posartista)
                nombre = nombre["DisplayName"]
                print (nombre)
            print ("-"*100)
        else: 
            posartista = lt.isPresent(listaartistas,artworks["ConstituentID"])
            posartista = posartista - 1
            nombre = lt.getElement(listaartistas, posartista)
            nombre = nombre["DisplayName"]
            print (nombre)
            print ("-"*100)


def agregarlistaartistas(listaartistas, listabuscar):
    listafinal = lt.newList(datastructure="ARRAY_LIST",cmpfunction=cmpfunctionlistaartistas)
    for artwork in lt.iterator(listabuscar):
        listaCI = artwork["ConstituentID"].split(",")
        for artist in listaCI:
            lt.addLast(listaartistas, artist)
    for artista in lt.iterator(catalog["artists"]):
        posartista = lt.isPresent(listaartistas, artista["ConstituentID"])
        if posartista > 0:
            lt.addLast(listafinal, artista)
            lt.addLast(listafinal, artista["ConstituentID"])
    return listafinal


def cmpfunctionlistaartistas (artist1,artist2):
    if artist1 in artist2:
        return 0
    else:
        return 1
        
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:
        print ("Escoja el tipo de lista que quiere utilizar: ")
        print ("1. Array List.\n2. Single Linked")
        num = int(input("Digite el número de estructura de la lista escogido: "))
        if num == 1:
            tipolista = "ARRAY_LIST"
        else:
            tipolista = "SINGLE_LINKED"
        print("Cargando información de los archivos ....")
        t1 = process_time()
        catalog = initCatalog(tipolista)
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks']))) 
        t2 = process_time()
        time = t2-t1
        print("El tiempo para cargar los archivos fue de:", str(time) , "s")     


    elif int(inputs[0]) == 2:
        sizesublist = int(input("Escoja el tamaño de la sublista: "))
        while lt.size(catalog["artworks"]) <= sizesublist:
            sizesublist = int(input("Escoja el tamaño de la sublista valido: "))
        print ("Escoja el tipo de ordenamiento a realizar:")
        print ("1. Insertion Sort.")
        print ("2. Shell Sort")
        print ("3. Merge Sort")
        print ("4. Quick Sorts")
        typeofsort = int(input("Si digita una opción invalida se escojerá por defecto quick sort: "))
        if typeofsort == 1: 
            typeofsort = "insertion"
        elif typeofsort == 2:
            typeofsort = "shell"
        elif typeofsort ==3:
            typeofsort = "merge"
        else:
            typeofsort = "quick"
        sortedartworkstime = controller.sortartworks(catalog,sizesublist,typeofsort)
        print(sortedartworkstime) 


    elif int(inputs[0]) == 3:   
        begin = int(input("Indique el año inicial del rango: "))
        end = int(input("Indique el año final del rango: "))
        a = len(str(begin))
        b = len(str(end))
        if a != 4:
            print("Inserte un año válido.")
        elif b != 4:
            print("Inserte un año válido.")
        elif begin > end:
            print("La fecha de fin no puede ser menor que la de inicio.")
        else:
            info = controller.sortartistsDates(catalog,begin,end)
            print("Hay un total de "+ str(info[0]) + " artistas entre " + str(begin)+ " - "+ str(end))   
            printsortartist(info[1]) 
            



    elif int(inputs[0]) == 4:
        begin = (input("Indique la fecha inicial del rango en formato numérico año-mes-día: "))
        end = (input("Indique la fecha final del rango en formato numérico año-mes-día: "))
        a = len(str(begin))
        b = len(str(end))
        datetime.strptime(end, "%Y-%m-%d")
        datetime.strptime(begin, "%Y-%m-%d")
        if a != 10:
            print("Inserte una fecha válida.")
        elif b != 10:
            print("Inserte una fecha válida.")
        elif begin > end:
            print("La fecha de fin no puede ser menor que la de inicio.")
        else:
            info = controller.sortartworks2(catalog,begin,end)
            print ("Numero de obras: " + str(info[0]))
            print ("Adquiridas por purchase: " + str(info[1]))
            listaartistas = lt.newList(datastructure= "ARRAY_LIST", cmpfunction= cmpfunctionlistaartistas)
            x = agregarlistaartistas(listaartistas, info[2])
            printsortartworks(info[2],x)
    elif int(inputs[0]) == 5:  
        artista = (input("Ingrese el nombre del artista de las obras a clasificar: "))    
        info = controller.artworksClasification(catalog, artista)
        tamaño_total_obras = lt.size(info)
        tamaño_medios = lt.newList(datastructure= "ARRAY_LIST")
        contadorif = 0
        contadorelse = 0
        for medio in lt.iterator(info):
            posicion = lt.isPresent(tamaño_medios,medio)
            if posicion == 0:
                contadorif += 1
                lt.addLast(tamaño_medios, medio)
                lt.addLast(tamaño_medios, str(1))
            else:
                contadorelse += 1
                x = lt.getElement(tamaño_medios, (posicion + 1))
                x = int(x) + 1
                x = str(x)
                lt.deleteElement(tamaño_medios, posicion+1)
                lt.insertElement(tamaño_medios, x, posicion+1)
        # Imprimir tamaño_medios
        for x in lt.iterator(tamaño_medios):
            print (x)
    else:
        sys.exit(0)
sys.exit(0)
