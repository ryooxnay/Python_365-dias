import pywhatkit as kit
import cv2
import plotly.graph_objects as go
import turtle as t
import random
from langdetect import detect
from countryinfo import CountryInfo
#'' % \
# 1
def contadorCaracter():
    palabra = input("Ingrese una palabra: ")
    #https://www.youtube.com/watch?v=0sRAzXRON8Y video autoestima
    count = {}
    for i in palabra:
        if i in count:
            count[i] += 1
            print("")
        else:
            count[i] = 1
    print(count)
    print(palabra)
#2
def multiploComun():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    if a > b:
        mayor = a
    elif b > a:
        mayor = b
    while(True):
        if((mayor %a == 0 )and (mayor %b == 0)):
            mul = mayor
            break
        mayor = mayor+1
    print(mul)
#3
def numRomano(): #Ajustar, tiene detalles
    simbolo={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    roman = input("Ingrese el Número Romano: ")
    sum = 0
    for i in range(len(roman)-1):
        izq = roman[i]
        der = roman[i + 1]
        if simbolo[izq] < simbolo[der]:
            sum -= simbolo[izq]
        else:
            sum += simbolo[izq]
    sum += simbolo[roman[-1]]
    print(sum)
#4
#### usando pywhatkit
def abrirYoutube():
    try:
        kit.playonyt("https://www.youtube.com/watch?v=pgN-vvVVxMA")
        print("Playing...")
    except:
        print("Network Error Occured")
    finally:
        print("###")
#5
def buscarGoogle():

    try:
        kit.search("Yony David Leal ")
        print("Buscando...")
    except:
        print("A ocurrido un error")
    finally:
        print("###")
#6
def msjWhats():
    try:
        kit.sendwhatmsg("+52 2321122964", "Hola amor te mande mensaje por un programa que acabo de hacer en mi compu, esto es Genial", 24,40)
        print("Mesnaje enviando...")
    except:
        print("Se a presentado un error")
    finally:
        print("##")
#7
#####################
def textHandW():
    letra= input("Ingresa una frase a convertir : ")
    kit.text_to_handwriting(letra, save_to="letras.png")        
    img = cv2.imread("letras.png")
    cv2.imshow("Python Coding", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#8
def mapaArbol():
    fig = go.Figure(go.Treemap(
        labels = ["A","B","C","D","E", "F", "G", "H", "I"],
        parents = ["", "A", "A", "C", "C", "A", "A", "G", "A"]
    ))
    fig.show()
#9
def fahreCelsius():
    print("Convertidor de Grados Celsius a Fahrenheit y viseversa") 
    def menu():
        print("1.- Grados Celsius a Fahrenheit.")
        print("2.- Grados Fahrenheit a Celsius.")
        print("0.- Salir")
    menu()
    opci = int(input())
    while(opci != 0):
        
        if opci == 1:
            gradosC = float(input("Ingrese los grados Celsius : "))
            gradosCF = float((gradosC*1.8)+32)
            print(gradosC,"CELSIUS = ", gradosCF, "FAHRENHEIT")
            print(" ")
            menu()
            opci = int(input())
        elif opci == 2:
            gradosF = float(input("Ingrese los grados Fahreneit : ")) 
            gradosFC = float((gradosF-32)/1.8)
            print(gradosF,"FAHRENHEIT = ", gradosFC, "CELSIUS")
            print(" ")
            menu()
            opci = int(input())
        else:
            break
    print("A-D-I-O-S")
#10  
def CalculadorIMC():
    print("Bienvenido al calculador de IMC para adultos:")
    def Otro():
        print("1.- Deceas hacer otra consulta. ")
        print("0.- Salir.")
    opcion = 1
    while(opcion != 0):
        masa = float(input("Ingrese su peso en Kilogramos : "))
        altu = float(input("Ingresa su estatura en Centimetros : "))
        imc = masa/(pow((altu/100),2))
        print("Tu masa corporal es de : ",imc)
        if imc < 18.6:
            print("          Tienes Bajo Peso...")
            Otro()
            opcion = int(input())
        elif imc > 18.6 and imc < 25:
            print("          Tu estado es Normal...")
            Otro()
            opcion = int(input())
        elif imc > 24.5 and imc < 30:
            print("          Tienes Sobrepeso...")
            Otro()
            opcion = int(input())
        elif imc > 29.9:
            print("          Tienes Obecidad...")
            Otro()
            opcion = int(input())
        else:
            break
    print("-A-D-I-O-S-")
#11
def figuras():
    #t.Turtle()
    try:
        
        s = t.Screen()
        s.bgcolor("Black")
        t.width(2)
        t.speed(15)
        col = ('white','pink', 'cyan')
        for i in range(100):
            t.pencolor(col[i%3])
            t.forward(i*4)
            t.right(121)
        
        t.hideturtle()
        t.destroyAllWindows()
    except(Exception):
        print(Exception)
#12 
def GeneradorPWS():
    print("")
    otro = 1
    while otro != 0:
        carac = int(input("Cuantos caracteries requiere en la contraseña : "))
        ca = "123456789qwertyuiopñlkjhgfdsazxcvbnm!#$*/-_.,=@QWERTYUIOPÑLKJHGFDSAZXCVBNM()"
        pwd = "".join(random.sample(ca,carac))
        print(pwd)
        otro = int(input("1.- Desea generar otra contraseña. \n 0.- Salir. \n"))
    print("-A-D-I-O-S-")
#13
def lenguajeDetec():
    otro = 1
    while otro != 0:
        texto = input("Ingrese el texto para detectar el idioma : ")
        idioma = {'af':'Africaans','ar':'Arabica',
                  'an':'aragones','hy':'Armenio','as':'Assamese','av':'Avarico','ae':'Avestico','ay':'Aymara','az':'Azerbaiyano',
                  'bm':'Bambar','ba':'Bashkir','eu':'Vasco','be':'Bielorruso','bn':'Bengali','bi':'Bislama','bs':'Bosnio','br':'Breton',
                  'bg':'Bulgaro','my':'Birmano','ca':'Catalan','ch':'Chamorro','ce':'Checheno','ny':'Chichewa','zh':'Chino','cu':'Eslavo','cv':'Chuvasio',
                  'kw':'Cornualles','co':'Corso','cr':'Cree','hr':'roata','cs':'Checo','da':'Danes','dv':'Divehi','nl':'Holandés','dz':'Dzongkha','en':'Ingles','es':'Español',
                  'eo':'Esperanto','et':'Estonio','ee':'Ewe','fo':'Foroés','fj':'Fiyiano','fi':'Filandés','fr':'Francés','fy':'Frisón Occidental','ff':'Fula','gd':'Gaélico','fa':'Persa',
                  'gu':'GU','he':'hebreo','hi':'Hindi','hr':'HR','hu':'Hungaro','id':'Indonesia','it':'','ja':'Japones','kn':'Canada','ko':'Koreano','lt':'Lituano','lv':'Leton',
                  'mk':'Macedonio','ml':'Malayalam','mr':'Marathi','ne':'Nepalí','nl':'','no':'Noruego','pa':'Punjabi','pl':'Polaco','pt':'Portugues','ro':'Rumano','ru':'Ruso','sk':'Eslovaco',
                  'sl':'Esloveno','so':'Somali','sq':'SQ','sv':'Sueco','sw':'Swahii','ta':'Tamil','te':'Telugo','th':'Tailandes','tl':'Talago','tr':'Turco','uk':'Ucranio','ur':'Urdu',
                  'vi':'Vietnamita','zh-cn':'ZH-CN','xh-tw':'XH-TW',}
        idio = detect(texto)
        
        print(idioma[idio])
        otro=int(input("1.- Desea inngresar otro texto. \n 0.- Salir. \n"))
#14
def infoEsta():
    otro = 1
    idioma = {'af':'Africaans','ar':'Arabica',
              'an':'aragones','hy':'Armenio','as':'Assamese','av':'Avarico','ae':'Avestico','ay':'Aymara','az':'Azerbaiyano',
              'bm':'Bambar','ba':'Bashkir','eu':'Vasco','be':'Bielorruso','bn':'Bengali','bi':'Bislama','bs':'Bosnio','br':'Breton',
              'bg':'Bulgaro','my':'Birmano','ca':'Catalan','ch':'Chamorro','ce':'Checheno','ny':'Chichewa','zh':'Chino','cu':'Eslavo','cv':'Chuvasio',
              'kw':'Cornualles','co':'Corso','cr':'Cree','hr':'roata','cs':'Checo','da':'Danes','dv':'Divehi','nl':'Holandés','dz':'Dzongkha','en':'Ingles','es':'Español',
              'eo':'Esperanto','et':'Estonio','ee':'Ewe','fo':'Foroés','fj':'Fiyiano','fi':'Filandés','fr':'Francés','fy':'Frisón Occidental','ff':'Fula','gd':'Gaélico','fa':'Persa',
              'gu':'GU','he':'hebreo','hi':'Hindi','hr':'HR','hu':'Hungaro','id':'Indonesia','it':'','ja':'Japones','kn':'Canada','ko':'Koreano','lt':'Lituano','lv':'Leton',
              'mk':'Macedonio','ml':'Malayalam','mr':'Marathi','ne':'Nepalí','nl':'','no':'Noruego','pa':'Punjabi','pl':'Polaco','pt':'Portugues','ro':'Rumano','ru':'Ruso','sk':'Eslovaco',
              'sl':'Esloveno','so':'Somali','sq':'SQ','sv':'Sueco','sw':'Swahii','ta':'Tamil','te':'Telugo','th':'Tailandes','tl':'Talago','tr':'Turco','uk':'Ucranio','ur':'Urdu',
              'vi':'Vietnamita','zh-cn':'ZH-CN','xh-tw':'XH-TW',}
    while otro != 0:
        estado = input("Ingrese un Pais : ")
        country = CountryInfo(estado)
        print("Su capital es: ", country.capital())
        idio = country.languages()
        #print("Su lengua es : ",idioma[idio])
        print("Su lengua es : ",idio)
        print("Otros nombres : ", country.alt_spellings())
        otro = int(input("1.- Desea inngresar otro texto. \n 0.- Salir. \n"))
infoEsta()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
