print("===Estado Inicial===")
hp_actual = 100
hp_actual_enemigo = 50
print(f"Heroe: {hp_actual}/100")
print(f"Enemigo: {hp_actual_enemigo}/100")
def calcular_dano(ataque=25, defensa=10):
    ataque=ataque-defensa
    if ataque <0:
        ataque=0
    return ataque
ataque=calcular_dano()
def realizar_ataque(atacante, defensor, dano):
  print(f"{atacante} ataca a {defensor} por {dano}")
print(realizar_ataque("Heroe", "Enemigo", ataque))
def aplicar_dano(hp_actual_enemigo, dano):
  print(f"Enemigo {hp_actual_enemigo- dano}/{hp_actual_enemigo}")
print(aplicar_dano(hp_actual_enemigo, ataque))
