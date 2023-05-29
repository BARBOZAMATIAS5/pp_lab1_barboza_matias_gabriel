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

dream_team = leer_archivo(r"C:\Users\gabri\OneDrive\Documentos\UTN\Laboratorio_I\primer_parcial\pp_lab1_barboza_matias_gabriel\dt.json")

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

def guardar_archivo_csv(nombre_archivo: str, contenido: str):
    '''
    Guarda con nombre y contenido pasado por parametro en formato csv
    Parametro: contenido -> string
    Retorna un booleano
    '''

    with open (nombre_archivo, "w+") as archivo:
        archivo_csv = archivo.write(contenido)
        print(archivo_csv)

    if archivo_csv > 0:
        print("Se creó el archivo correctamente")
        return True
    else:
        print("Error al guardar el archivo.")
        return False

def sumar_estadisticas(lista_jugadores: list, clave: str):
    '''
    Operacion de sumar
    Parametro: list - str
    Retorna la suma
    '''
    suma = 0
    for jugadores in lista_jugadores:
        for claves, valores in jugadores["estadisticas"].items():
            if claves == clave:
                suma += valores
    return suma

def dividir(dividendo, divisor) -> float:
    '''
    Operacion matematica dividir
    Parametro: ambos parametros pueden ser int o float
    Retorna el resultado de la division en int o float
    '''

    if divisor > 0:
        resultado = dividendo / divisor
        return float(resultado)
    elif divisor == 0: 
        return 0

def calcular_promedio(lista_jugadores: list, clave: str):
    '''
    Calcula y muestra el promedio de lo pasado por parametro
    Parametro: list - str
    Retorna el resultado del promedio
    '''

    promedio = dividir(
        sumar_estadisticas(lista_jugadores, clave), len(lista_jugadores))
    return promedio

def calcular_jugador_max_estadisticas(lista_jugadores: list, clave: str):
    '''
    Muestra el jugador maximo 
    Parametro: list - str - str
    Retorna el jugador maximo o minimo.
    '''
    lista_aux = {}
    for jugador in lista_jugadores:
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
    lista_aux = {}
    for jugador in lista_jugadores:
        if not lista_aux:
            lista_aux = jugador
        else:
            if lista_aux["estadisticas"][clave] > jugador["estadisticas"][clave]:
                lista_aux = jugador
    return lista_aux

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
    
#7, 8, 9, 13, 14, 19
def mostrar_jugador_estadisticas_max(lista_jugadores: list, clave: str):
    '''
    Muestra el jugador maximo dependiendo de lo pasado por parametro clave
    Parametro: list - str
    Retorna los datos del jugador formateado
    '''
    texto_formateado = []
    jugador = calcular_jugador_max_estadisticas(lista_jugadores, clave)
    texto_formateado.append("Nombre: {0}\nPosicion: {1}"
                            .format(jugador["nombre"], jugador["posicion"]))
    for claves, valor in jugador["estadisticas"].items():
        texto_formateado.append("{0}: {1}".format(
                        formatear_claves(claves, valor))
    texto_formateado = "\n".join(texto_formateado)

    return texto_formateado

#10, 11, 12, 15, 18
def estadisticas_mayores_a_input(lista_jugadores: list, clave: str):
    '''
    Muestra los jugadores que esten por encima del numero ingresado por input.
    Parametro= list - str
    Retorna nombre de los jugadores.
    '''
    numero = input("Ingrese un número: ")
    nombres_jugadores = []
    if validar_numero(numero) == True:
        numero = float(numero.strip())
        for jugadores in lista_jugadores:
            if (jugadores["estadisticas"][clave] > numero
                 and numero >= 0):
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
    jugador_min = calcular_jugador_min_estadisticas(lista_jugadores, clave)
    resultado_excluir_min = (sumar_estadisticas(lista_jugadores, clave) 
                            - jugador_min["estadisticas"][clave])
    promedio = resultado_excluir_min / (len(lista_jugadores) - 1)
    texto_formateado = []
    texto_formateado.append("{0}: {1}".format(
                    formatear_claves(clave).capitalize(),promedio))
    for jugador in lista_jugadores:
        if jugador != calcular_jugador_min_estadisticas(lista_jugadores, clave):
            texto_formateado.append("Nombre: {0}\nPromedio puntos por partido: {1}"
                    .format(jugador["nombre"], jugador["estadisticas"][clave]))
    texto_formateado = "\n".join(texto_formateado)
    return texto_formateado

#17
def jugador_mayor_logros(lista_jugadores: list):
    '''
    Imprime al jugador con mayores logros
    Parametro: list
    Retorna el nombre y sus logros
    '''
    lista_aux = {}
    lista_logros = []
    for jugador in lista_jugadores:
        if not lista_aux:
            lista_aux = jugador
        else:
            if len(lista_aux["logros"]) < len(jugador["logros"]):
                lista_aux = jugador
    for logros in lista_aux["logros"]:
        lista_logros.append(logros)
    lista_logros = "\n".join(lista_logros)
    return "Nombre: {0}\n-Logros- \n{1}".format(lista_aux["nombre"], lista_logros)

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

################################ FIN AUXILIARES #################################
############################### OPCION FUNCIONES ################################
#1
def imprimir_jugadores(lista_jugadores: list):
    '''
    Imprime de la lista, todos los jugadores: nombre y posicion
    Parametros: list
    No retorna nada
    '''
    for jugador in lista_jugadores:
        print("{0} - {1}".format(jugador["nombre"], jugador["posicion"]))
        
#2
def imprimir_estadisticas_jugador_indice(lista_jugadores: list):
    '''
    Muestra los datos del jugador que el usuario desee y, ademas, lo guarda en formato csv.
    Parametro: list
    Retorna la ficha del jugador elegido.
    '''
    indice_jugador = input(
    "Ingrese un numero del 0 al 11 para mostrar la informacion del jugador: ")
    lista_formateada = []
    if (validar_numero(indice_jugador) == True and 
            re.match(r"^(?:1[0-1]|[0-9])$", indice_jugador):
        jugador = lista_jugadores[int(indice_jugador)]
        lista_formateada.append("Nombre: {0},\nPosicion: {1}".format(
                            jugador["nombre"], jugador["posicion"]))
        for claves, valor in jugador["estadisticas"].items():
            lista_formateada.append("{0}: {1}".format(formatear_claves(clave), valor))
        lista_formateada = ",\n".join(lista_formateada)
        guardar_archivo_csv("jugador_elegido.csv", lista_formateada)
    else:
        print("ERROR. No existe el jugador.")

#3    
def imprimir_nombre_jugador_logros(lista_jugadores: list):
    '''
    Busca el nombre del jugador ingresado por input y muestra sus logros.
    Parametro: list
    Retorna nombre y logros del jugador.
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

#5
def imprimir_jugador_salon_fama(lista_jugadores: list):
    '''
    Muestra si el nombre del jugador ingresado se encuentra en el salon de la fama del baloncesto
    Parametro: list
    Retorna un print afirmando o negando si pertenece al salon de la fama del baloncesto
    '''
    copia_lista = lista_jugadores[:]
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    flag = 0
    if evaluar_palabras(nombre_jugador) == True:
        for jugador in copia_lista:
            if nombre_jugador == jugador["nombre"]:
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

#6
def imprimir_jugador_max_rebotes(lista_jugadores: list):
    '''
    Imprime los datos del jugador con mas rebotes totales.
    Parametros: list
    Retorna los datos formateados del jugador max.
    '''
    return mostrar_jugador_estadisticas_max(lista_jugadores, "rebotes_totales")
#7
def imprimir_jugador_max_tiros_campo(lista_jugadores: list):
    '''
    Imprime los datos del jugador con mas porcentaje de tiros de campo.
    Parametros: list
    Retorna los datos formateados del jugador max.
    '''
    return mostrar_jugador_estadisticas_max(lista_jugadores, "porcentaje_tiros_de_campo")

#8
def imprimir_jugador_max_asistencias_totales(lista_jugadores: list):
    '''
    Imprime los datos del jugador con mas asistencias totales.
    Parametros: list
    Retorna los datos formateados del jugador max.
    '''
    return mostrar_jugador_estadisticas_max(lista_jugadores, "asistencias_totales")
#9
def imprimir_jugadores_promedio_puntos_por_partido(lista_jugadores: list):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input(promedio puntos por patido)
    Parametros: list
    Retorna los datos formateados del jugador max.
    '''
    return estadisticas_mayores_a_input(lista_jugadores, "promedio_puntos_por_partido")

#10
def imprimir_jugadores_promedio_rebotes_por_partido(lista_jugadores: list):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input (promedio rebotes por partido)
    Parametros: list
    Retorna los nombres de los jugadores
    '''
    return estadisticas_mayores_a_input(lista_jugadores, "promedio_rebotes_por_partido")
#11
def imprimir_jugadores_promedio_asistencias_por_partido(lista_jugadores: list):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input (promedio asistencias por partido)
    Parametros: list
    Retorna los nombres de los jugadores
    '''
    return estadisticas_mayores_a_input(lista_jugadores, "promedio_asistencias_por_partido")
#12
def imprimir_jugador_max_robos_totales(lista_jugadores: list):
    '''
    Imprime los datos del jugador con mas robos totales.
    Parametros: list
    Retorna los datos formateados del jugador max.
    '''
    return mostrar_jugador_estadisticas_max(lista_jugadores, "robos_totales")
#13
def imprimir_jugador_max_bloqueos_totales(lista_jugadores: list):
    '''
    Imprime los datos del jugador con mas bloqueos totales.
    Parametros: list
    Retorna los datos formateados del jugador max.
    '''
    return mostrar_jugador_estadisticas_max(lista_jugadores, "bloqueos_totales")
#14
def imprimir_jugadores_porcentaje_tiros_libres(lista_jugadores: list):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input (porcentaje de tiros libres)
    Parametros: list
    Retorna los nombres de los jugadores
    '''
    return estadisticas_mayores_a_input(lista_jugadores, "porcentaje_tiros_libres")
#15
def imprimir_jugadores_y_excluir_al_menor_promedio_puntos_por_partido(lista_jugadores: list):
    '''
    Imprime el nombre de los jugadores y su estadistica correspondiente, excluyendo al jugador con el menor numero
    Parametros: list
    Retorna los nombres de los jugadores menos el excluido
    '''
    return excluir_jugador_min(lista_jugadores, "promedio_puntos_por_partido")
#16
def imprimir_jugador_max_logros(lista_jugadores: list):
    '''
    Imprime el nombre y logros del jugador con mas logros.
    Parametros: list
    Retorna los datos formateados del jugador max.

    '''
    return jugador_mayor_logros(lista_jugadores)
#17
def imprimir_jugadores_porcentaje_tiros_triples(lista_jugadores: list):
    '''
    Imprime el nombre de jugadores mayores al numero pasado por input (porcentaje de tiros triples)
    Parametros: list
    Retorna los datos formateados del jugador max.
    '''
    return estadisticas_mayores_a_input(lista_jugadores, "porcentaje_tiros_triples")
#18
def imprimir_jugador_max_temporadas(lista_jugadores: list):
    '''
    Imprime los datos del jugador con mas bloqueos temporadas.
    Parametros: list
    Retorna los datos formateados del jugador max.
    '''
    return mostrar_jugador_estadisticas_max(lista_jugadores, "temporadas")
#19

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
    while True:
        opcion = menu_principal_dream_team()

        match opcion:
            case "1":
                print("--------------------")
                imprimir_jugadores(lista_jugadores)
                print("--------------------")
            case "2":
                print("--------------------")
                imprimir_estadisticas_jugador_indice(lista_jugadores)
                print("--------------------")
            case '3':
                print("--------------------")
                print(imprimir_nombre_jugador_logros(lista_jugadores))
                print("--------------------")
            case '4':
                print("--------------------")
                print("Sin terminar")
                print("--------------------")
            case '5':
                print("--------------------")
                print(imprimir_jugador_salon_fama(lista_jugadores))
                print("--------------------")
            case '6':
                print("--------------------")
                print(imprimir_jugador_max_rebotes(lista_jugadores))
                print("--------------------")
            case '7':
                print("--------------------")
                print(imprimir_jugador_max_tiros_campo(lista_jugadores))
                print("--------------------")
            case '8':
                print("--------------------")
                print(imprimir_jugador_max_asistencias_totales(lista_jugadores))
                print("--------------------")
            case '9':
                print("--------------------")
                print(imprimir_jugadores_promedio_puntos_por_partido(lista_jugadores))
                print("--------------------")
            case '10':
                print("--------------------")
                print(imprimir_jugadores_promedio_rebotes_por_partido(lista_jugadores))
                print("--------------------")
            case '11':
                print("--------------------")
                print(imprimir_jugadores_promedio_asistencias_por_partido(lista_jugadores))
                print("--------------------")
            case '12':
                print("--------------------")
                print(imprimir_jugador_max_robos_totales(lista_jugadores))
                print("--------------------")
            case '13':
                print("--------------------")
                print(imprimir_jugador_max_bloqueos_totales(lista_jugadores))
                print("--------------------")
            case '14':
                print("--------------------")
                print(imprimir_jugadores_porcentaje_tiros_libres(lista_jugadores))
                print("--------------------")
            case '15':
                print("--------------------")
                print(imprimir_jugadores_y_excluir_al_menor_promedio_puntos_por_partido(lista_jugadores))
                print("--------------------")
            case '16':
                print("--------------------")
                print(imprimir_jugador_max_logros(lista_jugadores))
                print("--------------------")
            case "17":
                print("--------------------")
                print(imprimir_jugadores_porcentaje_tiros_triples(lista_jugadores))
                print("--------------------")
            case "18":
                print("--------------------")
                print(imprimir_jugador_max_temporadas(lista_jugadores))
                print("--------------------")
            case "19":
                print("--------------------")
                
                print("--------------------")
            case "23":
                print("--------------------")

                print("--------------------")
            case "0":
                break
            case _:
                print("--------------------")
                print("Ingrese correctamente la opcion que desee.")
                print("--------------------")
