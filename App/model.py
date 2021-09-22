import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf
from datetime import datetime
import time

# Construccion de modelos
def newCatalog(tipolista: str):
    catalog = {'artists': None,
               'artworks': None,
               }
    catalog["artists"] = lt.newList(tipolista,cmpfunction= compareartists)
    catalog["artworks"] = lt.newList(tipolista)
    return catalog

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):  
    lt.addLast(catalog["artworks"], artwork)
def addArtists(catalog,artist):
    lt.addLast(catalog["artists"], artist)

# Funciones utilizadas para comparar elementos dentro de una lista
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
def cmpfunctionmascaros(element1, element2):
    return element1["Costo"] > element2["Costo"]
def cmpfunctionantiguedad(element1,element2):
    if element1["Date"] == "" or element1["Date"] == None:
        element1["Date"]= "9999"
    if element2["Date"] == "" or element2["Date"] == None:
        element2["Date"] = "9999" 
    return element1["Date"] < element2["Date"]
def cmpMed(med1,med2):
    n = med1 < med2
    return n
def cmpNat(nat1,nat2):
    n = int(nat1) > int(nat2)
    return n

#Funciones de los requerimientos
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
def costotransporte(catalog,departamentoentrada): 
    
    departamentolista = lt.newList(datastructure="ARRAY_LIST")
    artworks= catalog["artworks"]
    for obra in lt.iterator(artworks):
        if obra["Department"] == departamentoentrada:
            if obra["Circumference (cm)"] == None or obra["Circumference (cm)"] == "":
                obra["Circumference (cm)"] = 0
            if obra["Depth (cm)"] == None or obra["Depth (cm)"] == "":
                obra["Depth (cm)"] = 0
            if obra["Diameter (cm)"] == None or obra["Diameter (cm)"] == "":
                obra["Diameter (cm)"] = 0
            if obra["Height (cm)"] == None or obra["Height (cm)"] == "":
                obra["Height (cm)"] = 0
            if obra["Length (cm)"] == None or obra["Length (cm)"] == "":
                obra["Length (cm)"] = 0
            if obra["Weight (kg)"] == None or obra["Weight (kg)"] == "":
                obra["Weight (kg)"] = 0
            if obra["Width (cm)"] == None or obra["Width (cm)"] == "":
                obra["Width (cm)"] = 0
            lt.addLast(departamentolista,obra)
    tamañodepartamento = lt.size(departamentolista)
    #Lista del departamento creada arriba
    costototal = float(0)
    for obra in lt.iterator(departamentolista):
        costokilo = float(0)
        costoarea = float(0)
        costovolumen = float(0)
        costodefecto = 48.00
        costomayor = float(0)
        costomultiplicar = 72.00

        # Costo por kilo.
        if obra["Weight (kg)"] != 0:
            costokilo = costomultiplicar * float(obra["Weight (kg)"])

        #Circulo o esféra
        if obra["Diameter (cm)"] != 0:
            print ("AAAAAAAAAAAAAAAAAAAAAA")
            #área
            if obra["Height (cm)"] == 0: 
                radio = ((float(obra["Diameter (cm)"]) * (1/100))/2)
                aream = (radio*radio)*3.1416
                costoarea = costomultiplicar * aream
            #volumen
            else: 
                radio = ((float(obra["Diameter (cm)"]) * (1/100))/2)
                volumen = (radio*radio)*float(obra["Height (cm)"])*3.1416
                costovolumen = volumen * costomultiplicar
        
        #Cuadro o bloque
        if obra["Height (cm)"] != 0  or obra["Length (cm)"] != 0:
            #Con length
            if obra["Length (cm)"] != 0:
                largo = float(obra["Length (cm)"]) * (1/100)
                if obra["Width (cm)"] != 0 :
                    ancho = float(obra["Width (cm)"]) * (1/100)
                    area= largo*ancho
                    if obra["Depth (cm)"] != 0:
                        profundidad = float(obra["Depth (cm)"]) * (1/100)
                        volumen = area*profundidad
                        costovolumen = volumen * costomultiplicar
                    if costovolumen == 0:
                        costoarea = area*costomultiplicar
            #Con height
            if obra["Height (cm)"] != 0:
                largo = float(obra["Height (cm)"]) * (1/100)
                if obra["Width (cm)"] != 0 :
                    ancho = float(obra["Width (cm)"]) * (1/100)
                    area= largo*ancho
                    if obra["Depth (cm)"] != 0:
                        profundidad = float(obra["Depth (cm)"]) * (1/100)
                        volumen = area*profundidad
                        costovolumen = volumen * costomultiplicar
                    if costovolumen == 0:
                        costoarea = area*costomultiplicar
        costomayor = max(costovolumen,costoarea,costokilo)
        #Costo mayor cuando no hay datos suficientes.
        if costoarea == 0 and costovolumen == 0 and costokilo ==0:
            costomayor = costodefecto
        obra["Costo"] = costomayor

        costototal += costomayor
    mascaros = ms.sort(departamentolista, cmpfunctionmascaros)
    mascaros = lt.subList(mascaros,1,5)
    masviejos = ms.sort(departamentolista, cmpfunctionantiguedad)
    masviejos = lt.subList(masviejos,1,5)

    for l in lt.iterator(mascaros):
        print(l["Costo"])
    
    for l in lt.iterator(masviejos):
        print(l["Date"])
    
    return tamañodepartamento, costototal, mascaros, masviejos
def artworksNat(catalog):
    artwork = catalog["artworks"]
    ids = lt.newList(datastructure="ARRAY_LIST")
    for elm in lt.iterator(artwork):
        id = elm["ConstituentID"].strip("[]")
        id = id.split(",")       
        for i in id:
            lt.addLast(ids, i)
 
    siz = lt.size(ids)
    sub = lt.subList(ids,0,siz)
    sub = sub.copy()
    
    nationalitys = lt.newList(datastructure="ARRAY_LIST")
    artists = catalog["artists"]
    
    for a in sub["elements"]:      
        for n in artists["elements"]:         
            id = n["ConstituentID"].strip()  
           # print(id)
            nat = n["Nationality"]
            a = a.strip()
            if a == id:      
                lt.addLast(nationalitys, nat)
    
    sorted = ms.sort(nationalitys,cmpMed)  

    return sorted
def countNat(lista):
    tamaño_n = lt.newList(datastructure= "ARRAY_LIST")

    for pais in lt.iterator(lista):
        posicion = lt.isPresent(tamaño_n,pais)
        if posicion == 0:               
            lt.addLast(tamaño_n, pais)
            lt.addLast(tamaño_n, str(1))
        else:
            x = lt.getElement(tamaño_n, (posicion + 1))
            x = int(x) + 1
            x = str(x)
            lt.deleteElement(tamaño_n, posicion+1)
            lt.insertElement(tamaño_n, x, posicion+1)
    return tamaño_n
def topNat(lst):
    
    num = lt.newList(datastructure = "ARRAY_LIST")
    cant = lt.size(lst)
    i = 0
    while i in range(0,cant):
        nu = i%2
        if nu == 0:
            el = lt.getElement(lst,i)
            lt.addLast(num,el)
        i+=1
    orden = ms.sort(num,cmpNat)
    
    natorden = lt.newList(datastructure = "ARRAY_LIST")
    
    for w in orden["elements"]:  
        pos = lt.isPresent(lst,w)             
        m = lt.getElement(lst, pos-1)     
        lt.addLast(natorden,m)
        n = lt.getElement(lst, pos)
        lt.deleteElement(lst, pos)
        delete = "0"
        lt.insertElement(lst, delete, pos)
        lt.addLast(natorden,n)
  
    for u in natorden["elements"]:
        if u == "":
            pos1 = lt.isPresent(natorden,u)
            pos = int(pos1)+1
            pos2 = lt.isPresent(natorden,"Nationality unknown")
            num = int(pos2)+1
            unk2= lt.getElement(natorden, num)    
            unk1 =  natorden["elements"][pos1]       
            new = int(unk2) + int(unk1)
            lt.changeInfo(natorden, pos, new)
            lt.changeInfo(natorden, pos1, "Nationality unknown")
            lt.deleteElement(natorden, pos2)
            lt.deleteElement(natorden, pos2)
    print(natorden)     