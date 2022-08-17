import sys
from funciones import *
from easygui import *

def main():

    pdfsLista = leerArchivo()
    #pdfsListaFormateada = formatearListaPdfs(pdfsLista)
    #print(pdfsListaFormateada)
    msgbox("Presione una tecla para terminar")
    
if __name__ == "__main__":
    sys.exit(main())