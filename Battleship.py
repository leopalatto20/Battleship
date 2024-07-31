#importamos 2 librerias que vamos a necesitar para que el programa funcione
import random

#Mostramos las instrucciones al usuario
print("Bienvenido a battleship\n"
      "Ingresa la dificultad que deseas jugar\n"
      "En la dificultad facil el tablero es de 8x8 y tienes 15 intentos para darle a 5 barcos\n"
      "En la dificultad dificil el tablero es de 9x9 y solo tienes 10 intentos para darle a 7 barcos")


#declaramos nuestras posibles dificultades dentro de una lista para usarlas en la comprobacion de datos
posibles_dificultades = ["F", "D"]
#pedimos la dificultad al usuario, usamos upper para evitar problemas con minusculas
dificultad = input("Ingresa tu dificultad (F/D)").upper()
#si la dificultad no esta dentro de las posibles dificultades, mostramos error y la seguimos pidiendo
while dificultad not in posibles_dificultades:
    print("Ingresa una dificultad valida")
    dificultad = input("Ingresa tu dificultad (F/D): ")#cuando la dificultad sea correcta rompemos el ciclo y seguimos
#si la dificulad ingresada es F declaramos todas nuestras variables a los valores que le corresponden a la dificultad facil
if dificultad == "F":
    filas = 8
    columnas = 8
    intentos = 15
    largo_del_tablero = "  A B C D E F G H"
    numero_limite = 7
    posibles_columnas = "(A-H)"
    posibles_filas = "(1-8)"
    numero_barcos = 5
#si la dificultad es dificil hacemos lo mismo pero cambiamos la variables a los valores que le corresponden a la dificultad dificil
elif dificultad == "D":
    filas = 9
    columnas = 9
    intentos = 10
    largo_del_tablero = "  A B C D E F G H I "
    numero_limite = 8
    posibles_columnas = "(A-I)"
    posibles_filas = "(1-9)"
    numero_barcos = 7



#declaramos una funcion para crear el tablero que va a usar el usuario
def crear_tablero(filas, columnas):
#declaramos el tablero inicial como una lista vacia
    tablero = []
    #ciclo for que se va a repetir el numero de veces que tenga asignada la variable filas
    for i in range(filas):
        #multiplicamos una lista con un solo valor por el numero de columnas, el cual es el mismo numero que el numero de filas
        fila = ["O"]*columnas
        #añadimos esa nueva fila a nuestro tablero
        tablero.append(fila)
    #este ciclo se repite 8 veces para el modo facil y 9 veces para el modo dificiil, al terminar el ciclo la funcion regresa el tablero para poder usarlo
    return tablero




def imprimir_tablero(tablero, largo_del_tablero):
    #imprimimos las letras que estan en la parte de arriba del tablero para ayudar al usuario con sus tiradas
    print(largo_del_tablero)
    #declaramos el numero de fila como 1 para imprimirlo con cada fila
    numero_fila=1
    #ciclo for que va a iterar cada fila dentro de nuestro tablero
    for fila in tablero:
        #%d y %s son reemplazados por el numero de fila actual, y por una linea vertical que se usa como espaciador entre casillas
        print("%d|%s|" % (numero_fila, "|".join(fila)))
        #despues de cada iteracion le sumamos 1 al numero de fila para crear el formato de tablero
        numero_fila +=1



#funcion que nos regresa coordenadas vacias para poder poner barcos ahi
def coordenadas_barcos(tablero):
    #ciclo infinito
    while True:
        #pedimos a la libreria random 1 numero aleatorio desde 0 hasta el largo del tablero, esto dos veces una para fila y una para columna
        fila = random.randrange(0,len(tablero))
        columna = random.randrange(0,len(tablero))
        #si la fila y la columna que tenemos en el tablero es igual a "O" regresamos esos valores como valores finales
        if tablero[fila][columna] == "O":
            return fila, columna



#funcion para poner los barcos dentro del tablero que queramos
def poner_barcos(tablero, numero_barcos):
    #ciclo for que se repite desde 0 hasta el numero de barcos para usar la cantidad que el usuario nos pidio
    for i in range(numero_barcos):
        #fila y columna toman el valor que la funcion anterior de coordenadas barcos regresa
        fila, columna = coordenadas_barcos(tablero)
        #cambiamos esa celda por una x solo en el tablero que no vamos a mostrar al usuario
        tablero2[fila][columna] = "X"


#hacemos un diccionario con las posibles letras que podemos tener en las tiradas y su equivalente en numero
letra_a_numero = {'A':1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9}
#funcion para pedir las coordenadas al usuario
def pedir_coordenadas():
    #ciclo infinito para comprobar las coordenadas
    while True:
        print("Ingresa tu fila", posibles_filas)
        #pedimos la fila al usuario
        fila = input("Ingresa tu fila:")
        #si lo que nos dio el usuario es un numero continuamos
        if fila.isdigit():
            #convertimos el numero a un entero y le restamos uno para que sirva con la matriz
            fila = int(fila)-1
            #comprobamos el numero que nos dio el usuario, si es menor o igual al numero de filas en el tablero continuamos y dejamos ese valor como el final
            if fila <= numero_limite:
                break
            #en caso de que alguna de estas condiciones no se cumpla mostramos error
            else:
                print("Ingresa una fila valida")
        else:
            print("Ingresa una fila valida")
        #ciclo infinito ahora para la columna
    while True:
        print("Ingresa tu columna", posibles_columnas)
        #pedimos la letra al usuario y usamos upper para hacerla mayuscula y que sirva con nuestro diccionario, tambien agregamos strip para borrar espacios vacios en caso de que el usuario de enter sin escribir nada
        columna = input("Ingresa tu columna: ").strip().upper()
        #si la columna es un espacio vacio mostramos error y la reiniciamos el ciclo para seguirla pidiendo
        if not columna:
            print("Ingresa una columna valida")
            continue
        #comprobamos que la letra este dentro de las posibles opciones
        if columna in "ABCDEFGHI":
            #usamos el diccionario para convertir la letra a un numero y le restamos 1 para usarlo con la matriz
            columna = letra_a_numero[columna]-1
            #si el numero que tenemos es menor o igual al numero de filas lo aceptamos y rompemos el ciclo
            if columna <= numero_limite:
                break
            else:
                print("Ingresa una columna valida")
        else:
            print("Ingresa una columna valida")
            #regresamos ambas variables para usarlas
    return fila, columna


#creamos 2 tableros, uno para mostrarlo al usuario y el otro para calificar las tiradas en ese
tablero1 = crear_tablero(filas, columnas)
tablero2 = crear_tablero(filas, columnas)
#mostramos el tablero vacio al usuario
imprimir_tablero(tablero1, largo_del_tablero)
print("Este es el tablero en el que vas a jugar, ahora el programa va a poner 5 barcos aleatoriamente")
#ponemos la cantidad de barcos que le corresponden a esa dificultad en el tablero
poner_barcos(tablero2, numero_barcos)
print("Los barcos ya estan puestos en el tablero\n"
      "Ya puedes comenzar a tirar")
#esto solo esta para que se pueda probar que las tiradas sirven, en el juego normal no estaría
imprimir_tablero(tablero2, largo_del_tablero)
#ciclo que se repite mientras que el usuario tenga mas de 0 intentos
while intentos > 0:
    #siempre mostramos cuantos intentos queda al principio de cada iteracion
    print(f"Te quedan {intentos} intentos")
    #mostramos el tablero 1 ya con los barcos puestos, el usuario no puede verlos porque los barcos visuales estan en el tablero 2
    imprimir_tablero(tablero1, largo_del_tablero)
    #usamos la funcion pedir coordenadas y asignamos los valores que regresa a variables
    x,y = pedir_coordenadas()
    #si la tirada del usuario da en una celda con una x significa que hundio un barco
    if tablero2[x][y] == "X":
        #le restamos 1 al numero de barcos
        numero_barcos -= 1
        #mostramos al usuario cuantos barcos quedan ahora
        print(f"Hundiste un barco, ahora quedan {numero_barcos} barcos.")
        #cambiamos esa celda a una H de hundido en AMBOS TABLEROS
        tablero2[x][y]= "H"
        tablero1[x][y] = "H"
        #si la tirada del usuario cae en una celda con una I o una H significa que ya tiro ahi, asi que mostramos ese mensaje
    elif tablero1[x][y] == "I" or tablero1[x][y] == "H":
        print("Ya tiraste ahi")
        #si ninguna de estas cosas pasa significa que no hay ningun barco ahi, asi que cambiamos la celda por una I
    else:
        print("No hay ningun barco ahi")
        tablero1[x][y] = "I"
    #despues de TODAS LAS TIRADAS, le restamos 1 al numero de intentos
    intentos -= 1
    #si el numero de barcos es igual a 0 significa que el usuario hundio todos los barcos
    if numero_barcos == 0:
        print("Hundiste todos los barcos")
        print("Ganaste el juego")
        #rompemos el ciclo cuando esto pase
        break
#si los intentos del usuario llegan a 0 el usuario pierde y mostramos el mensaje
if intentos == 0:
    print("Se acabaron tus intentos, perdiste")
