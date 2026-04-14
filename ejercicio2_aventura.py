import random as pd
import datetime
nombres=["Link", "Zelda", "Mario", "Toad"]
nombre= pd.choice(nombres)
clases=["Caballero", "Dragon", "Guerrero", "Mago"]
clase=pd.choice(clases)
generar_hp= pd.randint(80, 120)
fecha=datetime.now()
print("===Generador de Aventuras===")
print(f"Fecha: {fecha} ")
print(f"\n===Heroes Generados===")
print(f"Heroe 1 {nombre} Clase: {clase} HP: {generar_hp}")
print(f"Heroe 2 {nombre} Clase: {clase} HP: {generar_hp}")
print(f"Heroe 3 {nombre} Clase: {clase} HP: {generar_hp}")
