# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 02:28:24 2022

@author: USER
"""
import random as ra
import PyPDF2 as pf
import matplotlib.pyplot as pyplot
import getpass                #29


import plotly.express as px   #30
import pandas as pd           #30
from plotly.offline import plot
import plotly.graph_objs as go

import pyfiglet     #35  pip install pyfiglet
from better_profanity import profanity     #36 pip install better_profanity
#'' % \
from difflib import SequenceMatcher #37
import urllib.request #38
import pyqrcode #39    pip install pyqrcode
import png      #39    pip install pypng
from pyzbar.pyzbar import decode
from PIL import Image

from time import time  #40
from tkinter import *
import cv2
import pywhatkit as kit # 42    pip install pywhath
import sounddevice                   #43 pip insatll sounddevice
from scipy.io.wavfile import write   #43 pip insatll scipy
import pytube

#24
def palabras():
    def palabra(pala1,pala2):
        pala1 = pala1.lower()
        pala2 = pala2.lower()
        return sorted(pala1) == sorted(pala2)  # Sorted es para ordenar listas
    print(palabra("cinema", "iceman"))
    print(palabra("cool", "loco"))

#25 
def textPdf():
    pdf = open("compu.pdf","rb") 
    leer = pf.PdfFileReader(pdf)
    pag = leer.getPage(0)
    print(pag.extractText())
#26
def partes_pay():
    etiqueta = ('Python','Java','Scala','C#')
    tamaño = [45,30,15,10]
    pyplot.pie(tamaño, labels=etiqueta,autopct='%1.f%%',counterclock=False,startangle=105)
    pyplot.show()
#27 
def GraficoBarras():
    etiqueta = ('Python','Java','Scala','C#','PHP')
    index = (1,2,3,4,5)
    tamaño=[45,10,15,30,22]
    #Configuracion de la grafica 
    pyplot.bar(index, tamaño, tick_label = etiqueta)
    #Configuracion del diseño
    pyplot.ylabel('Usage')
    pyplot.xlabel('Programming lengues')
    pyplot.show()
#28
def ip_direccion():
    ip = input("Ingrese si ip: ")
    espacio_id = ip.split(".")
    separador = "[.]"
    new_ip = separador.join(espacio_id)
    print(new_ip)

#29
def passswordA():
    database = {"yonydavid":"123456789", "123yonydavid":"12345"}
    usuario = input("Ingrese su nombre: ")
    pwd = getpass.getpass("Password : ")
    for i in database.keys():
        if usuario == i:
            while pwd != database.get(i):
                pwd = getpass.getpass("Enter tu pwd : ")
            break
    print("Verificacion")

#30
 
def radar():
    data = pd.DataFrame(dict(keys=[10,20,30,40], values=["diez", "veinte","treinta","cuarenta"]))
    figure=px.line_polar(data, r='keys', theta='values', line_close=True)
    figure.update_traces(fill="toself")    
    print(figure)
    figure.show()


def plotly_ejem():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    print(plot(fig, auto_open=True))
    fig.show()
    
#33
def pascalTriang():
    arr = [1]
    temp = []
    n = int(input("Ingrese el numero de filas en el tringulo de pascal: "))
    for i in range(n):
        print("fila", i+1, end = " : ")
        for j in range(len(arr)):
            print(arr[j], end =" ")
        print()
        temp.append(1)
        for j in range(len(arr)-1):
            temp.append(arr[j] + arr[j+1])
        temp.append(1)
        arr = temp
        temp = []

#34 
def rombo():
    filas = int(input("Ingrese el tamaño de Diagonal Mayor : "))
    sim = input("Ingresa el simbolo deseado : ")
    fl = round((filas /2))
    for i in range(1, fl + 1):
        for j in range(1, fl - i + 1):
            print(end = ' ')
        for k in range(0, 2*i - 1):
            print(sim, end = "")
        print()
    for i in range(1, fl):
        for j in range(1, i + 1):
            print(end = ' ')
        for k in range(1, 2*(fl-i)):
            print(sim, end = "")
        print()

#35
def letras():
    letra = pyfiglet.figlet_format("Python Code")
    print(letra)

#36
def removePalabra(): #Blasfemias
    text = input("Ingrese una oracion : ")
    un = profanity.censor(text)
    print(un)
#37
def comparador():
    txt = input("Primera oracion : ")
    txt2 = input("Segunda oracion : ")
    sqs = SequenceMatcher(None, txt, txt2).ratio()
    print(f"Se aproxima que es un  {sqs * 100} % Similar ")

#38
def tablasWeb():
    url = "https://en.wikipedia.org/wiki/List_of_publicly_listed_ITES_companies_of_India"
    url2 = "https://www.tudn.com/mx/futbol/liga-mx/posiciones"
    with urllib.request.urlopen(url2) as i:
        html = i.read()
    data = pd.read_html(html)[0]
    print(data.head())
#39
def QrCode():
    def Code():
        link = input("Ingrese un link para convertir en QR : ")
        qrCode = pyqrcode.create(link)
        nom = input("Ingrese el nombre : ")
        qrCode.png(nom + ".png", scale=5)
    def desCode():
        nom = input("ingrese el nombre de la imagen : ")
        dec = decode(Image.open(nom))
        print(dec[0].data.decode("ascii"))
    def menu():
        print("**********  Bienvenido *********")
        print("1.- Crear Codigo")
        print("2.- Descodificar")
        print("0.- Salir")
    otro = 1
    
    while otro == 1:
        menu()
        opc = int(input(""))
        if opc == 1 :
            Code()
        if opc == 2:
            desCode()
        else:
            break
        otro = input("1.- Volver al menu. \n0.- Salir \n : ")
      
#40
def TimeEjecucion():
    star = time()
    email = input("Ingrese su correo: ")
    email = email.strip()
    slicer_index = email.index("@")
    nomUsuario = email[:slicer_index]
    domain_name = email[slicer_index+1:]
    print("Tu nombre de usuario es, " + nomUsuario +
          " y tu dominio es, "+ domain_name)
    end = time()
    execion_time = end - star
    print("Se ejecuto en : ", execion_time , "(s)")
        
def ventana_40():
    star = time()
    ven = Tk()
    ven.geometry("500x500")
    ven.title("Email")
    Lb1 = Label(ven, text = "Ingresa tu correo", font = "Helvetica 15 bold").pack()
    email = Entry(ven, font = "Helvetica 15 bold").pack()
    email = str(email)
    
    
    def cal():
        
        #email = email.strip()
        slicer_index = email.index("@")
        nomUsuario = email[:slicer_index]
        domain_name = email[slicer_index+1:]
        res = "Tu nombre de usuario es ", nomUsuario, " Y tu dominio es ",
        domain_name
        print(res)
        lb2 = Label(ven, text=res).pack()
    btn = Button(ven, text="Aceptar", command=cal).pack()
    
    ven.mainloop()

#41
def imagenPencil():
    try:
        #
        #Muestra la ventana e imagen
        img1 = cv2.imread("ono.jpg")
        windows_name = "Imagen Original"
        cv2.imshow(windows_name, img1)
    
        grey_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        invert = 255-grey_img
    
        #Suavisar imagen
        blur = cv2.GaussianBlur(invert, (21,21),0)
        inverteBlur = 255-blur
        sketch = cv2.divide(grey_img, inverteBlur, scale=256.0)
    
        cv2.imwrite(r"C:/Users/USER/Desktop/sketch.png", sketch)
    
        image = cv2.imread(r"C:/Users/USER/Desktop/sketch.png")
        windows_name = "sketch"
        cv2.imshow(windows_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except (ValueError):
        print(ValueError)

#42
def Email_Dominio():
    star = time()
    email = input("Ingrese su correo: ")
    email = email.strip()
    slicer_index = email.index("@")
    nomUsuario = email[:slicer_index]
    domain_name = email[slicer_index+1:]
    print("Tu nombre de usuario es, " + nomUsuario +
          " y tu dominio es, "+ domain_name)

#43
def busqueda():
    busqueda = (input("Ingrese el tema: "))
    kit.info(busqueda,100)
    


#44  Grador de vos desde python
def voces():
    fs = 44100
    segundos = int(input("Introduzca el tiempo de grabación en segundos : "))
    print("Recording ...")
    gravacion_voz = sounddevice.rec(int(segundos*fs), samplerate=fs, channels = 2)
    sounddevice.wait()
    write("MyGravacion.wav", fs, gravacion_voz)
    print("la grabación se ha realizado verifique su carpeta para ver la lista de grabación")


#45 Descargar videos de Youtube
def descargasYouTube():
    url = input("Ingrese el url del video : ")
    ubicacion = r"C:/Users/USER/Downloads"
    pytube.YouTube(url).streams.get_highest_resolution().download(ubicacion)

descargasYouTube()














