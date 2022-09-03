# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 00:13:11 2022

@author: USER
"""
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
import numpy as np
import datetime
import random
from textblob import TextBlob   # pip install -U textblob
#'' % \

#12
def conjunto():
    U = {1,2,3,4,5,6,7,8,9,10}
    A = {}
    B = {2,4,5,6}
    C = {1,2,3}
    def text():
        print(" U = {1,2,3,4,5,6,7,8,9,10} \n A = {" "} \n B = {2,4,5,6} \n C = {1,2,3}")
        print("1.- Pertenencia")
        print("2.- Subconjunto")
        print("3.- Unión")
        print("4.- Intersección")
        print("5.- Diferencia")
        print("6.- Complemento")
        print("0.- Salir")
    text()
    opc = int(input(" "))
    while opc == 1:
        otro = 1
        while otro != 0:
            num = int(input("Ingrese un valor del 1 al 10 :  "))
            if num in U != True:
                print(num, " Pertenese al conjunto U")
                if num in A != True:
                    print(num, " Pertenece al conjunto A")
                if num in B != True:
                    print(num, "Pertenece a conjunto B")
                if num in C != True:
                    print(num, " Pertenece al conjunto C")        
            else:
                print(num, " No es un numero valido ")
            otro = int(input("\n 1.- Ingresar otro valor \n 0.- Salir al meni principal \n  :: "))    
        text()
        opc = int(input(" "))
    while opc != 0:
        exit(0)

#13
def mas18():
    otro = "y" 
    while otro == "y":
        edad = int(input("Ingrese su edad : "))
        nombre = input("Ingrese su nombre : ")
        if edad > 17:
            print("Bienvenido ", nombre)
        elif edad < 18:
            print("Lo siento ", nombre, " no puede pasar.")
        
        otro = input("Desea intentar otro registro (y/n) : ")
    while otro != "n":
        exit(0)
#14
def onda():
    data= sns.load_dataset("tips")
    plt.figure(figsize=(10,4))
    sns.violinplot(x=data["total_bill"])
    plt.show()

#15
def edad():
    a = int(input("Ingese el su año de nacimiento: "))
    m = int(input("Ingese el su mes de nacimiento: "))
    d = int(input("Ingese el su dia de nacimiento: "))
    hoy = datetime.datetime.now().date()
    fecha = datetime.date(a,m,d)
    edad = int((hoy-fecha).days/365.25)
    print(edad)

###################################
    #Tres dimenciones con PLOTS

#16
def diemen3():
    def f(x,y):
        return np.sin(np.sqrt(x**2 + y**2))
    x = np.linspace(-6,6,30)
    y = np.linspace(-6,6,30)
    x,y = np.meshgrid(x,y)
    z = f(x,y)
    #fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(x,y,z,80, cmap='binary')
    #ax.size(432,288)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    #print(ax)
    plt.show()

#17
def ejemploGrafica_3D():
    # Creamos la figura
    fig = plt.figure()

    # Agrrgamos un plano 3D
    ax1 = fig.add_subplot(111,projection='3d')
    # Datos en array bi-dimensional
    x = np.array([[1,2,3,4,5,6,7,8,9,10]])
    y = np.array([[5,6,7,8,2,5,6,3,7,2]])
    z = np.array([[1,2,6,3,2,7,3,3,7,2]])

    # plot_wireframe nos permite agregar los datos x, y, z. Por ello 3D
    # Es necesario que los datos esten contenidos en un array bi-dimensional
    ax1.plot_wireframe(x, y, z)
    print(ax1)
    # Mostramos el gráfico
    plt.show()
    
#18
def barras_3D():
    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt
    import numpy as np
 
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')

    # Definimos los datos
    x3 = [1,2,3,4,5,6,7,8,9,10]
    y3 = [5,6,7,8,2,5,6,3,7,2]
    z3 = np.zeros(10)
    
    dx = np.ones(10)
    dy = np.ones(10)
    dz = [1,2,3,4,5,6,7,8,9,10]
    
    # utilizamos el método bar3d para graficar las barras
    ax1.bar3d(x3, y3, z3, dx, dy, dz)

    # Mostramos el gráfico
    plt.show()

#19
def scatter_3D():
    # Scatter

    # importamos las librerias necesarias
    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt

    # Creamos la figura
    fig = plt.figure()
    # Creamos el plano 3D
    ax1 = fig.add_subplot(111, projection='3d')

    # Definimos los datos de prueba
    x = [1,2,3,4,5,6,7,8,9,10]
    y = [5,6,7,8,2,5,6,3,7,2]
    z = [1,2,6,3,2,7,3,3,7,2]

    # Datos adicionales
    x2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
    y2 = [-5,-6,-7,-8,-2,-5,-6,-3,-7,-2]
    z2 = [1,2,6,3,2,7,3,3,7,2]

    # Agregamos los puntos en el plano 3D
    ax1.scatter(x, y, z, c='g', marker='o')
    ax1.scatter(x2, y2, z2, c ='r', marker='o')

    # Mostramos el gráfico
    plt.show()

#20
def correction():
    def Convert(string):
        li = list(string.split())
        return li
    str1 = input("Ingrese una palabra : ")
    palabra = Convert(str1)
    correc_pala = []
    for i in palabra:
        correc_pala.append(TextBlob(i))
    print("Palabra equivocada : ", palabra)
    print("La palabra correcta es :")
    for i in correc_pala:
        print(i.correct(), end="")
        
#21
def Spiner():
    state = {'turn':0}
    print()
#22
def azar():
    carta = ["Diamante", "Espadas","Corazones", "Bastos"]
    rank = [2,3,4,5,6,7,8,9,10, "Jack", "Queen", "King", "Ace"]
    
    cart =random.choices(carta)
    ran = random.choices(rank)
    print("The", ran, " of ", cart)
    
azar()    
    









































        
    
    
        