import random
import operator

def menu(usuario, puntos, vida):
    print(" ")
    print("Sesión de ",usuario)
    print("Total de puntos: ", puntos)
    print ("Vidas restantes: ",vida)
    print(" ")
    print("1-Comezar a jugar.")
    print("2-Ver tabla de posiciones.")
    print(" ")

def menu1():
    print(" ")
    print("1) Piedra, Papel, Tijera. (1 punto) ")
    print("2) 1 Dado: Adivina el número. (5 puntos) ")
    print("3) 2 Dados: Adivina el número. (10 puntos) ")
    print(" ")

def agregarUsuario(usuario, lista):
    lista.append(usuario)


def ppt ():
    puntos = 0
    while True:
        aleatorio = random.randrange(0,3)
        opcMaquina = ""
        print(" ")
        print("Juega contra la maquina. Piedra le gana a tijeras, papel le gana a piedra, y tijera le gana a papel")
        print(" ")
        print(" ")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        print(" ")
        opc = int(input("Elige opcion (1,2,3)"))
        print(" ")

        if opc == 1:
            opcUsuario = "Piedra"
        elif opc == 2:
            opcUsuario = "Papel"
        elif opc == 3:
            opcUsuario = "Tijera"

        if aleatorio == 0:
            opcMaquina = "Piedra"
        elif aleatorio == 1:
            opcMaquina = "Papel"
        elif aleatorio == 2:
            opcMaquina = "Tijera"
        print ("La maquina eligió: ", opcMaquina)    

        if opcMaquina == "Piedra" and opcUsuario == "Papel":
            print("Ganaste, papel envuelve piedra")
            puntos = 1
            print("Sumaste un punto!")
            break
        elif opcMaquina == "Papel" and   opcUsuario == "Tijera":
            print ("Ganaste, tijera corta papel")
            puntos = 1
            print("Sumaste un punto!")
            break
        elif opcMaquina == "Tijera" and opcUsuario == "Piedra":
            print("Ganaste, piedra rompe tijera")
            puntos = 1
            print("Sumaste un punto!")
            break
        if opcUsuario == "Piedra" and opcMaquina == "Papel":
            print("Perdiste, papel envuelve piedra")
            print("Pierde una vida")
            puntos = -1
            break
        elif opcUsuario == "Papel" and   opcMaquina == "Tijera":
            print ("Perdiste, tijera corta papel")
            print("Pierde una vida")
            puntos = -1
            break
        elif opcUsuario == "Tijera" and opcMaquina == "Piedra":
            print("Perdiste, piedra rompe tijera")
            print("Pierde una vida")
            puntos = -1
            break
        elif opcMaquina == opcUsuario:
            print ("Empate")
    print(" ")        
    return puntos

def dadoAdivina():
    print(" ")
    print("Tira el dado y suma puntos adivinando el numero que saldra")
    print(" ")
    while True:
        numUsuario = int(input("Elije un numero entre 1 el 6 y tira el dado: "))
        if (numUsuario < 1 or numUsuario > 6):
            print ("Numero invalido")   
        else:
            break
    dado = random.randrange(1,6)
    if numUsuario==dado:
        print("El dado muestra ", dado)
        print("Adivinaste! Suma 3 puntos")
        puntos = 3
    else:
        print("El dado muestra ", dado)
        print("No adivinaste, pierde una vida")
        puntos = -1
    print(" ")    
    return puntos

def dosDadosAdivina():
    print(" ")
    print("Tira los dados y suma puntos adivinando los numeros que saldran")
    print(" ")
    while True:
        numUsuario = int(input("Elije un numero entre 2 el 12 y tira los dados: "))
        if (numUsuario < 2 or numUsuario > 12):
            print ("Numero invalido")   
        else:
            break
        
    dado1 = random.randrange(1,6)
    dado2 = random.randrange(1,6)

    if numUsuario==dado1+dado2:
        print("Los dados muestran ", dado1,"y ", dado2)
        print("Adivinaste! Suma 10 puntos")
        puntos = 10
    else:
        print("Los dados muestran ", dado1,"y ", dado2)
        print("No adivinaste, pierde una vida")
        puntos = -1
    print(" ")
    return puntos

    

    

def comprobarDisponible(usuario, usuarios):
    disponible = True
    i=0
    for u in usuarios:
        if usuario.strip().lower() == usuarios[i].strip().lower():
            disponible = False
        i = i + 1        
    return disponible


usuarios = []
dic1 = {}
vida = 3
while True:
    print(" ")
    print ("JUEGO DE SUERTE")
    print ("REGLAS")
    print(" ")
    print ("El usuario comienza con 3 vidas y tiene 3 modos de juegos disponibles")
    print ("Si gana un juego, puede seguir jugando y acumulando puntos")
    print ("Si pierde un juego, pierde una vida")
    print ("El objetivo es juntar la mayor cantidad de puntos antes de quedarse sin vidas")
    print(" ")
    
    usuario = input("Ingrese su nombre de usuario: ")

    while True:
        if comprobarDisponible(usuario, usuarios) == False:
            print ("Usuario ya existente")
            usuario = input("Ingrese su nombre de usuario: ")
        else: 
            break

    puntos = 0

    agregarUsuario(usuario, usuarios)
    SesionUsuario = True

    while SesionUsuario == True:
        menu(usuario, puntos, vida)
        dic1 [usuario] = puntos
        seguirMostrando = True
        while seguirMostrando == True:
            opc = input()
            if opc == "1" or opc == "2":
                seguirMostrando = False
            else:
                print("Opción no valida, intente de nuevo")

        if(opc == "1"):
            menu1()            
            num = int(input())
            match num:
                case 1:
                    res = ppt()
                    if res == -1:
                        vida = vida - 1
                    else: puntos = puntos + res

                case 2:
                    res = dadoAdivina()
                    if res == -1:
                        vida = vida - 1
                    else: puntos = puntos + res
                
                case 3:
                    res =  dosDadosAdivina()
                    if res == -1:
                        vida = vida - 1
                    else: puntos = puntos + res

        elif (opc == "2"):
            if (len(dic1) < 2):
                print(" ")
                print("No se registraron puntajes aun")
            else:
                dic1_sort = sorted(dic1.items(), key=operator.itemgetter(1), reverse=True)
                for item, valor in dic1_sort:
                    print(" ")
                    print(item, valor)
                    print(" ")

        
        if (vida == 0):
            vida = 3
            SesionUsuario = False










