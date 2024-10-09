from audiencia import *

def test_lee_audiencia(fichero):
    print("Leyendo el archivo csv..")
    audiencias= lee_audiencias(fichero)
    print(audiencias[:3])


if __name__ == "__main__":
    test_lee_audiencia('TEO-Audiencias\data\GH.csv')

