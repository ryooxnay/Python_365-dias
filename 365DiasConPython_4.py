# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 00:25:39 2022
@author: USER
"""
#Librerias  -->>>
from geopy.geocoders import Nominatim #46 pip install geopy
import sys, time             #50 
import os                    #53
import hashlib               #54
import pyautogui as captt    #56
import random                #57
import math
import matplotlib.pyplot as plt    #58
from PyPDF2 import PdfFileWriter, PdfFileReader #59   pip install PyPDF2
import getpass
import time              #64 
# <<<<<------
#'' % \

#46  -->> Obtener el código postal con la ubicación dada usando GeoPy en Python
def GeoPostal():
    geolocalizador = Nominatim(user_agent="geoapiExercises")
    lugar = input("Ingrese el nombre de la ciudad : ")
    locacion = geolocalizador.geocode(lugar)
    print(locacion)

#47  -->> Ordenación por selección en python
def selec():
    List = []
    n = int(input("Ingrese cuantos datos tiene su lista : "))
    for i in range(n):
        L = int(input("Ingresa un número : "))
        List.append(L)
    def sel(List):
        for i in range(len(List)-1):
            mini = i
            for j in range(i+1,len(List)):
                if(List[j]<List[mini]):
                    mini = j
            if(mini != i):
                List[i], List[mini] = List[mini], List[i]
        return List
    if __name__ == "__main__":
        #List = [3,4,2,6,5,7,1,9,8]
        print("Lista Ordenada: ", sel(List))

#48   --->> ordenamiento de burbuja en python
def burbuja():
    List = []
    n = int(input("Ingresa cuantos datos tiene tu lista : "))
    for i in range(n):
        L = int(input("Ingresa un número : "))
        List.append(L)
    
    def burbu(List):
        for i in range(len(List)):
            for j in range(len(List)-1, i, -1):
                if List[j] < List[j - 1]:
                    List[j], List[j - 1]= List[j - 1], List[j]
        return List
    if __name__ == "__main__":
        #
        print("Lista Ordenada: ", burbu(List))   

#49  -->>>  Ordenar por inserción usando Python
def Ord_Insercion():
    List = []
    n = int(input("Ingresa cuantos datos tiene tu lista : "))
    for i in range(n):
        L = int(input("Ingrese un número: "))
        List.append(L)
    def insercion(List):
        for i in range(1, len(List)):
            currentN = List[i]
            for j in range(i -1, -1, -1):
                if List[j] > currentN:
                    List[j], List[j + 1] = List[j + 1 ], List[j]
                else:
                    List[j + 1] = currentN
                    break
        return List
    if __name__ == "__main__":
        print("Orden Por Insección : ", insercion(List) )
    
#50   --->>> Barra de progreso en python
def Bar_Prg():
    def progreso(count, total, suffix = ""):
        Tamaño_bar = 60
        bar_llena = int(round(Tamaño_bar * count / float(total)))
        per = round(100.0 * count / float(total),1)
        bar = "=" * bar_llena + "-" * (Tamaño_bar - bar_llena)
        sys.stdout.write("[%s] %s%s ... %s\r" % (bar, per, "%", suffix)) 
        sys.stdout.flush()
    for i in range(11):
        time.sleep(1)
        progreso(i, 10)

#51  --->>> verificaccion de un número perfecto
def Num_Perfec():
    otro = 1  
    def PerN():
        n = int(input("Ingrese un número : "))
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        print(sum == n, "\n")
    while otro == 1:
        print("1.- Comprobar un número. ")
        print("0.- Salir.")
        opc = int(input(""))
        if opc == 1:
            PerN()
            opc = 1
        else:
            break
    
#52  --->>> Numeros primos menor 
def num_primos():
    otro = 1
    def primos():
        n = int(input("Ingrese un número : "))
        prim = [True] * (n+1)
        p = 2
        while((p*p) <= n):
            if(prim[p])==True:
                for i in range(p*2, n+1, p):
                    prim[i]= False
            p += 1
        for i in range(2, n ):
            if prim[i]:
                print(i)
    if __name__ == "__main__":
        primos()
    while otro == 1:
        #print()
        print("\n","1.- Comprobar otro número. ")
        print(" 0.- Salir.")
        opc = int(input(""))
        if opc == 1:
            primos()
            opc = 1
        else:
            break

#53  -->>> Contar los directorios y numero de archivos.
def Direc_File():
    try:
        #path = input("Ingrese el directorio a analizar.")
        path = r"C:\Users\USER\Documents"
    except:
        print("Ingrese una direccion valida:")
    archivoC = 0
    directorioC = 0
    for root, dirs, file in os.walk(path):
        #print("Looking in : ", root)
        for directories in dirs:
            directorioC += 1
        for Files in file:
            archivoC += 1
    print("Numero de archivos", archivoC)
    print("Numero de carpetas", directorioC)
    print("Total : ", int(archivoC) + int(directorioC))
    
#54  --->> Calcular un hash de un archivo
#--->>> Cifrado de algoritmos con hashlib (md5 y sha)
def calcu():
    BLOCKSIZE = 65536
    AbriArchivo = r"C:\Users\USER\Documents\txt_doc.txt"
    hasher = hashlib.md5()
    with open(AbriArchivo, "rb") as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    print(hasher.hexdigest())
           
#55 -->>> Assignar un valor clave en python
def diccio():
    d = {'a':1, 'b':2, 'c':3 }
    c = int(input("ingrese el nuevo valor para la letra C = "))
    d['c'] = c
    dd =int(input("Ingrese el nuevo valor para D = "))  
    d['d'] = dd
    print(d)

#56   ---->>>> Captura de pantalla en python
def captura():
    cap = captt.screenshot()
    nom = input("ingrese el nombre de la captura : ")
    dire = nom + ".png"
    cap.save(r"C:/Users/USER/Documents/"+dire)
    
#57   --->>> Juego de adivinar el numero
def adivinar():
    bajo = int(input("Ingresa el mas bajo : "))
    alto = int(input("Ingresa el mas alto : "))
    num = random.randint(bajo, alto)
    print("\n\t Solo tienes ",round(math.log(alto-bajo+1,2))," oportunidades \n\t Estas Listo...")
    contador = 0
    while contador < math.log(alto - bajo + 1, 2):
        contador += 1 
        adiv = int(input("Adivina un número : "))
        if num == adiv:
            print("Felicidades adivinastes el número con ", contador, " intentos" )
            break
        elif num < adiv:
            print("El número es muy grande.")
        elif num > adiv:
            print("El número es muy pequeño.")
    if contador >= math.log(alto - bajo + 1,2):
        print("\n El número es ", num)
        print("\n Suerte a la proxima XD.. ")
    
#58   -->>> Graficas usando Matplotilib
def graficas():
    montando = ((17,18,21,22,19,21,25,22,24),(3,6,3.5,4,5,6.3,4.5,5,4.5))
    natacion =((17,18,20,19,22,21,23,19,21,24),(8,9,7,10,7.5,9,8,7,8.5,9))
    navegacion = ((31,28,29,36,27,32,34,35,33,39),(4,6.3,6,3,5,7.5,2,5,7,4))
    plt.scatter(x = montando[0], y = montando[1], c = 'red',  label='Montando')
    plt.scatter(x = natacion[0], y = natacion[1], c = "green", label="Natación")
    plt.scatter(x = navegacion[0], y = navegacion[1], c = "blue", label="Navegación")
    plt.xlabel("Edad")
    plt.ylabel("Horas")
    plt.title("Actividades en Grafica")
    plt.legend()
    plt.show()
    
#59 -->> Proteger un pdf con contraseña
def pwd_pdf():
    pdfEscritura = PdfFileWriter()
    pdf = PdfFileReader(r"C:\Users\USER\Documents\SS.pdf")
    for page_num in range(pdf.numPages):
        pdfEscritura.addPage(pdf.getPage(page_num))
    pwd = getpass.getpass(prompt = "Ingrese una Contraseña: ")
    pdfEscritura.encrypt(pwd)
    with open(r"C:\Users\USER\Documents\SS.pdf",'wb' ) as f:
        pdfEscritura.write(f)
    print("Nuevo archivo protegido con contraseña....")

#60   --->>> Programa para checar si es u numero Armstrong
def Armstrong():
    sum = 0
    num = int(input("Ingrese el número para comparar: "))
    numS = num
    while numS > 0:
        digit = numS % 10
        sum += digit ** 3
        numS //= 10
    if num == sum:
        print(num, " Si es un número Armstrong")
    else:
        print(num, " No es un número Armstrong")
        
#61   ---->>> Serie de fibonacci 
def fibonacci():
    n1, n2 = 0,1
    cont = 0
    num =int(input("Cuantos números desea encontrar : "))
    if num <= 0:
        print("Ingresa un numero positivo.")
    elif num == 1:
        print("Secuencia de 1 : ")
        print(n1)
    else:
        print("Secuencia de fibonacci: ")
        while cont < num:
            print(n1)
            ntt = n1 + n2
            n1 = n2
            n2 = ntt
            cont += 1

#62 --->>>         
def factor():
    num = int(input("Ingrese el numero para encontrar el factor : "))
    def factorX(x):
        print("EL factor de ",x," es: ")
        for i in range(1, x + 1):
            if x % i == 0:
                print(i)
    factorX(num)

#63 --->>> Remover Signos de puntuaciones en String
def RemoPun():
    puntuacion = '''!()-_[]{};:,.<>=/+*@#$~^''' 
    Sttring = input("Ingresa una Oracion : ")
    noPuntuacion = ""
    for char in Sttring:
        if char not in puntuacion:
            noPuntuacion = noPuntuacion + char
    print(noPuntuacion)
    
#64  -->>>> Contador regresivo programable
def contador():
    def conttt(time_sec):
        while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end = '/r')
            time.sleep(1)
            time_sec -= 1
        print("Stop ")
    num =int(input("Ingresa el tiempo : "))
    conttt(num)
    
    
contador()