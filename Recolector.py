# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 01:59:13 2021

@author: JOSE
"""
import os
import re
import ssl
import sys
import time
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import git
import traceback

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

estudiantes = pd.read_excel("Estudiantes.xlsx")
print(estudiantes.head())

estudiantes.dropna(subset=['Usuario de GitHub'], inplace=True)
print(estudiantes.head())


chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
  })

URL = zip(estudiantes['Usuario de GitHub'], estudiantes['Número X asignado'])

estudiantes_correctos = list()
estudiantes_incorrectos = list()

for estudiante in URL:
    nombre = str(estudiante[0]) 
    numero = str(estudiante[1]) 
    try:
        webpage = r'https://github.com/' + nombre + '/MIIA_estudiante_' + numero
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print(webpage)
        driver.get(webpage)
        validar = int(numero)
        if validar <= 3:
            entrada = input("Está todo bien??")
            if entrada == "1":
                print("Continue")
            else: break
        try:
            error = driver.find_element_by_xpath('/html/body/div[4]/main/div[1]/div[2]/img[2]')
        except:
            estudiantes_correctos.append(webpage + '.git')  
    except:
        traceback.print_exc()
        print("No se recuperó el link del estudiante " + nombre)
        continue
    try:
        screenname = driver.find_element_by_xpath("//a[@title='Talleres']")
        screenname = driver.find_element_by_xpath("//a[@title='Laboratorios']")
    except:
        print("El estudiante " + nombre + " no creó bien el repo.")
        estudiantes_incorrectos.append(nombre)
        continue
    driver.close()

for malo in estudiantes_incorrectos:
    print(malo)        
deseo = input('Marque 1 si quiere clonar los repos y 2 si quiere actualizarlos:  ') 
direccion = input('Ingrese la ruta en donde quiere guardar los repos:  ')   

def clonacion(estudiantes: list):
    for est in estudiantes:
        print(est)
        nombredeest = str(est)
        git.Repo.clone_from(est,direccion + '/' + str(re.search('estudiante_(.*).git', nombredeest).group(1)))
    return None


def pulling(estudiantes: list):
    rango = range(45)
    for num in rango:
        cc = direccion
        cc += "/MIIA_estudiante_" + str(num)
        repo = git.Repo(cc)
        o = repo.remotes.origin
        o.pull()
    return None
 
if deseo == "1":
    clonacion(estudiantes_correctos)
if deseo == "2":
    pulling(estudiantes_correctos)

