# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 06:35:08 2022

@author: USER
"""
#Librerias  -->>>
import pytesseract
from itertools import permutations   #69
import imageio          #71
from geopy.geocoders import Nominatim  #73
from moviepy.editor import VideoFileClip  #75     pip install moviepy
from captcha.image import ImageCaptcha    #76     pip install captcha
import emoji            #77        pip install emoji
from PIL import Image, ImageDraw, ImageFont     #78
import demoji                     #79     pip install demoji
import PyPDF2                     #80     pip install PyPDF2
import pyttsx3                   #       pip install pyttsx3
import pyshorteners              # 81    pip install pyshorteners
from zipfile import ZipFile      #82
from pdf2docx import Converter   #83
import time                      #84   
from plyer import notification   #         pip install plyer
import  webbrowser               #85
import urllib.request            #86      pip install urllib
from skimage import data, io, filters    #87
import whois                             #88
from calendar import *                   #89 
from PIL import Image                    #91
import barcode
from barcode.writer import ImageWriter    #93  pip install python-barcode

# <<<<<------
# '' % \ | ¿ ° & ? 
#65  -->>> Programa para encontrar el factorial de un número
def factorial():
    otro = 1
    while otro == 1:
        num = int(input("Ingrese un número : "))
        factorial = 1
        if num < 0:
            #
            print("Lo sentimos, el factorial no existe en nú<meros negativos.")
        elif num == 0:
            print("El factorial de 0 es 1")
        else:
            for i in range(1, num + 1):
                factorial = factorial * i
            print("El factorial de ", num, " es ", factorial)
        print("")
        otro = int(input(" 1) Desea intentar con otro número \n 0) Salir \n"))

#66 ---->>   Crando un triangulo con números
def trian_num():
    otro = 1
    while otro == 1:
        fila = int(input("Ingresa el número de filas del triangulo: "))
        num = 1
        for i in range(fila):
            for j in range(i + 1):
                print(num, end = " ")
                num = num + 1
            print()
        print(" ")
        otro = int(input(" 1) Desea intentar con otro número \n 0) Salir \n"))

#67 ---->>  Programa la suma de dos numeros
def suma():
    otro = 1
    while otro == 1:
        num1 = float(input("Ingrese el primer núemero: "))
        num2 = float(input("Ingrsesa el segundo número: "))
        sum = float(num1)+float(num2)
        print("La suma de {0} and {1} es {2}".format(num1, num2, sum))
        print("")
        otro = int(input(" 1) Desea intentar otra suma \n 0) Salir \n"))

#68 ---->>  programa para encontrar interes compuesto
def interes():
    otro = 1
    while otro == 1:
        P = float(input("Ingrese el valor principal : "))
        R = float(input("Ingrese el valor de la tarifa :"))
        T = float(input("Ingresa el valor de tiempo :"))
        def com_inter(principal, tarifa, tiempo):
            con = principal * (pow((1 + tarifa / 100), tiempo))
            CI = con - principal
            print("Interes compuesto = ", CI)
        com_inter(P, R, T)
        print("")
        otro = int(input(" 1) Desea intentar otra suma \n 0) Salir \n"))
            #

#69 ---->>  Permutaciones de cadenas
def permutar():
    otro = 1
    while otro == 1:
        def TodoPer(str):
            permList = permutations(str)
            def cuenta():
                cuenta.numero += 1
                return cuenta.numero
            cuenta.numero = 0
            for i in list(permList):
                print(cuenta(),".- ","".join(i))
        if __name__=="__main__":
            str = input("ingrese una palabra : ")
            TodoPer(str)
        print("")
        otro = int(input(" 1) Desea intentar otra suma \n 0) Salir \n"))
        
#70  ---->> Programa para intercambiar el primer y último elemento de una lista        
def intercambio():
    otro = 1
    while otro == 1:
        listN = []
        listN = [int(item) for item in input("Ingrese una lista de numeros : ").split()]
        def swList(listN):
            tamaño = len(listN)
            temp = listN[0]
            listN[0] = listN[tamaño - 1]
            listN[tamaño - 1] = temp
            return listN
        print(swList(listN))
        print("")
        otro = int(input(" 1) Desea intentar otra suma \n 0) Salir \n"))

#71  ---->>> Creacion de Gif
def git():
    #Las fos tipos de rutas funcionan
    #filename = [r"C:\Users\USER\Documents\ISC\ \Cursos\python_curse\cursos\python101\360_dias\sketch.png", r"C:\Users\USER\Documents\ISC\ \Cursos\python_curse\cursos\python101\360_dias\ono.jpg"]
    filename = ["sketch.png", "ono.jpg"]
    img = []
    for filename in filename:
        img.append(imageio.imread(filename))
    imageio.mimsave('movie2.gif', img, 'GIF', duration = 1)

#72   ---->>> Operciones entre bits
def opera():
    otro = 1
    while otro == 1:
        x = int(input("Ingrese el número uno : "))
        y = int(input("Ingrese el número uno : "))
        print(x | y)
        print(x ^ y)
        print(x & y)
        print(x << y)
        print(x >> y)
        print("")
        otro = int(input(" 1) Desea intentar otra suma \n 0) Salir \n"))

#73  --->>>  Obtener direccion atraves del codigo postal
def codigoP():
    otro = 1
    while otro == 1:
        geolocal = Nominatim(user_agent="geoapiExercises")
        codig_p = input("Ingrese un codigo postal: ")
        localidad = geolocal.geocode(codig_p)
        print("Codigo Postal : ", codig_p)
        print(localidad)
        print("")
        otro = int(input(" 1) Desea intentar otro codigo \n 0) Salir \n"))

#74  --->> Comprobar numeros Disarium
# Es un numero que elavado a la potencia asiganada (1,2,3,4) la suma es el mismo numero. 89, 175
def disarium():
    otro = 1
    while otro == 1:
        num = int(input("Ingrese un numero : "))
        def is_disarium(num):
            flag = (num == sum([int(str(num)[i-1])**i for i in range(1,len(str(num))+1)]))
            return flag
        print("\n El ",num," es un numero Disarium",is_disarium(num))
        print(" ")
        otro = int(input(" 1) Desea intentar con otro número \n 0) Salir \n"))

#75  --->> Convertir videos en Gif python
def video():
    videoClip = VideoFileClip("kaily.mp4")
    videoClip.write_gif("giff.gif")
        
#76  --->> Generar una imagen captcha en python
def captcha():
    image = ImageCaptcha(width = 300, height = 100)
    captcha_text = input("Ingrese las palabras para el captcha : ")
    data = image.generate(captcha_text)
    nom = input("Ingrese el nombre del captcha : ")
    nombre = nom + ".png"
    image.write(captcha_text, nombre)
    from PIL import Image
    Image.open(nombre)

#77  --->>> Imprimiendo emojis 
def emojis():
    #
    print(emoji.emojize(":books:"))
    print(emoji.emojize(":red_heart:"))
    print(emoji.emojize(":hibiscus:"))
    print(emoji.emojize(":rose:"))
    print(emoji.emojize(":baby:"))

#78 --->>> Marcado de agua en Imagenes con python
def marcado():
    img = Image.open(r"ono.jpg")
    draw = ImageDraw.Draw(img)
    text = "RyOoxNaY,kry"
    fond = ImageFont.truetype("arial.ttf", 50)
    textwidth, textheight = draw.textsize(text, fond)
    width, height = img.size
    x = width/2 - textwidth/2
    y = height - textheight - 50
    draw.text((x, y), text, fond = fond)
    img.save(r"marca.png")

#79  -->>> Combertir un emoji a texto
def emoji_text():
    otro = 1
    while otro == 1:
        emoji = input("Ingrese un emoji :")
        print(demoji.findall(emoji))
        print("")
        otro = int(input(" 1) Desea intentar con otro emoji \n 0) Salir \n"))

#80 ---->>> Convertir PDF en audiolibro
def audio():
    with open("goodman.pdf", "rb")as book:
        #
        full_text =""
        reader = PyPDF2.PdfFileReader(book)
        audiolibro = pyttsx3.init()
        audiolibro.setProperty("rate", 100)
        for pagina in range(reader.numPages):
            next_pg = reader.getPage(pagina)
            content = next_pg.extractText()
            full_text += content
        audiolibro.save_to_file(full_text, "myAudio.mp3")
        audiolibro.runAndWait()


def voz():
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    text = "Hola mundo. soy Ryooxnay"
    engine.say(text)
    another_text = "Me gusta python"
    engine.say(another_text)
    engine.runAndWait()


#81  --->> Un acortador de URL 
def url():
    link = input("Ingrese un URL para acortar: ")
    tipe_tiny = pyshorteners.Shortener()
    short_url = tipe_tiny.tinyurl.short(link)
    print("La URL corta es :" + short_url)

#82  --->> Descomprimiendo archivos Zip
def zipp():
    with ZipFile("360.zip", "r") as zip_object:
        zip_object.extractall()
    print(zip_object.namelist())

#83  --->> Convertidor PDF a documento doct
def pdf_docx():
    pdf_file = "goodman.pdf"
    docx_file = "Nuevo_Doc.docx"
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()
#84  ------->>>>>>>>>        ************************************************
#------->>>>>>>>>        ************************************************
#------->>>>>>>>>        ************************************************
#------->>>>>>>>>        ************************************************
#------->>>>>>>>>        ************************************************

#85  --->>  Notificaciones de escritorio en python
def noti():
    if __name__ == "__main__":
        while True:
            notification.notify(
                title="ALERT",
                message = "Tome un descanso, por una hora.",
                timeout = 10
            )
            time.sleep(5)
#86  --->>> Buscador en la web con python
def buscador():
    #
    Url = input("Ingresa la Url: ")
    webbrowser.open(Url)
    webbrowser.open_new(Url)
    webbrowser.open_new_tab(Url)

#87  --->>> Descargar un PDF 
def descargaPDF():
    url = input("Ingrese el link de un PDF : ")
    name = input("Ingrese el nombre para guardar el pdf : ")
    fieleName = name+".pdf"
    urllib.request.urlretrieve(url, fieleName)
    
#88  --->> programa para encontrar los bordes de una moneda
def bordeMoneda():
    image = data.coins()
    bordes = filters.sobel(image)
    io.imshow(bordes)
    
#89 --->>> Obtanaer informacion del nombre de dominio 
def dominio():
    dominio = input("Ingrese un dominio : ")
    dominio_info = whois.whois(dominio)
    for key, value in dominio_info.items():
        print(key, ";", value)

#90 ---->> Imprimir el calendario de este año
def calendario():
    anio = int(input("Ingrese con numero el año que quiere ver : "))
    print(calendar(anio, 2, 1, 8, 4))

#91 ---->>> Crar una imagen espejo en pyhton
def espejo():
    #Image.open("ono.jpg")
    img = Image.open("ono.jpg")
    Mirro_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    #Mirro_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    Mirro_img.save(r"ono_espejo.png")
    Image.open("ono_espejo.png")
#92 --->>> Tomar detalles de una Imagen
def detalleImage():
    img = Image.open("ono.jpg")
    print(img.format, ", ", img.mode, ", ", img.size, ", ", img.palette)

#93  -->>> Generar codigo de barras usando Python
def Codigo_Barras():
    num = input("Ingresa el número a convertir en codigo de barras : ")
    #obtener el formato de código de barras requerido
    forma_barra = barcode.get_barcode_class("upc")
    #generar código de barras y renderizar como imagen
    myCodigo = forma_barra(num, writer = ImageWriter())
    #Guardar el codigo
    myCodigo.save("nuevoCodigo")
    Image.open("nuevoCodigo.png")
#94   --->>> Extraer texto de una Imagen 
def imagText():
    #westeyex
    direc_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
    direct_img = "imgText.jpg"
    pytesseract.tesseract_cmd = direc_tesseract
    img = Image.open(direct_img)
    text = pytesseract.image_to_string(img)
    print(text)
imagText()