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
