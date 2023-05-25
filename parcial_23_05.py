#ENTREGA LUNES 29/05 18:30
import json
import csv
import re

def leer_archivo(path_completo: str):
    '''
    Lee el archivo .json por ruta
    Parametros: ruta en str
    Retorna la lectura del json
    '''

    with open(path_completo, "r") as archivo:
        return list[dict](json.load(archivo)["jugadores"])

dream_team = leer_archivo(r"C:\Users\gabri\OneDrive\Documentos\UTN\Laboratorio_I\primer_parcial\pp_lab1_barboza_matias_gabriel\dt.json")

#1
def imprimir_jugadores(lista_jugadores: list):
    '''
    Imprime de la lista, todos los jugadores: nombre y posicion
    Parametros: list
    No retorna nada
    '''
    for jugadores in lista_jugadores:
        print("{0} - {1}".format(jugadores["nombre"], jugadores["posicion"]))

#2
def validar_numero(numero: str)-> bool:
    '''
    Valida si el dato ingresado es un numero, sea int o float
    Parametro: str
    Retorna un booleando
    '''
    if type(str(numero)) is str:
        valor_reemplazado = numero.replace(".","")
        if valor_reemplazado.isnumeric():
            return True
        else:
            return False
        
def estadisticas_jugador(lista_jugadores: list):
    '''
    Muestra los datos del jugador que el usuario desee.
    Parametro: list
    Retorna la ficha del jugador elegido.
    '''
    copia_lista = lista_jugadores[:]
    indice_jugador = input(
    "Ingrese un numero del 0 al 11 para mostrar la informacion del jugador: ")

    if (validar_numero(indice_jugador) == True 
        and re.match(r"^(?:1[0-1]|[0-9])$", indice_jugador)):
            
            indice_jugador = int(indice_jugador)
            print("Nombre: \t{0}".format(copia_lista[indice_jugador]["nombre"]))
            print("Posicion: \t{0}".format(copia_lista[indice_jugador]["posicion"]))
            print("-------Estadisticas-------")
            print("Temporadas: \t{0}".
                  format(copia_lista[indice_jugador]["estadisticas"]
                         ["temporadas"]))
            print("Puntos totales: {0}".
                  format(copia_lista[indice_jugador]["estadisticas"]
                         ["puntos_totales"]))
            print("Promedio puntos por partida: {0}".
                  format(copia_lista[indice_jugador]["estadisticas"]
                         ["promedio_puntos_por_partido"]))
            print("Rebotes totales: {0}".
                  format(copia_lista[indice_jugador]["estadisticas"]
                         ["rebotes_totales"]))
            print("Promedio rebotes por partido: {0}".
                  format(copia_lista[indice_jugador]["estadisticas"]
                         ["promedio_rebotes_por_partido"]))
            print("Asistencias totales: {0}".
                  format(copia_lista[indice_jugador]["estadisticas"]
                         ["asistencias_totales"]))
            print("Promedio asistencias por partido: {0}".
                  format(copia_lista[indice_jugador]["estadisticas"]
                         ["promedio_asistencias_por_partido"]))
            print("Robos totales: {0}".
                  format(copia_lista[indice_jugador]["estadisticas"]
                         ["robos_totales"]))
            print("Bloqueos totales: {0}".
                  format(copia_lista[indice_jugador]["estadisticas"]
                         ["bloqueos_totales"]))
            print("% tiros de campo: {0}".
                  format(copia_lista[indice_jugador]["estadisticas"]
                         ["porcentaje_tiros_de_campo"]))
            print("% tiros libres: {0}".
                  format(copia_lista[indice_jugador]["estadisticas"]
                         ["porcentaje_tiros_libres"]))
            print("% tiros triples: {0}".
                  format(copia_lista[indice_jugador]["estadisticas"]
                         ["porcentaje_tiros_triples"]))
            print("")
    else:
        print("ERROR. Intentelo nuevamente.")

(estadisticas_jugador(dream_team))
