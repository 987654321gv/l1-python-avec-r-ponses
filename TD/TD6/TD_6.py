"""

"""

## Revoir les notions vues en cours
# 1.
def inverser(l:list)->list:return l[::-1]
# 2.
(lambda m:print(list(range(0,10*m+1,m))))(int(input()))
# 3.
def uniques(l:list)->list:return list(set(l))
# 4.
def compter_negatives(nombres:list[int])->int:
    i=0
    for n in nombres:
        if n<0:
            i+=1
    return i
# 5.
def mot_commun(mot1:str,mot2:str)->list[str]:return list(set(mot1.split())&set(mot2.split()))
## Ecrire un programme plus complexe
# 1.
import random
ok=True
while ok:
    liste_lettres_possibles=['A']*9+['E', 'I', 'N', 'O', 'R', 'S', 'T']*6
    tirage=[]
    for _ in range(7):
        i=random.randint(0,len(liste_lettres_possibles)-1)
        tirage.append(liste_lettres_possibles[i])
        del tirage[i]
    ok=tirage.count('A')+tirage.count('E')+tirage.count('I')+tirage.count('O')<2
