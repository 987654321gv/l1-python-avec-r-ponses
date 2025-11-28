"""

"""
## Le module math
# 1.
import math

liste_racines = [math.sqrt(x) for x in range(1, 11)]
# 2.
print(*[math.ceil(x) for x in liste_racines])
# 3.
matrice_racines = [[math.sqrt(4 * y + x + 1) for x in range(4)] for y in range(4)]
## Probabilité et fréquence - somme de 2 dés égale à 6 - simulation
# 1.
import random

print([(random.randint(1, 6) + random.randint(1, 6)) for _ in range(100)].count(6) / 100)
# 2.
nb_lancers = int(input("nombre de lancers effectués:"))
print([(random.randint(1, 6) + random.randint(1, 6)) for _ in range(nb_lancers)].count(6) / nb_lancers)
## Le module time
import time

heure_debut = input("heure du début du TP (hh:mm) : ").split(":")
temps_debut = int(heure_debut[0]) * 60 + int(heure_debut[1])
heure_actuelle = (round(time.time()) % (24 * 60 * 60)) // 60
print(f"il s'est passé {(heure_actuelle // 60) + 1 - (temps_debut // 60)} heures et "
      f"{(heure_actuelle % 60) - (temps_debut % 60)} minutes depuis le debut du TP")
## Un premier module
import mon_module

liste = [9, 4, 7, 2, 0, 8]
print(mon_module.get_min(liste), mon_module.get_max(liste), mon_module.get_moy(liste))

