# ENTREGA LUNES 29/05 18:30
import json
import csv
import re

########################### AUXILIARES #############################

def leer_archivo(path_completo: str) -> json:
    '''
    Lee el archivo .json por ruta
    Parametros: ruta en str
    Retorna la lectura del json
    '''

    with open(path_completo, "r") as archivo:
        return list[dict](json.load(archivo)["jugadores"])

def numero_int_o_float(numero: str)-> int | float:
    '''
    Convierte el numero pasado por parametro en un numero entero o flotante
    Parametro: str
    Retorna un int o float
    '''
    if "," in numero:
        return numero_int_o_float(numero.replace(",", "."))
    else:
        if "." in numero:
            return float(numero)
        else:
            return int(numero)

def validar_numero(numero: str) -> bool:
    '''
    Valida si el dato ingresado es un numero, sea int o float
    Parametro: str
    Retorna un booleando
    '''
    if type(str(numero)) is str:
        if "." in numero:
            return validar_numero(numero.replace(".", ""))
        else:
            if numero.isnumeric():
                return True
            else:
                return False

def formatear_claves(clave: str)-> str:
    '''
    Formatea las palabras de las claves de estadisticas
    Parametro: str
    Retorna la palabra formateada
    '''
    if "_" in clave:
        return clave.replace("_", " ").capitalize()
    else:
        return clave.capitalize()

def evaluar_palabras(palabra: str)-> bool:
    '''
    Evalua si la palabra u oracion ingresada son letras
    Parametro: str
    Retorna True o False
    '''
    evaluar_nombre = palabra.strip().lower().replace(" ", "")
    if evaluar_nombre.isalpha() == True:
        return True
    else:
        return False

def guardar_archivo_csv(nombre_archivo: str, contenido: str) -> bool:
    '''
    Guarda con nombre y contenido pasado por parametro en formato csv
    Parametro: contenido -> string
    Retorna un true si se guardo, false si hubo un error.
    '''

    with open(nombre_archivo, "w+") as archivo:
        archivo_csv = archivo.write(contenido)

    if archivo_csv > 0:
        print("Se creó el archivo correctamente")
        return True
    else:
        print("Error al guardar el archivo.")
        return False

def sumar_estadisticas(lista_jugadores: list, clave: str)-> float | int:
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

def calcular_jugador_max_min_estadisticas(lista_jugadores: list[dict], clave: str, auxiliar: str)-> dict:
    '''
    Muestra el jugador maximo o minimo y lo almacena 
    Parametro: list - str - str
    Retorna el jugador maximo.
    '''
    copia_lista = lista_jugadores[:]
    lista_aux = {}
    for jugador in copia_lista:
        if auxiliar == "max":
            if not lista_aux:
                lista_aux = jugador
            else:
                if lista_aux["estadisticas"][clave] < jugador["estadisticas"][clave]:
                    lista_aux = jugador
        elif auxiliar == "min":
            if not lista_aux:
                lista_aux = jugador
            else:
                if lista_aux["estadisticas"][clave] > jugador["estadisticas"][clave]:
                    lista_aux = jugador

    return lista_aux

def lista_dict_nombres(lista_jugadores: list[dict], clave: str)-> list[dict]:
    '''
    Crea una lista donde se almacenaran los nombres y la clave a eleccion.
    Parametro: list[dict] - str
    Retorna la lista.
    '''
    copia_lista = lista_jugadores[:]
    lista_nombres_puntos = []
    for jugadores in copia_lista:
        for claves in jugadores["estadisticas"]:
            if claves == clave:
                lista_nombres_puntos.append(
                    {"nombre": jugadores["nombre"],
                     clave: jugadores["estadisticas"][clave]})

    return lista_nombres_puntos

# 1
def formateo_dream_team_jugadores(lista_jugadores: list[dict])-> str:
    '''
    Muestra y formatea el nombre y la posicion de todos los jugadores
    Parametros: list
    No retorna nada
    '''
    formateo_jugadores = []
    for jugador in lista_jugadores:
        formateo_jugadores.append(
            "{0} - {1}".format(jugador["nombre"], jugador["posicion"]))
    formateo_jugadores = "\n".join(formateo_jugadores)
    return formateo_jugadores

# 2
def buscar_jugador_por_indice(lista_jugadores: list[dict]):
    '''
    Hace ingresar un numero por input, el cual es el indice que llama al jugador correspondiente.
    Parametros: list
    No retorna nada
    '''
    copia_lista = lista_jugadores
    indice_jugador = input(
        "Ingrese un numero del 0 al 11 para mostrar la informacion del jugador: ")
    lista_formateada = []
    if (validar_numero(indice_jugador) == True and
        re.match(r"^(?:1[0-1]|[0-9])$", indice_jugador)):
        jugador = copia_lista[numero_int_o_float(indice_jugador)]
        lista_formateada.append("Nombre: {0},\nPosicion: {1},".format(
            jugador["nombre"], jugador["posicion"]))

        for claves, valor in jugador["estadisticas"].items():
            lista_formateada.append("{0}: {1},".format(
                formatear_claves(claves), valor))

        lista_formateada = "\n".join(lista_formateada)

        print(lista_formateada)
        guardar_archivo_csv("jugador_elegido.csv", lista_formateada)
    else:
        print("ERROR. No existe el jugador.")

# 3
def nombre_jugador_logros(lista_jugadores: list[dict])-> str:
    '''
    Busca si el jugador ingresado por input coincide con los que se encuentran en la lista,
    si es asi, muestra el nombre y sus logros.
    Parametro: list
    Retorna un texto formateado con los datos del jugador
    '''
    copia_lista = lista_jugadores[:]
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    flag = 0
    if evaluar_palabras(nombre_jugador) == True:
        for jugador in copia_lista:
            if nombre_jugador.lower() == jugador["nombre"].lower() and flag == 0:
                jugador_elegido = ("Nombre jugador: {0}\nLogros: \n{1}".
                                   format(jugador["nombre"], "\n".join(jugador["logros"])))
                flag = 1

        if flag == 1:
            return jugador_elegido
        else:
            return "ERROR"
    else:
        return "Error, ingrese correctamente."

# 4
def ordenar_claves_o_numeros(lista_jugadores: list[dict], clave: str, auxiliar: bool)-> list[dict]:
    '''
    Ordena las claves pasadas por parametro
    Parametros: list - str
    Retorna la lista modificada.
    '''
    copia_lista = lista_jugadores[:]
    bandera_swap = True
    while bandera_swap:
        bandera_swap = False
        if auxiliar == True:
            for indice in range(len(copia_lista) - 1):
                if copia_lista[indice][clave] > copia_lista[indice+1][clave]:
                    copia_lista[indice], copia_lista[indice +1] = copia_lista[indice+1], copia_lista[indice]
                    bandera_swap = True
        else:
            for indice in range(len(copia_lista) - 1):
                if copia_lista[indice][clave] < copia_lista[indice+1][clave]:
                    copia_lista[indice], copia_lista[indice + 1] = copia_lista[indice+1], copia_lista[indice]
                    bandera_swap = True
    return copia_lista


def formateo_ordenados(lista_jugadores: list[dict], clave: str):
    '''
    Formateo de string de los nombres y sus promedios.
    Parametro: list
    No retorna nada
    '''
    copia_lista = lista_jugadores[:]
    lista = lista_dict_nombres(copia_lista, clave)
    lista = ordenar_claves_o_numeros(lista, "nombre", True)
    for jugadores in lista:
        for claves, valores in jugadores.items():
            print("{0}: {1}".format(formatear_claves(claves), valores))

# 5
def jugadores_salon_fama(lista_jugadores: list[dict])-> str:
    '''
    Busca si el nombre del jugador ingresado por input es miembro o no del 
    salon de la fama del baloncesto.
    Parametro: list
    Retorna string formateado
    '''
    copia_lista = lista_jugadores[:]
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    flag = 0
    if evaluar_palabras(nombre_jugador) == True:
        for jugador in copia_lista:
            if nombre_jugador.lower() == jugador["nombre"].lower():
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

# 7, 8, 9, 13, 14, 19
def mostrar_jugador_estadisticas_max(lista_jugadores: list[dict], clave: str)-> str:
    '''
    Muestra el jugador maximo dependiendo de lo pasado por parametro clave
    Parametro: list - str
    Retorna los datos del jugador formateado
    '''
    copia_lista = lista_jugadores[:]
    texto_formateado = []
    jugador = calcular_jugador_max_min_estadisticas(copia_lista, clave, "max")
    texto_formateado.append("Nombre: {0}\nPosicion: {1}".format(
        jugador["nombre"], jugador["posicion"]))

    for claves, valor in jugador["estadisticas"].items():
        if claves == clave:
            texto_formateado.append("{0}: {1}".format(
                formatear_claves(clave), valor))

    texto_formateado = "\n".join(texto_formateado)

    return texto_formateado

# 10, 11, 12, 15, 18
def estadisticas_mayores_a_input(lista_jugadores: list[dict], clave: str) -> str:
    '''
    Muestra los jugadores que esten por encima del numero ingresado por input.
    Parametro= list - str
    Retorna nombre de los jugadores.
    '''
    copia_lista = lista_jugadores[:]
    numero = input("Ingrese un número: ")
    nombres_jugadores = []
    if validar_numero(numero) == True:
        numero = numero_int_o_float(numero)
        for jugadores in copia_lista:
            if (jugadores["estadisticas"][clave] > numero):
                nombres_jugadores.append(
                    "Nombre: {0}".format(jugadores["nombre"]))

        if len(nombres_jugadores) > 0:
            nombres_jugadores = "\n".join(nombres_jugadores)
            return nombres_jugadores
        else:
            return "No hay jugadores por encima del valor ingresado."
    else:
        return "ERROR. Ingrese un numero."

# 16
def excluir_jugador_min(lista_jugadores: list[dict], clave: str) -> str:
    '''
    Muestra a todos los jugadores menos el menor del dato pasado por parametro
    Parametro: list - str
    No retorna nada
    '''
    copia_lista = lista_jugadores[:]
    jugador_min = calcular_jugador_max_min_estadisticas(
                                copia_lista, clave, "min")
    resultado_excluir_min = (sumar_estadisticas(copia_lista, clave)
                             - jugador_min["estadisticas"][clave])
    promedio = resultado_excluir_min / (len(copia_lista) - 1)
    texto_formateado = []
    texto_formateado.append("{0}: {1}".format(
        formatear_claves(clave).capitalize(), promedio))
    for jugador in copia_lista:
        if jugador != jugador_min:
            texto_formateado.append("Nombre: {0}\n{1}: {2}"
                                    .format(jugador["nombre"], 
                                            formatear_claves(clave),
                                            jugador["estadisticas"][clave]))

    texto_formateado.append("\nJugador excluido {0}".format(
        jugador_min["nombre"]))
    texto_formateado = "\n".join(texto_formateado)
    return texto_formateado

# 17
def jugador_mayor_logros(lista_jugadores: list[dict]) -> str:
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
    return "Nombre: {0}\n-Logros- \n{1}".format(
        lista_aux["nombre"], lista_logros)

# 20
def lista_modificada(lista_jugadores: list[dict]) -> list[dict]:
    '''
    Modifica la lista intercambiando las posiciones por numeros
    Parametros: list
    Retorna una lista modificada
    '''
    copia_lista = lista_jugadores[:]
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
            return "Error"

    return copia_lista


def ordenar_por_posiciones(lista_jugadores: list[dict]) -> list[dict]:
    '''
    Ordena a los jugadores segun los numeros y cambia los numeros por las posiciones 
    de la anterior funcion.
    Parametro: list
    Retorna la lista ordenada y modificada
    '''
    copia_lista = lista_jugadores[:]
    lista_ordenada = ordenar_claves_o_numeros(copia_lista, "posicion", True)
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

# 23
def ranking_dream_team(lista_jugadores: list[dict]) -> list[dict]:
    '''
    Crea una lista con diccionarios con los nombres de los jugadores y
    el numero de puesto dependiendo de en qué lugar se encuentran en
    puntos, rebotes, asistencias o robos. 1 al 12 (1 como mejor, 12 como
    peor)
    Parametro: list
    Retorna una lista con diccionarios de jugadores y el numero en el cual 
    se ubican en cada una de los rankings dichos anteriormente.
    '''
    copia_lista = lista_jugadores[:]
    lista_ordenada_puntos = ordenar_claves_o_numeros(lista_dict_nombres(
        copia_lista, "puntos_totales"), "puntos_totales", False)
    lista_ordenada_rebotes = ordenar_claves_o_numeros(lista_dict_nombres(
        copia_lista, "rebotes_totales"), "rebotes_totales", False)
    lista_ordenada_asistencias = ordenar_claves_o_numeros(lista_dict_nombres(
        copia_lista, "asistencias_totales"), "asistencias_totales", False)
    lista_ordenada_robos = ordenar_claves_o_numeros(lista_dict_nombres(
        copia_lista, "robos_totales"), "robos_totales", False)

    lista_ranking_jugadores = []
    for jugadores in copia_lista:
        dict_rankings = {}
        for indice in range(len(copia_lista)):
            if jugadores["nombre"] == lista_ordenada_puntos[indice]["nombre"]:
                dict_rankings["Nombre"] = lista_ordenada_puntos[indice]["nombre"]
                dict_rankings["Puntos"] = indice + 1
            if jugadores["nombre"] == lista_ordenada_rebotes[indice]["nombre"]:
                dict_rankings["Rebotes"] = indice + 1
            if jugadores["nombre"] == lista_ordenada_asistencias[indice]["nombre"]:
                dict_rankings["Asistencias"] = indice + 1
            if jugadores["nombre"] == lista_ordenada_robos[indice]["nombre"]:
                dict_rankings["Robos"] = indice + 1

        lista_ranking_jugadores.append(dict_rankings)

    return lista_ranking_jugadores

def formatear_y_guardar_ranking(lista_jugadores: list[dict]):
    '''
    La lista con diccionarios es formateado a string y guardado en un formato csv, siempre y cuando 
    la lista provenga de la funcion "ranking_dream_team"
    Parametro: list[dict]
    No retorna nada
    '''
    copia_lista = lista_jugadores[:]
    lista_ranking = ranking_dream_team(copia_lista)
    texto_formateado = []
    for jugadores in lista_ranking:
        texto_formateado.append(
            "Jugador, Puntos, Rebotes, Asistencias, Robos,")
        texto_formateado.append("{0}, {1}, {2}, {3}, {4},".format(
            jugadores["Nombre"], jugadores["Puntos"], jugadores["Rebotes"],
            jugadores["Asistencias"], jugadores["Robos"]))
    texto_formateado = "\n".join(texto_formateado)
    print(texto_formateado)
    guardar_archivo_csv("ranking_jugadores.csv", texto_formateado)

# EJERCICIOS EXTRAS
# 1
def cantidad_jugadores_por_posicion(lista_jugadores: list[dict]) -> dict[list]:
    '''
    Crea un diccionario que contiene las posiciones y dentro de ellas, listas con los nombres de los jugadores
    Parametro: lista[dict]
    Retorna un diccionario con listas
    '''
    copia_lista = lista_jugadores[:]
    lista_ordenada = ordenar_por_posiciones(lista_modificada(copia_lista))
    diccionario_posiciones = {}
    for jugador in lista_ordenada:
        if jugador["posicion"] in diccionario_posiciones:
            lista_auxiliar = []
            lista_auxiliar = diccionario_posiciones[jugador["posicion"]]
            lista_auxiliar.append(jugador["nombre"])
        else:
            lista_auxiliar = []
            lista_auxiliar.append(jugador["nombre"])
            diccionario_posiciones[jugador["posicion"]] = lista_auxiliar

    return diccionario_posiciones


def formatear_posicion_cantidad(lista_jugadores: list[dict])-> str:
    '''
    Formatea los diccionarios con listas que se encuentran en la variable
    diccionario_ordenado, mostrando así, el nombre de las posiciones y cuantos
    jugadores juegan en dichas posiciones.
    Parametro: list[dict]
    Retorna un str
    '''
    copia_lista = lista_jugadores[:]
    diccionario_ordenado = cantidad_jugadores_por_posicion(copia_lista)
    formateo_posiciones = []
    for posiciones in diccionario_ordenado:
        formateo_posiciones.append("{0}: {1}".format(
            posiciones, len(diccionario_ordenado[posiciones])))
    formateo_posiciones = "\n".join(formateo_posiciones)

    return formateo_posiciones

#2
def jugador_nombre_logro_all_star(lista_jugadores: list[dict]):
    '''
    Crea una lista con diccionarios de los jugadores con su nombre y si en
    sus logros se encuentra al menos que fueron 1 vez all star
    Parametro: list[dict]
    Retorna una lista con diccionarios de los jugadores: su nombre y las veces que fueron all star si lo son.
    '''
    copia_lista = lista_jugadores[:]
    lista_all_star = []
    for jugador in copia_lista:
        diccionario_all_star = {}
        for logro in jugador["logros"]:
            if "All-Star" in logro:
                diccionario_all_star["nombre"] = jugador["nombre"]
                diccionario_all_star["logro"] = logro
        lista_all_star.append(diccionario_all_star)
    lista_nueva = [diccionario for diccionario in lista_all_star if diccionario]
    #crea una lista donde diccionario es la variable auxiliar, hace un for en 
    #lista_all_star y si diccionario tiene algun elemento, lo agrega a la lista.
    return lista_nueva

def ordenar_all_star_descendente(lista_jugadores: list[dict])-> list[dict]:
    '''
    Ordena de forma descendente las veces que fueron all star los jugadores.
    Parametro: list[dict]
    Retorna la lista con diccionarios, ordenados de forma descendente.    
    '''
    copia_lista = lista_jugadores[:]
    lista_all_star = jugador_nombre_logro_all_star(copia_lista)
    bandera_swap = True
    while bandera_swap:
        bandera_swap = False
        for i in range(len(lista_all_star) - 1):
            if (int(lista_all_star[i]["logro"].split(" ")[0]) <
                int(lista_all_star[i+1]["logro"].split(" ")[0])):
                lista_all_star[i], lista_all_star[i+1] = lista_all_star[i+1], lista_all_star[i]
                bandera_swap = True
    
    return lista_all_star

def formatear_all_star(lista_jugadores: list[dict])-> str:
    '''
    Formatea el nombre y el logro de all star de cada jugador que haya sido al menos 1 vez all star
    Parametro: list[dict]
    Retorna en string el nombre y cuantas veces fue all star.
    '''
    copia_lista = lista_jugadores[:]
    all_star_ordenado = ordenar_all_star_descendente(copia_lista)
    formateo_all_star = []
    for jugador in all_star_ordenado:
        formateo_all_star.append("{0} ({1})".format(
                                jugador["nombre"], jugador["logro"]))
    formateo_all_star = "\n".join(formateo_all_star)

    return formateo_all_star

#3
def jugadores_max_estadisticas(lista_jugadores: list[dict]) -> str:
    '''
    Muesta los jugadores que tienen las mejores estadisticas.
    Parametro: list[dict]
    Retorna formateado en string los nombres, la estadistica que sobresalen y
    el valor de los jugadores con las mejores estadisticas.
    '''
    copia_lista = lista_jugadores[:]
    jugadores_max = []
    for jugadores in copia_lista:
        for estadistica in jugadores["estadisticas"]:
            jugador_maximo = calcular_jugador_max_min_estadisticas(
                                    copia_lista, estadistica, "max")
            jugadores_max.append("Mayor cantidad de {0}: {1} ({2})".format(
                                formatear_claves(estadistica), 
                                jugador_maximo["nombre"], 
                                jugador_maximo["estadisticas"][estadistica]))
        break
    jugadores_max = "\n".join(jugadores_max)
    return jugadores_max

#4
def lista_jugadores_promedio_ranking(lista_jugadores: list[dict]) -> list[dict]:
    '''
    Crea una lista con diccionarios donde estará el nombre del jugador y su
    promedio de la suma de su posicion en cada ranking divido por 4 (puntos,
    rebotes, asistencias, robos)
    Parametro: list[dict]
    Retorna una lista con diccionarios donde se encuentra los nombres y sus 
    promedios.
    '''
    copia_lista = lista_jugadores[:]
    ranking_jugadores = ranking_dream_team(copia_lista)
    jugadores_estadistica_suma = []
    for jugadores in ranking_jugadores:
        diccionario = {}
        suma = 0
        for claves in jugadores:
            if claves != "Nombre":
                suma = suma + jugadores[claves] / 4
                diccionario["nombre"] = jugadores["Nombre"]
                diccionario["promedio"] = suma
        jugadores_estadistica_suma.append(diccionario)

    return jugadores_estadistica_suma

def jugador_con_mejor_estadistica(lista_jugadores: list[dict]) -> dict:
    '''
    Muestra el diccionario de quien es el jugador con mejores estadisticas del
    equipo. El jugador con el promedio mas chico es el mejor debido a que en
    el ranking tiene posiciones favorables.
    Parametro: list[dict]
    Retorna un diccionario
    '''
    copia_lista = lista_jugadores[:]
    lista_promedio_ranking = lista_jugadores_promedio_ranking(copia_lista)
    jugador_aux = None
    for jugador in lista_promedio_ranking:
        if not jugador_aux:
            jugador_aux = jugador
        else:
            if jugador_aux["promedio"] > jugador["promedio"]:
                jugador_aux = jugador
    
    return ("El jugador {0} tiene las mejores estadisticas de todos,\nademas de mejores posiciones en el ranking.".
            format(jugador_aux["nombre"]))