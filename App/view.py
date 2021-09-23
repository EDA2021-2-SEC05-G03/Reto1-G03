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
catalog = None

#Imprimir el Menú
def printMenu():
    print ("Bienvenido")
    print ("1. Cargar archivos.")
    print ("2. Ordenar por orden de adquisición de las obras")
    print ("3. REQ. 1: Listar cronológicamente los artistas")
    print ("4. REQ. 2: Listar cronológicamente las adquisiciones.")
    print ("5. REQ. 3: Clasificar las obras de un artista por técnica")
    print ("6. REQ. 4: Clasificar las obras por la nacionalidad de sus creadores.")
    print ("7. REQ. 5: Costo de transportar las obras de un departamento a otro")
    print ("0. Salir")

#Iniciador de catalogos y carga de datos
def initCatalog(tipolista: str):
    return controller.initCatalog(tipolista)
def loadData(catalog):
    controller.loadData(catalog)


#Funciones de imprimir: listas y cmpfunction de estas
def printsortartist(lista):
    print(" ")
    print("-" * 100)
    for artists in lt.iterator(lista):
        print("Nombre: " + artists["DisplayName"])
        print("Fecha de Nacimiento: " + artists["BeginDate"])
        print("Fecha de fallecimiento: " + artists["EndDate"])
        print("Nacionalidad: " + artists["Nationality"])
        print("Género: " + artists["Gender"])
        print("-" * 100)
def printsortartworks(lista, listaartistas):
    print("-" * 188)
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
                print ("- "+nombre)
            print ("-"*188)
        else: 
            posartista = lt.isPresent(listaartistas,artworks["ConstituentID"])
            posartista = posartista - 1
            nombre = lt.getElement(listaartistas, posartista)
            nombre = nombre["DisplayName"]
            print ("- "+nombre)
            print ("-"*188)
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
def printtransport(info,departamento):
    #tamañodepartamento, costototal, mascaros, masviejos
    print ("=" * 150)
    print ("El total de obras para la categoría " + departamento + " es de: " + str(info[0]) )
    print ("El costo total de transportar este departamento es de " + str(round(info[1],2)) + " USD apróximadamente.")
    print ("=" * 150)
    print ("El TOP 5 de obras mas caras son: ")
    print ("=" * 150)
    for obra in lt.iterator(info[2]):
        print("Object ID: " + obra["ObjectID"] )
        print("Título: "+ obra["Title"])
        ###
        print("Clasificación: " + obra["Department"])
        print("Fecha de la obra: " + obra["Date"])
        print("Medio: " + obra["Classification"])
        print("Dimensiones: " + obra["Dimensions"])
        print ("Costo de transporte: " + str(obra["Costo"]) + " USD")
        print ("URL: " + obra["URL"])
        print ("-" * 150)
    print ("="*150)
    print ("El TOP 5 obras mas viejas de la categoría a transportar:")
    print ("="*150)
    for obra in lt.iterator(info[3]):
        print("Object ID: " + obra["ObjectID"] )
        print("Título: "+ obra["Title"])
        ###
        print("Clasificación: " + obra["Department"])
        print("Fecha de la obra: " + obra["Date"])
        print("Medio: " + obra["Classification"])
        print("Dimensiones: " + obra["Dimensions"])
        print ("Costo de transporte: " + str(obra["Costo"]) + " USD")
        print ("URL: " + obra["URL"])
        print ("-" * 150)
#Menú Principal
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
            print(" ")
            print ("Numero de obras: " + str(info[0]))
            print ("Adquiridas por purchase: " + str(info[1]))
            listaartistas = lt.newList(datastructure= "ARRAY_LIST", cmpfunction= cmpfunctionlistaartistas)
            x = agregarlistaartistas(listaartistas, info[2])
            printsortartworks(info[2],x)
    elif int(inputs[0]) == 5:  
        artista = (input("Ingrese el nombre del artista de las obras a clasificar: "))    
        info = controller.artworksClasification(catalog, artista)
        lista = info[0]
        tamaño_total_obras = lt.size(lista)
        tamaño_medios = lt.newList(datastructure= "ARRAY_LIST")
        print("El artista " +artista+" tiene un total de "+ str(tamaño_total_obras)+" de obras en el museo.")  
        for medio in lt.iterator(lista):
            posicion = lt.isPresent(tamaño_medios,medio)
            if posicion == 0:
                
                lt.addLast(tamaño_medios, medio)
                lt.addLast(tamaño_medios, str(1))
            else:
                x = lt.getElement(tamaño_medios, (posicion + 1))
                x = int(x) + 1
                x = str(x)
                lt.deleteElement(tamaño_medios, posicion+1)
                lt.insertElement(tamaño_medios, x, posicion+1)
        # TOP 5
        top = controller.topMed(tamaño_medios)
        print("+"+("-"*51)+"+")  
        print("|"+"TOP 5 TÉCNICAS".center(51)+"|")  
        print("+"+("-"*51)+"+") 
        x = 0
        while x < 10:
            print ("|"+top["elements"][x].center(40)+"|"+top["elements"][x+1].center(10)+"|")
            print("+"+("-"*51)+"+") 
            x+=2
        #Obras Medio TOP
        main = top["elements"][0]
        info_medio = controller.info_medios(catalog,info[1],main)
        print(" ")
        l = len(info_medio)
        f=0
        print("+"+("-"*217)+"+")
        print("|"+"Titulo".center(105)+" | "+"Fecha".center(13)+" | "+"Medio".center(15)+" | "+"Dimensiones".center(74)+" | ")
        print("+"+("-"*217)+"+")
        while f < l-1:
            print("|"+info_medio[0]["elements"][f].center(105)+" | "+info_medio[1]["elements"][f].center(13)+" | "+info_medio[2]["elements"][f].center(15)+" | "+info_medio[3]["elements"][f].center(74)+" | ")
            print("+"+("-"*217)+"+")
            f+=1
    elif int(inputs[0]) == 6:  
        nacionalidades = controller.artworksNat(catalog)
        tamaños = controller.countNat(nacionalidades)
        top = controller.topNat(tamaños)
    elif int(inputs[0]) == 7:
        departamento = input("Ingrese el departamento a evaluar su costo de transporte: ")
        info = controller.costotransporte(catalog,departamento)
        printtransport(info,departamento)
    else:
        sys.exit(0)
sys.exit(0)