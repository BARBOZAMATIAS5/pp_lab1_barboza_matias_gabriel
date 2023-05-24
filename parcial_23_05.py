#ENTREGA LUNES 29/05 18:30
import json
import csv
import re

def leer_archivo(path_completo: str):
    '''
    Leer el archivo .json por ruta
    Parametros: ruta en str
    Retorna la lectura del json
    '''

    with open(path_completo, "r") as archivo:
        return list[dict](json.load(archivo)["jugadores"])

dream_team = leer_archivo(r"C:\Users\gabri\OneDrive\Documentos\UTN\Laboratorio_I\parcial\dt.json")

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
def estadisticas_jugador(lista_heroes: list):
    '''
    
    
    
    '''