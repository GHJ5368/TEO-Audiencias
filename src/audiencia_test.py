from audiencia import *

def test_lee_audiencia(fichero):
    print("Leyendo el archivo csv..")
    audiencias= lee_audiencias(fichero)
    #print(audiencias[:3])
    return audiencias

def test_calcula_ediciones(audiencias, nombre_programa):
    ediciones = calcula_ediciones(audiencias)
    print(f"Número de ediciones del programa {nombre_programa}: {ediciones}")

def test_filtra_por_ediciones(audiencias, ediciones, nombre_programa):
    filtradas = filtra_por_edicion(audiencias, ediciones)
    print(f"Los datos de las ediciones {ediciones} del programa {nombre_programa} son:\n {filtradas}")

def test_agrupa_por_ediciones(audiencias, nombre_programa):
    dicc = agrupa_por_ediciones(audiencias)
    print(f"Agrupación por ediciones del programa {nombre_programa}: \n{dicc}")

def test_medias_por_ediciones(audiencias, nombre_programa):
    dicc = medias_por_ediciones(audiencias)
    print(f"La media por ediciones del programa {nombre_programa} es: \n{dicc}")




if __name__ == "__main__":
    audiencias_gh = test_lee_audiencia('TEO-Audiencias\data\GH.csv')
    audiencias_masterchef = test_lee_audiencia('TEO-Audiencias\data\MasterChef.csv')
    #test_calcula_ediciones(audiencias_gh, "Gran Hermano")
    #test_calcula_ediciones(audiencias_masterchef, "Master Chef")
    #test_filtra_por_ediciones(audiencias_gh, [1,2,3], "Gran Hermano")
    #test_filtra_por_ediciones(audiencias_masterchef, [4,5], "Master Chef")
    test_agrupa_por_ediciones(audiencias_gh, "Gran Hermano")
    test_agrupa_por_ediciones(audiencias_masterchef, "Master Chef")
    test_medias_por_ediciones(audiencias_gh, "Gran Hermano")
    test_medias_por_ediciones(audiencias_masterchef, "Master Chef")

