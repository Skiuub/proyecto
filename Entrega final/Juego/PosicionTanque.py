import random
from .Variables import *
from .Tanques import *
from .Esquinas import *
from .Terreno import Terreno

def posicion_aparicion(cantidad):
    
    distribuir = cantidad-20
    Contador = 0

    while Contador < 6:
        posiciones_X[Contador] = random.randint(((distribuir-cantidad)+40),distribuir)
        #print(cantidad)
        #print(distribuir)
        Contador += 1
        distribuir = distribuir+(cantidad+20)

#Función para la destruccion del terreno
def posicion(jugador):
    #Se valida la posicion del tanque Azul luego de la destruccion del terreno
    if jugador.get_Y()+1 < ancho[0]:
        if mapa[(jugador.get_Y())+1][jugador.get_X()] == 0 or mapa[(jugador.get_Y())+2][jugador.get_X()] == 0:

            estado = 0
            Aux = 1
            jugador.set_Y(jugador.get_Y()-30)
            contx = jugador.get_X()
            conty = jugador.get_Y()

            while jugador.get_Y() < conty+15:
                Define_color = contx
                while jugador.get_X() < contx+15:
                    while (Define_color+Aux) > contx:
                        mapa[jugador.get_Y()][Define_color+Aux] = estado
                        mapa[jugador.get_Y()][Define_color] = estado
                        Define_color -= 1
                    jugador.set_X(jugador.get_X()+1)
                jugador.set_Y(jugador.get_Y()+1)
                Aux += 1
                jugador.set_X(contx)

            while jugador.get_Y() < conty+30:
                Define_color = contx
                while jugador.get_X() < contx+30:
                    while (Define_color+Aux) > contx:
                        mapa[jugador.get_Y()][Define_color+Aux] = estado
                        mapa[jugador.get_Y()][Define_color] = estado
                        Define_color -= 1
                    jugador.set_X(jugador.get_X()+1)
                jugador.set_Y(jugador.get_Y()+1)
                Aux -= 1
                jugador.set_X(contx)

    
            jugador.set_X(jugador.get_X())
            jugador.set_Y(jugador.get_Y())
            

            
            y = jugador.get_Y()
            x = jugador.get_X()
            Aux = 1
            Ver = False

            if y+30 >= ancho[0]:
                Ver = True

            if Ver == False:
                while mapa[y+30][x] == 0:
                    y += 1
                    if y+30 > ancho[0]:
                        Ver = True
                        break

            if Ver == False:
                contx = x
                conty = y
                while y < conty+15:
                    Define_color = contx
                    while x < contx+15:
                        while (Define_color+Aux) > contx:
                            mapa[y][Define_color+Aux] = jugador.color
                            mapa[y][Define_color] = jugador.color
                            Define_color -= 1
                        x += 1
                    y += 1
                    Aux += 1
                    x = contx
                while y < conty+30:
                    Define_color = contx
                    while x < contx+30:
                        while (Define_color+Aux) > contx:
                            mapa[y][Define_color+Aux] = jugador.color
                            mapa[y][Define_color] = jugador.color
                            Define_color -= 1
                        x += 1
                    y += 1
                    Aux -= 1
                    x = contx


                if(jugador.get_Y() != y):
                    daño = y-jugador.get_Y()
                    jugador.set_Vida(jugador.get_Vida()-daño)
                jugador.set_X(x)
                jugador.set_Y(y)

                #Actualiza la pantalla
                Terreno.dibuja_mapa(Pant,mapa)
                pygame.display.update()



def Borrar_Tanque(jugador,mapa):
    x = 0
    y = 0
    while y < ancho[0]:
        while x < largo[0]:
            if mapa[y][x] == jugador.color:
                mapa[y][x] = 0
            x += 1
        y += 1
        x = 0
    Terreno.dibuja_mapa(Pant,mapa)
    pygame.display.update()
            