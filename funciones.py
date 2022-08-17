from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pathlib import *
from easygui import *
from selenium import webdriver
from random import randint
from time import sleep
import csv
import inspect
import os
import re

# Lee los nombres de los pdfs a buscar y los guarda en una lista. Están almacenados en un txt, separados por /n
# Recibe: -
# Devuelve: listaDePdfs
def leerArchivo():
    informacion = open("listaDePdfs.txt", "r", encoding="latin1")

    listaDePdfs = []
    for fila in informacion:
       listaDePdfs.append((fila).strip())
    
    print (listaDePdfs)

    return [listaDePdfs]

'''def formatearListaPdfs(pdfsAbuscar):
    msgbox("Formateando la lista")
    #nuevaLista = [x[:-1] for x in pdfsAbuscar]
    #nuevaLista = [x[1] for x in pdfsAbuscar]
    nuevaLista = []
    for pdf in pdfsAbuscar:
        pdf.strip("/n")
    return nuevaLista
'''


