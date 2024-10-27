import csv   # Para leer los csv de datos
from matplotlib import pyplot as plt   # Para mostrar gráficas, importamos matplotlib.pyplot, renombrándolo como plt
from collections import namedtuple     # Para definir tuplas con nombre

Audiencias = namedtuple("Audiencia",["edicion","share"])

def lee_audiencias(fichero):
    audiencias=[]
    with open(fichero,"r",encoding="utf-8") as f:
        lector = csv.reader(f)
        for edicion, visualizacion in lector:
            edicion=int(edicion)
            visualizacion=float(visualizacion)
            audiencia=Audiencias(edicion, visualizacion)
            audiencias.append(audiencia)
    return audiencias

def calcula_ediciones(audiencias):
    ediciones = set()

    for a in audiencias:
        ediciones.add(a.edicion)

    return len(ediciones)

def filtra_por_edicion(audiencias,ediciones):
    filtrado = []
    
    for a in audiencias:
        if a.audiencias in ediciones:
            filtrado.append(a)
    
    return filtrado

def agrupa_por_ediciones(audiencias):
    res = dict()
    
    for a in audiencias:
        if a.edicion in res: #Seria como comprobar si está en res.keys()
            res[a.edicion].append(a.share)
        else:
            res[a.edicion] = []
    
    return res

def medias_por_ediciones(audiencias):
    grupo_ediciones = agrupa_por_ediciones(audiencias)
    res = dict()

    for edicion, shares in grupo_ediciones:
        media_share = sum(shares)/len(shares)
        res[edicion] = media_share

    return res

