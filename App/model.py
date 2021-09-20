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
    artists = artwork["ConstituentID"].strip("[]")
    artists = artwork["ConstituentID"].split(",")
    for artist in artists:
        addArtistArtWork(catalog,artist,artwork)
  

def addArtistArtWork(catalog,artistname,artwork):
    artists = catalog["artists"]
    posartist = lt.isPresent(artists,artistname)
    if posartist >0:
        artist = lt.getElement(artists, posartist)
    else:
        artist = newArtist (artistname)
        lt.addLast(artists, artist)
    lt.addLast(artist["artworks"], artwork)

def newArtist(name):
    artist = {"ConstituentID":"" , "artworks": None , "DisplayName":"" , "Nationality":"" , "Gender": "" , "BeginDate":None , "EndDate":None}
    artist["ConstituentID"] = name
    artist["artworks"] = lt.newList("ARRAY_LIST")
    return artist

def addArtists(catalog,artist):
    ConstituentID = artist["ConstituentID"]
    posartista = lt.isPresent(catalog["artists"], ConstituentID)
    if posartista > 0:
        nombre = lt.getElement(catalog["artists"],posartista)
        nombre["DisplayName"] = artist["DisplayName"]
        nombre["Nationality"] = artist["Nationality"]
        nombre["Gender"] = artist["Gender"]
        nombre["BeginDate"] = artist["BeginDate"]
        nombre["EndDate"] = artist["EndDate"]
    else:
        nombre = newArtist (ConstituentID)
        nombre["DisplayName"] = artist["DisplayName"]
        nombre["Nationality"] = artist["Nationality"]
        nombre["Gender"] = artist["Gender"]
        nombre["BeginDate"] = artist["BeginDate"]
        nombre["EndDate"] = artist["EndDate"]
        lt.addLast(catalog["artists"], nombre)


    
    


def compareartists(artistname1, artist):
    if (artistname1.lower() in artist['ConstituentID'].lower()):
        return 0
    return -1

def cmpArtworkByDateAcquired(artwork1, artwork2):
    if artwork1["DateAcquired"] == None or artwork1["DateAcquired"] == "":
        artwork1["DateAcquired"] = "0001-01-01"
    if artwork2["DateAcquired"] == None or artwork2["DateAcquired"] == "":
        artwork2["DateAcquired"] = "0001-01-01"

    return datetime.strptime(artwork1["DateAcquired"], "%Y-%m-%d") < datetime.strptime(artwork2["DateAcquired"], "%Y-%m-%d")


def cmpArtistDate(artist1, artist2):
    if artist1["BeginDate"] == None or artist1["BeginDate"] == "":
        artist1["BeginDate"] = "0"
    if artist2["BeginDate"] == None or artist2["BeginDate"] == "":
        artist2["BeginDate"] = "0"
    n = (float(artist1['BeginDate']) < float(artist2['BeginDate']))
    return n


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
    s = lt.size(art) 
       
    sub_list = lt.subList(art,1,s)
    sub_list = sub_list.copy()
    sorted_list = ms.sort(sub_list,cmpArtistDate) 
    elm = sorted_list["elements"]
   # print(sorted_list)
    
    pos1 = lt.newList("ARRAY_LIST")
    pos2 = lt.newList("ARRAY_LIST")
    for i in elm:        
        a = i["BeginDate"]   
            
        ai = int(a)
        lt.addLast(pos1,a)
        if ai >= begin:
            posartista1 = lt.isPresent(pos1, a)                   
            for j in elm:                
                b = j["BeginDate"]  
               # print(b)              
                if b == None:
                    bi = 0
                else:
                    bi = int(b) 
                lt.addLast(pos2,b)             
                if bi == end + 1:
                    lt.removeLast(pos2)
                    last = lt.size(pos2)
                    first = lt.size(pos1)
                    #print(pos2)
                    t = last - first                            
                    lo = lt.subList(sorted_list, posartista1, t)
                    print(last, first)
                    break
            break            
        elif ai >= end:
            break
        else:
            None
    return t
               


        
       
       
    
        

