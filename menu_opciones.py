from funciones_parcial import (formateo_dream_team_jugadores,
                                buscar_jugador_por_indice,
                                nombre_jugador_logros,
                                formateo_ordenados,
                                jugadores_salon_fama,
                                mostrar_jugador_estadisticas_max,
                                estadisticas_mayores_a_input,
                                excluir_jugador_min,
                                jugador_mayor_logros,
                                ordenar_por_posiciones,
                                lista_modificada,
                                formatear_y_guardar_ranking,
                                validar_numero,
                                formatear_posicion_cantidad,
                                formatear_all_star,
                                jugadores_max_estadisticas,
                                jugador_con_mejor_estadistica)

# 1
def imprimir_jugadores(lista_jugadores: list[dict]):
    '''
    Imprime de la lista todos los jugadores: nombre y posicion
    Parametros: list[dict]
    No retorna nada
    '''
    print(formateo_dream_team_jugadores(
        lista_jugadores))

# 2
def imprimir_estadisticas_jugador_indice(lista_jugadores: list[dict]):
    '''
    Muestra los datos del jugador que el usuario desee y, ademas, 
    lo guarda en formato csv.
    Parametro: list[dict]
    No retorna nada
    '''
    buscar_jugador_por_indice(
        lista_jugadores)

# 3
def imprimir_nombre_jugador_y_logros(lista_jugadores: list[dict]):
    '''
    Imprime el nombre del jugador y sus logros.
    Parametro: list[dict]
    No retorna nada
    '''
    print(nombre_jugador_logros(
        lista_jugadores))

# 4
def imprimir_asc_alfabeticamente_promedio_puntos(lista_jugadores: list[dict]):
    '''
    Imprime de forma alfabetica los nombres de los jugadores y su promedio 
    puntos por partido.
    Parametro: list[dict]
    No retorna nada
    '''
    formateo_ordenados(
        lista_jugadores, "promedio_puntos_por_partido")
# 5
def imprimir_jugador_salon_fama(lista_jugadores: list[dict]):
    '''
    Imprime si el nombre del jugador ingresado se encuentra en el 
    salon de la fama del baloncesto
    Parametro: list[dict]
    No retorna nada
    '''
    print(jugadores_salon_fama(
        lista_jugadores))

# 6
def imprimir_jugador_max_rebotes(lista_jugadores: list[dict]):
    '''
    Imprime los datos del jugador con mas rebotes totales.
    Parametros: list[dict]
    No retorna nada
    '''
    print(mostrar_jugador_estadisticas_max(
        lista_jugadores, "rebotes_totales"))
# 7
def imprimir_jugador_max_tiros_campo(lista_jugadores: list[dict]):
    '''
    Imprime los datos del jugador con mas porcentaje de tiros de campo.
    Parametros: list[dict]
    No retorna nada
    '''
    print(mostrar_jugador_estadisticas_max(
        lista_jugadores, "porcentaje_tiros_de_campo"))

# 8
def imprimir_jugador_max_asistencias_totales(lista_jugadores: list[dict]):
    '''
    Imprime los datos del jugador con mas asistencias totales.
    Parametros: list[dict]
    No retorna nada
    '''
    print(mostrar_jugador_estadisticas_max(
        lista_jugadores, "asistencias_totales"))
# 9
def imprimir_jugadores_promedio_puntos_por_partido(lista_jugadores: list[dict]):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input
    (promedio puntos por patido)
    Parametros: list[dict]
    No retorna nada
    '''
    print(estadisticas_mayores_a_input(
        lista_jugadores, "promedio_puntos_por_partido"))

# 10
def imprimir_jugadores_promedio_rebotes_por_partido(lista_jugadores: list[dict]):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input 
    (promedio rebotes por partido)
    Parametros: list[dict]
    No retorna nada
    '''
    print(estadisticas_mayores_a_input(
        lista_jugadores, "promedio_rebotes_por_partido"))
    
# 11
def imprimir_jugadores_promedio_asistencias_por_partido(lista_jugadores: list[dict]):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input 
    (promedio asistencias por partido)
    Parametros: list[dict]
    No retorna nada
    '''
    print(estadisticas_mayores_a_input(
        lista_jugadores, "promedio_asistencias_por_partido"))
    
# 12
def imprimir_jugador_max_robos_totales(lista_jugadores: list[dict]):
    '''
    Imprime los datos del jugador con mas robos totales.
    Parametros: list[dict]
    No retorna nada
    '''
    print(mostrar_jugador_estadisticas_max(
        lista_jugadores, "robos_totales"))
    
# 13
def imprimir_jugador_max_bloqueos_totales(lista_jugadores: list[dict]):
    '''
    Imprime los datos del jugador con mas bloqueos totales.
    Parametros: list[dict]
    No retorna nada
    '''
    print(mostrar_jugador_estadisticas_max(
        lista_jugadores, "bloqueos_totales"))
    
# 14
def imprimir_jugadores_porcentaje_tiros_libres(lista_jugadores: list[dict]):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input 
    (porcentaje de tiros libres)
    Parametros: list[dict]
    No retorna nada
    '''
    print(estadisticas_mayores_a_input(
        lista_jugadores, "porcentaje_tiros_libres"))
    
# 15
def imprimir_jugadores_y_excluir_al_menor_promedio_puntos_por_partido(
        lista_jugadores: list[dict]):
    '''
    Imprime el nombre de los jugadores y su estadistica correspondiente, 
    excluyendo al jugador con el menor numero
    Parametros: list[dict]
    No retorna nada
    '''
    print(excluir_jugador_min(
        lista_jugadores, "promedio_puntos_por_partido"))

# 16
def imprimir_jugador_max_logros(lista_jugadores: list[dict]):
    '''
    Imprime el nombre y logros del jugador con mas logros.
    Parametros: list[dict]
    No retorna nada

    '''
    print(jugador_mayor_logros(
        lista_jugadores))

# 17
def imprimir_jugadores_porcentaje_tiros_triples(lista_jugadores: list[dict]):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input 
    (porcentaje de tiros triples)
    Parametros: list[dict]
    No retorna nada
    '''
    print(estadisticas_mayores_a_input(
        lista_jugadores, "porcentaje_tiros_triples"))

# 18
def imprimir_jugador_max_temporadas(lista_jugadores: list[dict]):
    '''
    Imprime los datos del jugador con mas bloqueos temporadas.
    Parametros: list[dict]
    No retorna nada
    '''
    print(mostrar_jugador_estadisticas_max(
        lista_jugadores, "temporadas"))
    
# 19
def imprimir_jugadores_ordenados_posicion(lista_jugadores: list[dict]):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input 
    (porcentaje tiros de campo)
    Parametro: list[dict]
    No retorna nada
    '''
    print(estadisticas_mayores_a_input(ordenar_por_posiciones(
        lista_modificada(lista_jugadores)), "porcentaje_tiros_de_campo"))
    
# 23
def imprimir_ranking_de_jugadores(lista_jugadores: list[dict]):
    '''
    Imprime el nombre de los jugadores con sus lugares en el ranking de puntos, rebotes, 
    asistencias y robos.
    Paramentro: list[dict]
    No retorna nada
    '''
    formatear_y_guardar_ranking(lista_jugadores)
#1.1
def imprimir_cantidad_jugadores_por_posicion(lista_jugadores: list[dict]):
    '''
    Imprime las posiciones habidas en basquet y muestra cuantos jugadores
    corresponden a cada uno.
    Parametro: list[dict]
    No retorna nada.
    '''
    print(formatear_posicion_cantidad(lista_jugadores))

#1.2
def imprimir_jugadores_all_star(lista_jugadores: list[dict]):
    '''
    Imprime el nombre de los jugadores que al menos fueron 1 vez all stars
    y entre parentesis las veces que lo fueron, ordenado de forma descendente
    Parametro: list[dict]
    No retorna nada
    '''
    print(formatear_all_star(lista_jugadores))
#1.3
def imprimir_jugadores_max_estadisticas(lista_jugadores: list[dict]):
    '''
    Imprime las estadisticas formateadas y el nombre de quien es el maximo
    en dichas estadisticas y entre parentesis el valor de su estadistica.
    Parametro: list[dict]
    No retorna nada
    '''
    print(jugadores_max_estadisticas(lista_jugadores))

#1.4
def imprime_mejor_jugador_estadisticas(lista_jugadores: list[dict]):
    '''
    Imprime el jugador que tiene las mejores estadistica de todo el equipo
    Parametro: list[dict]
    No retorna nada
    '''
    print(jugador_con_mejor_estadistica(lista_jugadores))
########## MENU############
def menu_opciones():
    '''
    Print del menu de opciones.
    No tiene parametros.
    No retorna nada
    '''
    print(
        "-Menú de opciones-")
    print(
        "1. Mostrar todos los jugadores del Dream Team.")
    print(
        "2. Mostrar jugador seleccionado por indice y guardarlo en formato CSV.")
    print(
        "3. Buscar un jugador por nombre y mostrar sus logros.")
    print(
        "4. Mostrar promedio de puntos por partido de todo el equipo, ordenado de forma ascendente.")
    print(
        "5. Buscar un jugador por nombre y mostrar si es miembro del Salon de la Fama del Baloncesto.")
    print(
        "6. Mostrar jugador con mayor cantidad de rebotes totales.")
    print(
        "7. Mostrar jugador con mayor porcentaje de tiros de campo.")
    print(
        "8. Mostrar jugador con mayor cantidad de asistencias totales.")
    print(
        "9. Ingresar un valor y mostrar los jugadores que promediaron más puntos por partido que ese valor.")
    print(
        "10. Ingresar un valor y mostrar los jugadores que promediaron más rebotes por partido que ese valor.")
    print(
        "11. Ingresar un valor y mostrar los jugadores que promediaron más asistencias por partido que ese valor.")
    print(
        "12. Mostrar jugador con mayor cantidad de robos totales.")
    print(
        "13. Mostrar jugador con mayor cantidad de bloqueos totales.")
    print(
        "14. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.")
    print(
        "15. Mostrar promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
    print(
        "16. Mostrar jugador con mayor cantidad de logros obtenidos.")
    print(
        "17. Ingresar un valor y mostrar los jugadores que tuvieron un porcentaje de tiros triples superior a ese valor.")
    print(
        "18. Mostrar jugador con mayor cantidad de temporadas jugadas")
    print(
        "19. Ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor")
    print(
        "23. Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking.")
    print(
        "1.1. Mostrar posiciones y cuantos jugadores hay en ellas.")
    print(
        "1.2. Mostrar los all star de forma descendente.")
    print(
        "1.3. Mostrar mejor jugador en cada estadistica.")
    print(
        "1.4. Mostrar quien es el jugador con mejores estadistica de todos.")
    print(
        "0. Salir")
    print(
        " ")


def menu_principal_dream_team():
    '''
    Muestra el menu de opciones y la opcion a ingresar
    No tiene parametros
    No retorna nada
    '''
    menu_opciones()
    opcion = input("Ingrese una opción: ")

    return opcion


def dream_team_app(lista_jugadores: list):
    '''
    Muestra el menu de opciones, la opcion a ingresar y devuelve la opcion ingresada por consola
    Parametro: list
    No retorna nada
    '''
    copia_lista = lista_jugadores[:]
    if copia_lista:
        while True:
            opcion = menu_principal_dream_team()
            match opcion:
                case "1":
                    print("--------------------")
                    imprimir_jugadores(copia_lista)
                    print("--------------------")
                case "2":
                    print("--------------------")
                    imprimir_estadisticas_jugador_indice(copia_lista)
                    print("--------------------")
                case "3":
                    print("--------------------")
                    imprimir_nombre_jugador_y_logros(copia_lista)
                    print("--------------------")
                case "4":
                    print("--------------------")
                    imprimir_asc_alfabeticamente_promedio_puntos(copia_lista)
                    print("--------------------")
                case "5":
                    print("--------------------")
                    imprimir_jugador_salon_fama(copia_lista)
                    print("--------------------")
                case "6":
                    print("--------------------")
                    imprimir_jugador_max_rebotes(copia_lista)
                    print("--------------------")
                case "7":
                    print("--------------------")
                    imprimir_jugador_max_tiros_campo(copia_lista)
                    print("--------------------")
                case "8":
                    print("--------------------")
                    imprimir_jugador_max_asistencias_totales(copia_lista)
                    print("--------------------")
                case "9":
                    print("--------------------")
                    imprimir_jugadores_promedio_puntos_por_partido(copia_lista)
                    print("--------------------")
                case "10":
                    print("--------------------")
                    imprimir_jugadores_promedio_rebotes_por_partido(
                        copia_lista)
                    print("--------------------")
                case "11":
                    print("--------------------")
                    imprimir_jugadores_promedio_asistencias_por_partido(
                        copia_lista)
                    print("--------------------")
                case "12":
                    print("--------------------")
                    imprimir_jugador_max_robos_totales(copia_lista)
                    print("--------------------")
                case "13":
                    print("--------------------")
                    imprimir_jugador_max_bloqueos_totales(copia_lista)
                    print("--------------------")
                case "14":
                    print("--------------------")
                    imprimir_jugadores_porcentaje_tiros_libres(copia_lista)
                    print("--------------------")
                case "15":
                    print("--------------------")
                    imprimir_jugadores_y_excluir_al_menor_promedio_puntos_por_partido(
                        copia_lista)
                    print("--------------------")
                case "16":
                    print("--------------------")
                    imprimir_jugador_max_logros(copia_lista)
                    print("--------------------")
                case "17":
                    print("--------------------")
                    imprimir_jugadores_porcentaje_tiros_triples(copia_lista)
                    print("--------------------")
                case "18":
                    print("--------------------")
                    imprimir_jugador_max_temporadas(copia_lista)
                    print("--------------------")
                case "19":
                    print("--------------------")
                    imprimir_jugadores_ordenados_posicion(copia_lista)
                    print("--------------------")
                case "23":
                    print("--------------------")
                    imprimir_ranking_de_jugadores(copia_lista)
                    print("--------------------")
                case "1.1":
                    print("--------------------")
                    imprimir_cantidad_jugadores_por_posicion(copia_lista)
                    print("--------------------")
                case "1.2":
                    print("--------------------")
                    imprimir_jugadores_all_star(copia_lista)
                    print("--------------------")
                case "1.3":
                    print("--------------------")
                    imprimir_jugadores_max_estadisticas(copia_lista)
                    print("--------------------")
                case "1.4":
                    print("--------------------")
                    imprime_mejor_jugador_estadisticas(copia_lista)
                    print("--------------------")
                case "0":
                    break
                case _:
                    print("--------------------")
                    print("Ingrese una opcion que aparezca en el menú.")
                    print("--------------------")
    else:
        print("No existe la lista")
