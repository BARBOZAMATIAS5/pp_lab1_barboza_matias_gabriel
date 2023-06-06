from funciones_parcial import leer_archivo
from menu_opciones import dream_team_app

dream_team = leer_archivo(r"primer_parcial\pp_lab1_barboza_matias_gabriel\dt.json")
dream_team_app(dream_team)