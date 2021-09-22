"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import isPresent
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf
from datetime import datetime
import time
import controller

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog(tipolista: str):
    catalog = {'artists': None,
               'artworks': None,
               }
    catalog["artists"] = lt.newList(tipolista,cmpfunction= compareartists)
    catalog["artworks"] = lt.newList(tipolista)

    return catalog

def addArtwork(catalog, artwork):  
    lt.addLast(catalog["artworks"], artwork)

def addArtists(catalog,artist):
    lt.addLast(catalog["artists"], artist)

def compareartists(artistname1, artist):
    if (artistname1.lower() in artist['ConstituentID'].lower()):
        return 0
    return 1

def cmpArtworkByDateAcquired(artwork1, artwork2):
    if artwork1["DateAcquired"] == None or artwork1["DateAcquired"] == "":
        artwork1["DateAcquired"] = "0001-01-01"
    if artwork2["DateAcquired"] == None or artwork2["DateAcquired"] == "":
        artwork2["DateAcquired"] = "0001-01-01"
    artwork1 = datetime.strptime(artwork1["DateAcquired"], "%Y-%m-%d")
    artwork2 = datetime.strptime(artwork2["DateAcquired"], "%Y-%m-%d")
    return artwork1 < artwork2


def cmpArtistDate(artist1, artist2):
    if artist1["BeginDate"] == None or artist1["BeginDate"] == "":
        artist1["BeginDate"] = "0"
    if artist2["BeginDate"] == None or artist2["BeginDate"] == "":
        artist2["BeginDate"] = "0"
    n = (int(artist1['BeginDate']) < int(artist2['BeginDate']))
    return n

def cmpNat(nat1,nat2):
    n = (int(nat1) > int(nat2))
    return n

def cmpmedio(medio1,medio2):
    if medio1 in medio2:
        return 0
    else:
        return 1


# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def sortartworks(catalog, sizesublist, typeofsort):
    sub_list = lt.subList(catalog['artworks'], 1, sizesublist)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if typeofsort == "insertion":
        sorted_list = ins.sort(sub_list, cmpArtworkByDateAcquired)
    elif typeofsort == "shell":
        sorted_list = ss.sort(sub_list, cmpArtworkByDateAcquired)       
    elif typeofsort == "merge":
        sorted_list = ms.sort(sub_list, cmpArtworkByDateAcquired)
    elif typeofsort == "quick":
        sorted_list = qs.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    tiempo = (stop_time - start_time)*1000
    elapsed_time_mseg = round(tiempo, 2)
    return elapsed_time_mseg 

def sortartistsDates(catalog, begin, end):
    art = catalog["artists"]
    sub_list = art.copy()
    sorted_list = ms.sort(sub_list,cmpArtistDate)
    listarespuesta = lt.newList(datastructure="ARRAY_LIST")
    for artista in lt.iterator(sorted_list):
        if int(artista["BeginDate"]) >= int(begin) and int(artista["BeginDate"]) < (int(end)+1):
            lt.addLast(listarespuesta, artista)
    totalartistas = lt.size(listarespuesta)
    sublista1 = lt.subList(listarespuesta,1,3)
    sublista2 = lt.subList(listarespuesta,(totalartistas-2),3)
    listarespuesta3y3 = lt.newList(datastructure="ARRAY_LIST")
    for artista in lt.iterator(sublista1):
        lt.addLast(listarespuesta3y3,artista)
    for artista in lt.iterator(sublista2):
        lt.addLast(listarespuesta3y3,artista)

    return totalartistas, listarespuesta3y3

def sortartworks2 (catalog,begin,end):
    sublist = catalog["artworks"]
    sublist = sublist.copy()
    sorted_list = ms.sort(sublist, cmpArtworkByDateAcquired)
    listarespuesta = lt.newList(datastructure="ARRAY_LIST")
    compradasporpurchase = 0
    for artwork in lt.iterator(sorted_list):
        if artwork["DateAcquired"] >= begin and artwork["DateAcquired"] <= end:
            lt.addLast(listarespuesta, artwork)
            acomparar = artwork["CreditLine"].lower()
            acomparar = acomparar.find("purchase")
            if acomparar != -1:
                compradasporpurchase += 1
    totalobras = lt.size(listarespuesta)
    sublista1 = lt.subList(listarespuesta,1,3)
    sublista2 = lt.subList(listarespuesta,(totalobras-2),3)
    listarespuesta3y3 = lt.newList(datastructure="ARRAY_LIST")
    for artwork in lt.iterator(sublista1):
        lt.addLast(listarespuesta3y3,artwork)
    for artwork in lt.iterator(sublista2):
        lt.addLast(listarespuesta3y3,artwork)
    return totalobras, compradasporpurchase, listarespuesta3y3

def Clasification(catalog, artist):
    art = catalog["artists"]
    medio_obras = lt.newList(datastructure="ARRAY_LIST")
    for a in lt.iterator(art):
        if a["DisplayName"] == artist:
            id = a["ConstituentID"]
    
    artworks = catalog["artworks"]
    
    for w in lt.iterator(artworks):       
        if w["ConstituentID"].strip("[]") == id:                    
            medium = w["Medium"]
            lt.addLast(medio_obras,medium)
       
    return (medio_obras,id) 
    
def info_medios(catalog, id, top):
    artworks = catalog["artworks"] 
    titulos = lt.newList(datastructure= "ARRAY_LIST")
    fechas = lt.newList(datastructure= "ARRAY_LIST")
    medio = lt.newList(datastructure= "ARRAY_LIST")
    dimensiones = lt.newList(datastructure= "ARRAY_LIST")
    for w in lt.iterator(artworks):       
        if w["ConstituentID"].strip("[]") == id:                    
            medium = w["Medium"]
            if medium == top:
                tit = w["Title"]
                lt.addLast(titulos,tit)
                fe = w["DateAcquired"]
                lt.addLast(fechas,fe)
                lt.addLast(medio,medium)
                di = w["Dimensions"]
                lt.addLast(dimensiones,di)
    return(titulos,fechas,medio,dimensiones)     

    
def topNat(tamaño_medios):
    num = lt.newList(datastructure= "ARRAY_LIST")
    cant = lt.size(tamaño_medios)
    i = 0
    while i in range(0,cant):
        nu = i%2
        if nu == 0:
            el = lt.getElement(tamaño_medios,i)
            lt.addLast(num,el)
        i+=1
    g = lt.size(num)
    print("Con un total de "+ str(g) +" tecnicas diferentes")
    sub = lt.subList(num,0,g)
    sub = sub.copy()
    orden = ms.sort(num,cmpNat)

    f = lt.size(orden)
    natorden = lt.newList(datastructure= "ARRAY_LIST")
    
    for w in orden["elements"]:  
        pos = lt.isPresent(tamaño_medios,w)             
        m = lt.getElement(tamaño_medios, pos-1)
        lt.addLast(natorden,m)
        n = lt.getElement(tamaño_medios, pos)
        lt.deleteElement(tamaño_medios, pos)
        delete = "0"
        lt.insertElement(tamaño_medios, delete, pos)
        lt.addLast(natorden,n)
    return natorden



        
       
       
    
        

