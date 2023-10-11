#
#   Proyecto 1
#El proyecto de este curso consistirá en un videojuego de texto de recorrer laberintos.
#Este consistirá de laberintos representados por caracteres ASCII dónde # representará una pared, 
#. un pasillo y P el personaje
#
#Podrás moverte por el mapa usando las teclas ↑ ↓ ← → de tu teclado.
#

from os import system #Libreria de Evento de Sistema
import keyboard #libreria de eventos del teclado
#################################################
#   VARIABLES DEL SISTEMA

#Variable con laverinto 
laberinto = [
    ['P','.','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
    ['.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
    ['#','.','#','.','#','#','#','#','#','.','#','#','#','#','#','#','#','#','#','.','#'],
    ['#','.','#','.','.','.','.','.','.','.','.','.','.','.','#','.','#','.','#','.','#'],
    ['#','.','#','#','#','#','#','.','#','.','#','#','#','.','#','.','#','.','#','.','#'],
    ['#','.','.','.','#','.','#','.','#','.','#','.','.','.','.','.','#','.','.','.','#'],
    ['#','.','#','.','#','.','#','#','#','#','#','#','#','.','#','.','#','#','#','#','#'],
    ['#','.','#','.','.','.','#','.','.','.','.','.','#','.','#','.','.','.','#','.','#'],
    ['#','#','#','#','#','.','#','#','#','#','#','.','#','.','#','.','#','#','#','.','#'],
    ['#','.','#','.','#','.','#','.','.','.','.','.','.','.','#','.','.','.','#','.','#'],
    ['#','.','#','.','#','.','#','#','#','#','#','#','#','.','#','#','#','#','#','.','#'],
    ['#','.','.','.','#','.','.','.','#','.','.','.','#','.','#','.','#','.','.','.','#'],
    ['#','#','#','.','#','.','#','#','#','#','#','.','#','.','#','.','#','#','#','.','#'],
    ['#','.','#','.','.','.','#','.','.','.','.','.','.','.','#','.','.','.','.','.','#'],
    ['#','.','#','.','#','.','#','#','#','.','#','.','#','.','#','#','#','.','#','.','#'],
    ['#','.','.','.','#','.','#','.','.','.','#','.','#','.','.','.','.','.','#','.','#'],
    ['#','#','#','.','#','#','#','#','#','#','#','.','#','#','#','.','#','#','#','.','#'],
    ['#','.','#','.','#','.','#','.','#','.','#','.','.','.','.','#','#','.','.','.','#'],
    ['#','.','#','.','#','.','#','.','#','.','#','.','#','.','#','.','#','.','#','.','#'],
    ['#','.','.','.','.','.','#','.','.','.','.','.','#','.','#','.','#','.','#','.','#'],
    ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','.','.'],
]
old_posicion = [0,0]            #POSISION ACTUAL DEL JUGADOR
new_posicion = [0,0]            #NUEVA POSISION DEL JUGADOR
pasillo = '.'                   #DEFINIR DONDE PUEDE MOVERSE EL JUGADOR
jugador = ''                    #DEFINIR VARIABLE DEL JUGADOR

titulo = 'Juego del Laberinto'              #mensaje de titulo
subtitulo = '====================================================\n\tDescripcion:\nEl proyecto de este curso consistirá en un videojuego de texto de recorrer laberintos.\nEste consistirá de laberintos representados por caracteres ASCII dónde # representará una pared,\n. un pasillo y P el personaje\n Podrás moverte por el mapa usando las teclas ↑ ↓ ← → de tu teclado.\n \t\t"q" para salir\n====================================================' #Mensaje de Descripcion
print(titulo)                               #Mostrar Titulo
jugador = input('\nNombre del Jugador: ')   #Ingreso de Nombre 
system("cls")                               #limpiar Pantalla

#inicio del Recorrido
while True:
    
    #########################################################
    # RECORRER EL LABERINDO PARA SABER DONDE ESTA EL JUGADOR
    for row in range(len(laberinto)):
        for col in range(len(laberinto[0])):
            if(laberinto[row][col] == 'P'):
                old_posicion = [row, col]    

    #########################################################
    # EVENTOS DEL TECLADO
    if keyboard.is_pressed('q'):                        #   Salir del laberinto 
         break                                          #SALIR DEL LABERINTO
    
    elif keyboard.is_pressed('right'):                  #   Moverse a la Derecha
        if(old_posicion[1] < len( laberinto[0] ) ):       #DEFINIR QUE EL NO SOBREPASE EL ANCHO DEL LABERINTO
            new_posicion[1] = old_posicion[1] + 1   #MOVER AL JUGADOR 1 POSICION HACIA LA DERECHA DE LA COLUMNA
            new_posicion[0] = old_posicion[0]       #MANTENER LA POSICION DE LA FILA QUE ESTA EL JUGADOR        

    elif keyboard.is_pressed('left'):                   #   Moverse a la Izquierda
        if(old_posicion[1] > 0 ):                       #DEFINIR QUE EL JUGADOR NO SERA MENOR QUE EL INICIO DEL LABERINTO
                new_posicion[1] = old_posicion[1] - 1   #MOVER AL JUGADOR 1 POSICION HACIA LA IZQUIERDA DE LA COLUMNA
                new_posicion[0] = old_posicion[0]       #MANTENER LA POSICION DE LA FILA QUE ESTA EL JUGADOR

    elif keyboard.is_pressed('down'):                   #   Moverse hacia Abajo
        if(old_posicion[0] < len(laberinto) ):          #DEFINIR QUE EL NO SOBREPASE EL ALTO DEL LABERINTO
                new_posicion[0] = old_posicion[0] + 1   #MOVER AL JUGADOR 1 POSICION HACIA LA ABAJO DE LA FILA
                new_posicion[1] = old_posicion[1]       #MANTENER LA POSICION DE LA COLUMNA QUE ESTA EL JUGADOR

    elif keyboard.is_pressed('up'):                     #   Moverse hacia Arriba
        if(old_posicion[0] > 0 ):                       #DEFINIR QUE EL NO SOBREPASE EL INICIO DEL LABERINTO
                new_posicion[0] = old_posicion[0] - 1   #MOVER AL JUGADOR 1 POSICION HACIA LA ARRIBA DE LA FILA
                new_posicion[1] = old_posicion[1]       #MANTENER LA POSICION DE LA COLUMNA QUE ESTA EL JUGADOR                                                                       
    
    elif( laberinto[new_posicion[0]][new_posicion[1]] == pasillo ):         #DEFINIR SI EL JUGADOR SE A MOVIDO Y ES PASILLO EL JUGADOR PUEDE MOVERSE        
            laberinto[new_posicion[0]][new_posicion[1]] = 'P'               #SE AGREGA LA NUEVA POSICION DEL JUGADOR
            laberinto[old_posicion[0]][old_posicion[1]] = '.'               #SE AGREGA POSICION ANTERIOR DEL JUGADOR COMO PASILLO POR SI DESEA REGRESAR
    
    ########################################################
    # Mostrar el Laberinto
    ########################################################
    system('cls')  
    print('\n\t',titulo,'\n',subtitulo,'\n\nBienvenid@',jugador)
    str_row = ""
    print('\n')
    for row in laberinto:
        str_row += "\n"    
        for col in row:
            str_row += col
    print(str_row)

    print(old_posicion, ' , ', new_posicion, 'alto: ',len(laberinto), ' ancho: ',len(laberinto[0]))     #MOSTRAR POSICION ACTUA DEL JUGADOR
    #########################################################
    # DEFINIR SI EL JUGADOR SOBRE PASA EL ALTO DEL LABERINTO 
    if(new_posicion[0] == len(laberinto)-1 and new_posicion[1] == len(laberinto[0])-1 ):  
        print('\nFelicidades',jugador,'as completado el Laberinto !\n')                 #MOSTRAR MENSAJE DE VENCEDOR
        break                                                                           #TERMINA EL CICLO 
    keyboard.read_event()                               # Esperar Evento del teclado 
    
    
    

print('Gracias Por Jugar')
print('Presione una tecla para salir ......')
keyboard.read_event() 
exit()