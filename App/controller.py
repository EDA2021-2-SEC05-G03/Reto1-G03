import config as cf
import model
import csv

# Inicialización del Catálogo de libros
def initCatalog(tipolista : str):
    catalog = model.newCatalog(tipolista)
    return catalog
    
# Funciones para la carga de datos
def loadData(catalog):
    loadArtwork(catalog)
    loadArtists(catalog)
def loadArtwork(catalog):
    awfile = cf.data_dir + "Artworks-utf8-small.csv"
    input_file = csv.DictReader(open(awfile, encoding ="utf-8"))
    for aw in input_file:
        model.addArtwork(catalog, aw)
def loadArtists(catalog):
    artistfile = cf.data_dir + "Artists-utf8-small.csv"
    input_file = csv.DictReader(open(artistfile, encoding ="utf-8"))
    for artist in input_file:
        model.addArtists(catalog, artist)

#Funciones de requerimientos y ordenamientos
def sortartworks(catalog,sizesublist,typeofsort):
    return model.sortartworks(catalog,sizesublist,typeofsort)
def sortartworks2(catalog,begin,end):
    return model.sortartworks2(catalog,begin,end)
def sortartistsDates(catalog,begin,end):
    return model.sortartistsDates(catalog,begin,end)
def artworksClasification(catalog, artista):
    return model.Clasification(catalog,artista)
def topMed(num):
    return model.topMed(num)
def info_medios(catalog,id,top):
    return model.info_medios(catalog,id,top)
def costotransporte(catalog,departamento):
    return model.costotransporte(catalog,departamento)
def artworksNat(catalog):
    return model.artworksNat(catalog)
def countNat(catalog):
    return model.countNat(catalog)
def topNat(num):
    return model.topNat(num)