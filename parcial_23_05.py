#ENTREGA LUNES 29/05 18:30
import json
import csv
import re

########################### AUXILIARES #############################

def leer_archivo(path_completo: str):
    '''
    Lee el archivo .json por ruta
    Parametros: ruta en str
    Retorna la lectura del json
    '''

    with open(path_completo, "r") as archivo:
        return list[dict](json.load(archivo)["jugadores"])

def validar_numero(numero: str)-> bool:
    '''
    Valida si el dato ingresado es un numero, sea int o float
    Parametro: str
    Retorna un booleando
    '''
    if type(str(numero)) is str:
        valor_reemplazado = numero.strip().replace(".","")
        if valor_reemplazado.isnumeric():
            return True
        else:
            return False
        
def formatear_claves(clave: str):
    '''
    Formatea las palabras de las claves de estadisticas
    Parametro: str
    Retorna la palabra formateada
    '''
    if "_" in clave:
        return clave.replace("_", " ").capitalize()
    else:
        return clave.capitalize()

def evaluar_palabras(palabra: str):
    '''
    Evalua si la palabra u oracion ingresada son letras
    Parametro: str
    Retorna True o False
    '''
    evaluar_nombre = palabra.strip().lower().replace(" ","")
    if evaluar_nombre.isalpha() == True:
        return True
    else:
        return False

def guardar_archivo_csv(nombre_archivo: str, contenido: str):
    '''
    Guarda con nombre y contenido pasado por parametro en formato csv
    Parametro: contenido -> string
    Retorna un booleano
    '''

    with open (nombre_archivo, "w+") as archivo:
        archivo_csv = archivo.write(contenido)

    if archivo_csv > 0:
        print("Se creó el archivo correctamente")
        return True
    else:
        print("Error al guardar el archivo.")
        return False

def sumar_estadisticas(lista_jugadores: list, clave: str):
    '''
    Operacion matematica sumar
    Parametro: list - str
    Retorna la suma
    '''
    copia_lista = lista_jugadores[:]
    suma = 0
    for jugadores in copia_lista:
        for claves, valores in jugadores["estadisticas"].items():
            if claves == clave:
                suma += valores
    return suma

def dividir(dividendo: float, divisor: float) -> float:
    '''
    Operacion matematica dividir
    Parametro: ambos parametros pueden ser int o float
    Retorna el resultado de la division en int o float
    '''

    if divisor > 0:
        resultado = dividendo / divisor
        return resultado
    elif divisor == 0: 
        return 0

def calcular_promedio(lista_jugadores: list, clave: str):
    '''
    Calcula y muestra el promedio de lo pasado por parametro
    Parametro: list - str
    Retorna el resultado del promedio
    '''
    copia_lista = lista_jugadores[:]
    promedio = dividir(
        sumar_estadisticas(copia_lista, clave), len(copia_lista))
    return promedio

def calcular_jugador_max_estadisticas(lista_jugadores: list, clave: str):
    '''
    Muestra el jugador maximo 
    Parametro: list - str - str
    Retorna el jugador maximo o minimo.
    '''
    copia_lista = lista_jugadores[:]
    lista_aux = {}
    for jugador in copia_lista:
        if not lista_aux:
            lista_aux = jugador
        else:
            if lista_aux["estadisticas"][clave] < jugador["estadisticas"][clave]:
                lista_aux = jugador
    return lista_aux

def calcular_jugador_min_estadisticas(lista_jugadores: list, clave: str):
    '''
    Muestra el jugador maximo 
    Parametro: list - str - str
    Retorna el jugador maximo o minimo.
    '''
    copia_lista = lista_jugadores[:]
    lista_aux = {}
    for jugador in copia_lista:
        if not lista_aux:
            lista_aux = jugador
        else:
            if lista_aux["estadisticas"][clave] > jugador["estadisticas"][clave]:
                lista_aux = jugador
    return lista_aux

def lista_dict_nombres(lista_jugadores: list[dict], clave: str):
    '''
    Crea una lista donde se almacenaran los nombres y la clave a eleccion.
    Parametro: list[dict] - str
    Retorna la lista.
    '''
    copia_lista = lista_jugadores[:]
    lista_nombres_puntos = []
    for jugadores in copia_lista:
        for claves in jugadores["estadisticas"].keys():
            if claves == clave:
                lista_nombres_puntos.append({"nombre": jugadores["nombre"],
                                             clave: jugadores["estadisticas"][clave]})
    return lista_nombres_puntos

#1
def formateo_dream_team_jugadores(lista_jugadores: list):
    '''
    Muestra y formatea el nombre y la posicion de todos los jugadores
    Parametros: list
    No retorna nada
    '''
    for jugador in lista_jugadores:
        print("{0} - {1}".format(jugador["nombre"], jugador["posicion"]))

#2
def buscar_jugador_por_indice(lista_jugadores: list):
    '''
    Hace ingresar un numero por input, el cual es el indice que llama al jugador correspondiente.
    Parametros: list
    Retorna los datos del jugador llamado.
    '''
    copia_lista = lista_jugadores
    indice_jugador = input(
    "Ingrese un numero del 0 al 11 para mostrar la informacion del jugador: ")
    lista_formateada = []
    if (validar_numero(indice_jugador) == True and 
            re.match(r"^(?:1[0-1]|[0-9])$", indice_jugador)):
        jugador = copia_lista[int(indice_jugador)]
        lista_formateada.append("Nombre: {0},\nPosicion: {1},".format(
                            jugador["nombre"], jugador["posicion"]))
        for claves, valor in jugador["estadisticas"].items():
            lista_formateada.append("{0}: {1},".format(formatear_claves(claves), valor))
        lista_formateada = "\n".join(lista_formateada)
        print(lista_formateada)
        guardar_archivo_csv("jugador_elegido.csv", lista_formateada)
    else:
        print("ERROR. No existe el jugador.")

#3
def nombre_jugador_logros(lista_jugadores: list):
    '''
    Busca si el jugador ingresado por input coincide con los que se encuentran en la lista.
    Parametro: list
    Retorna un texto formateado con los datos del jugador
    '''
    copia_lista = lista_jugadores[:]
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    flag = 0
    while evaluar_palabras(nombre_jugador) == True:
        for jugador in copia_lista:
            if nombre_jugador == jugador["nombre"] and flag == 0:
                jugador_elegido = ("Nombre jugador: {0}\nLogros: \n{1}".
                    format(jugador["nombre"], "\n".join(jugador["logros"])))
                flag = 1
        if flag == 1:
            return jugador_elegido
        else:
            return "ERROR"
    else:
        return "Error, ingrese correctamente."

#4
def ordenar_claves_o_numeros(lista_jugadores:list, clave: str):
    '''
    Ordena las claves pasadas por parametro
    Parametros: list - str
    Retorna la lista modificada.
    '''
    copia_lista = lista_jugadores[:]
    longitud_lista = len(copia_lista)
    bandera_swap = True
    while bandera_swap:
        bandera_swap = False
        longitud_lista = longitud_lista - 1
        for indice in range(longitud_lista):
            if copia_lista[indice][clave] > copia_lista[indice+1][clave]:
                copia_lista[indice], copia_lista[indice+1] = copia_lista[indice+1], copia_lista[indice]
                bandera_swap = True
    return copia_lista


def formateo_ordenados(lista_jugadores: list, clave: str):
    '''
    Formateo de string de los nombres y sus promedios.
    Parametro: list
    No retorna nada
    '''
    copia_lista = lista_jugadores[:]
    lista = lista_dict_nombres(copia_lista, clave)
    lista = ordenar_claves_o_numeros(lista, "nombre")
    for jugadores in lista:
        for claves, valores in jugadores.items():
            print("{0}: {1}".format(formatear_claves(claves), valores))

#5
def jugadores_salon_fama(lista_jugadores: list):
    '''
    Busca si el nombre del jugador ingresado por input es miembro o no del salon de la fama del baloncesto
    Parametro: list
    Retorna string formateado
    '''
    copia_lista = lista_jugadores[:]
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    flag = 0
    if evaluar_palabras(nombre_jugador) == True:
        for jugador in copia_lista:
            if nombre_jugador.capitalize() == jugador["nombre"].capitalize():
                for logros in jugador["logros"]:
                    if (logros in "Miembro del Salon de la Fama del Baloncesto"
                        and flag == 0):
                        dato = (
                            "{0} es Miembro del Salon de la Fama del Baloncesto."
                            .format(jugador["nombre"]))
                        flag = 1
        if flag == 1:
            return dato
        else:
            return "{0} no es miembro.".format(nombre_jugador)
    else:
        return "Error, ingrese correctamente."

#7, 8, 9, 13, 14, 19
def mostrar_jugador_estadisticas_max(lista_jugadores: list, clave: str):
    '''
    Muestra el jugador maximo dependiendo de lo pasado por parametro clave
    Parametro: list - str
    Retorna los datos del jugador formateado
    '''
    copia_lista = lista_jugadores[:]
    texto_formateado = []
    jugador = calcular_jugador_max_estadisticas(copia_lista, clave)
    texto_formateado.append("Nombre: {0}\nPosicion: {1}"
                            .format(jugador["nombre"], jugador["posicion"]))
    for claves, valor in jugador["estadisticas"].items():
        if claves == clave:
            texto_formateado.append("{0}: {1}".format(formatear_claves(clave), valor))
    texto_formateado = "\n".join(texto_formateado)

    return texto_formateado

#10, 11, 12, 15, 18
def estadisticas_mayores_a_input(lista_jugadores: list, clave: str):
    '''
    Muestra los jugadores que esten por encima del numero ingresado por input.
    Parametro= list - str
    Retorna nombre de los jugadores.
    '''
    copia_lista = lista_jugadores[:]
    numero = input("Ingrese un número: ")
    nombres_jugadores = []
    if validar_numero(numero) == True:
        for jugadores in copia_lista:
            if (jugadores["estadisticas"][clave] > float(numero)):
                nombres_jugadores.append(
                    "Nombre: {0}".format(jugadores["nombre"]))
        if len(nombres_jugadores) > 0:
            nombres_jugadores = "\n".join(nombres_jugadores)
            return nombres_jugadores
        else:
            return "No hay jugadores por encima del valor ingresado."
    else:
        print("ERROR. Ingrese un numero.")

#16
def excluir_jugador_min(lista_jugadores: list, clave: str):
    '''
    Muestra a todos los jugadores menos el menor del dato pasado por parametro
    Parametro: list - str
    No retorna nada
    '''
    copia_lista = lista_jugadores[:]
    jugador_min = calcular_jugador_min_estadisticas(copia_lista, clave)
    resultado_excluir_min = (sumar_estadisticas(copia_lista, clave) 
                            - jugador_min["estadisticas"][clave])
    promedio = resultado_excluir_min / (len(copia_lista) - 1)
    texto_formateado = []
    texto_formateado.append("{0}: {1}".format(
                    formatear_claves(clave).capitalize(),promedio))
    for jugador in copia_lista:
        if jugador != jugador_min:
            texto_formateado.append("Nombre: {0}\n{1}: {2}"
                    .format(jugador["nombre"], formatear_claves(clave), jugador["estadisticas"][clave]))
            
    texto_formateado.append("\nJugador excluido {0}".format(jugador_min["nombre"]))
    texto_formateado = "\n".join(texto_formateado)
    return texto_formateado

#17
def jugador_mayor_logros(lista_jugadores: list):
    '''
    Imprime al jugador con mayores logros
    Parametro: list
    Retorna el nombre y sus logros
    '''
    copia_lista = lista_jugadores[:]
    lista_aux = {}
    lista_logros = []
    for jugador in copia_lista:
        if not lista_aux:
            lista_aux = jugador
        else:
            if len(lista_aux["logros"]) < len(jugador["logros"]):
                lista_aux = jugador
    for logros in lista_aux["logros"]:
        lista_logros.append(logros)
    lista_logros = "\n".join(lista_logros)
    return "Nombre: {0}\n-Logros- \n{1}".format(lista_aux["nombre"], lista_logros)

#20
def lista_modificada(lista_jugadores: list) -> list:
    '''
    Modifica la lista intercambiando las posiciones por numeros
    Parametros: list
    Retorna una lista modificada
    '''
    copia_lista = lista_jugadores [:]
    for jugadores in copia_lista:
        if jugadores["posicion"] == "Base":
            jugadores["posicion"] = 1
        elif jugadores["posicion"] == "Escolta":
            jugadores["posicion"] = 2
        elif jugadores["posicion"] == "Alero":
            jugadores["posicion"] = 3
        elif jugadores["posicion"] == "Ala-Pivot":
            jugadores["posicion"] = 4
        elif jugadores["posicion"] == "Pivot":
            jugadores["posicion"] = 5
        else:
            return "No funciona"

    return copia_lista

def ordenar_por_posiciones(lista_jugadores: list):
    '''
    Ordena y cambia las posiciones de numeros a las posiciones correspondientes
    Parametro: list
    Retorna la lista ordenada y modificada
    '''
    copia_lista = lista_jugadores[:]
    lista_ordenada = ordenar_claves_o_numeros(copia_lista, "posicion")
    for jugadores in lista_ordenada:
        if jugadores["posicion"] == 1:
            jugadores["posicion"] = "Base"
        elif jugadores["posicion"] == 2:
            jugadores["posicion"] = "Escolta"
        elif jugadores["posicion"] == 3:
            jugadores["posicion"] = "Alero"
        elif jugadores["posicion"] == 4:
            jugadores["posicion"] = "Ala-Pivot"
        elif jugadores["posicion"] == 5:
            jugadores["posicion"] = "Pivot"

    return lista_ordenada

print()

################################ FIN AUXILIARES #################################
############################### OPCION FUNCIONES ################################
#1
def imprimir_jugadores(lista_jugadores: list):
    '''
    Imprime de la lista todos los jugadores: nombre y posicion
    Parametros: list
    No retorna nada
    '''
    formateo_dream_team_jugadores(
                            lista_jugadores)
        
#2
def imprimir_estadisticas_jugador_indice(lista_jugadores: list):
    '''
    Muestra los datos del jugador que el usuario desee y, ademas, 
    lo guarda en formato csv.
    Parametro: list
    No retorna nada
    '''
    buscar_jugador_por_indice(
                            lista_jugadores)

#3    
def imprimir_nombre_jugador_y_logros(lista_jugadores: list):
    '''
    Imprime el nombre del jugador y sus logros.
    Parametro: list
    No retorna nada
    '''
    print(nombre_jugador_logros(
                            lista_jugadores))

#4
def imprimir_asc_alfabeticamente_promedio_puntos(lista_jugadores: list):
    '''
    Imprime de forma alfabetica los nombres de los jugadores y su promedio 
    puntos por partido.
    Parametro: list
    No retorna nada
    '''
    formateo_ordenados(
                    lista_jugadores, "promedio_puntos_por_partido")
#5
def imprimir_jugador_salon_fama(lista_jugadores: list):
    '''
    Imprime si el nombre del jugador ingresado se encuentra en el 
    salon de la fama del baloncesto
    Parametro: list
    No retorna nada
    '''
    print(jugadores_salon_fama(
                            lista_jugadores))

#6
def imprimir_jugador_max_rebotes(lista_jugadores: list):
    '''
    Imprime los datos del jugador con mas rebotes totales.
    Parametros: list
    No retorna nada
    '''
    print(mostrar_jugador_estadisticas_max(
                            lista_jugadores, "rebotes_totales"))
#7
def imprimir_jugador_max_tiros_campo(lista_jugadores: list):
    '''
    Imprime los datos del jugador con mas porcentaje de tiros de campo.
    Parametros: list
    No retorna nada
    '''
    print(mostrar_jugador_estadisticas_max(
                            lista_jugadores, "porcentaje_tiros_de_campo"))

#8
def imprimir_jugador_max_asistencias_totales(lista_jugadores: list):
    '''
    Imprime los datos del jugador con mas asistencias totales.
    Parametros: list
    No retorna nada
    '''
    print(mostrar_jugador_estadisticas_max(
                            lista_jugadores, "asistencias_totales"))
#9
def imprimir_jugadores_promedio_puntos_por_partido(lista_jugadores: list):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input
    (promedio puntos por patido)
    Parametros: list
    No retorna nada
    '''
    print(estadisticas_mayores_a_input(
                            lista_jugadores, "promedio_puntos_por_partido"))

#10
def imprimir_jugadores_promedio_rebotes_por_partido(lista_jugadores: list):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input 
    (promedio rebotes por partido)
    Parametros: list
    No retorna nada
    '''
    print(estadisticas_mayores_a_input(
                            lista_jugadores, "promedio_rebotes_por_partido"))
#11
def imprimir_jugadores_promedio_asistencias_por_partido(lista_jugadores: list):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input 
    (promedio asistencias por partido)
    Parametros: list
    No retorna nada
    '''
    print(estadisticas_mayores_a_input(
                        lista_jugadores, "promedio_asistencias_por_partido"))
#12
def imprimir_jugador_max_robos_totales(lista_jugadores: list):
    '''
    Imprime los datos del jugador con mas robos totales.
    Parametros: list
    No retorna nada
    '''
    print(mostrar_jugador_estadisticas_max(
                            lista_jugadores, "robos_totales"))
#13
def imprimir_jugador_max_bloqueos_totales(lista_jugadores: list):
    '''
    Imprime los datos del jugador con mas bloqueos totales.
    Parametros: list
    No retorna nada
    '''
    print(mostrar_jugador_estadisticas_max(
                            lista_jugadores, "bloqueos_totales"))
#14
def imprimir_jugadores_porcentaje_tiros_libres(lista_jugadores: list):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input 
    (porcentaje de tiros libres)
    Parametros: list
    No retorna nada
    '''
    print(estadisticas_mayores_a_input(
                            lista_jugadores, "porcentaje_tiros_libres"))
#15
def imprimir_jugadores_y_excluir_al_menor_promedio_puntos_por_partido(
                                                        lista_jugadores: list):
    '''
    Imprime el nombre de los jugadores y su estadistica correspondiente, 
    excluyendo al jugador con el menor numero
    Parametros: list
    No retorna nada
    '''
    print(excluir_jugador_min(
                            lista_jugadores, "promedio_puntos_por_partido"))
#16
def imprimir_jugador_max_logros(lista_jugadores: list):
    '''
    Imprime el nombre y logros del jugador con mas logros.
    Parametros: list
    No retorna nada

    '''
    print(jugador_mayor_logros(
                            lista_jugadores))
#17
def imprimir_jugadores_porcentaje_tiros_triples(lista_jugadores: list):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input 
    (porcentaje de tiros triples)
    Parametros: list
    No retorna nada
    '''
    print(estadisticas_mayores_a_input(
                            lista_jugadores, "porcentaje_tiros_triples"))
#18
def imprimir_jugador_max_temporadas(lista_jugadores: list):
    '''
    Imprime los datos del jugador con mas bloqueos temporadas.
    Parametros: list
    No retorna nada
    '''
    print(mostrar_jugador_estadisticas_max(
                            lista_jugadores, "temporadas"))
#19
def imprimir_jugadores_ordenados_posicion(lista_jugadores: list):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input 
    (porcentaje tiros de campo)
    Parametro: list
    No retorna nada
    '''
    print(estadisticas_mayores_a_input(ordenar_por_posiciones(
        lista_modificada(lista_jugadores)), "porcentaje_tiros_de_campo"))
#23

##########MENU############
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
    "19. Ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje \nde tiros de campo superior a ese valor")
    print(
    "23. Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking.")
    print(
    "0. Salir.")
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
    if validar_numero(opcion) == True:
        return opcion
    else:
        return -1

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
                    imprimir_jugadores_promedio_rebotes_por_partido(copia_lista)
                    print("--------------------")
                case "11":
                    print("--------------------")
                    imprimir_jugadores_promedio_asistencias_por_partido(copia_lista)
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
                    imprimir_jugadores_y_excluir_al_menor_promedio_puntos_por_partido(copia_lista)
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
                    print("Sin terminar, proximamente.")
                    print("--------------------")
                case "0":
                    break
                case _:
                    print("--------------------")
                    print("Ingrese la opcion que desee del menú.")
                    print("--------------------")
    else:
        print("No existe la lista")