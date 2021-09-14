﻿"""
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
assert cf




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
    print ("2. Listar cronológicamente los artistas")
    print ("3. Listar cronológicamente las adquisiciones.")
    print ("4. Clasificar las obras de un artista por técnica")
    print ("5. Clasificar las obras por la nacionalidad de sus creadores.")
    print ("6. Costo de transportar las obras de un departamento a otro")
    print ("7. Proponer una nueva exposción en el museo")
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
        catalog = initCatalog(tipolista)
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks']))) 
             
    elif int(inputs[0]) == 2:
        pass
    else:
        sys.exit(0)
sys.exit(0)
