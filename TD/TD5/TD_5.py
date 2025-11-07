"""

"""

## Débuts avec les listes
# 1.
l=[3, 5, 10]
print(l)
# 2.
l.extend([12,17])
print(l)
# 3.
l[l.index(10)]=-7
# 4.
l=[x*2 for x in l]
print(l)
# 5.
l=[l[i]+i for i in range(len(l))]
# 6.
import random
l2=[random.randint(0,99) for _ in range(10)]
print(sum(l2),max(l2))
# 7.
l_pairs=[x for x in l2 if x%2==0]
l_impairs=[x for x in l2 if x%2!=0]
# 8.
l_cartes=list(range(1,53))
# 9.
i_coupe=random.randint(1,51)
l_cartes=l_cartes[i_coupe:]+l_cartes[:i_coupe]
## Problème de Syracuse
#2.
def syracuse(n:int)->list[int]:
    return list(iter_syracuse(n))
def iter_syracuse(n:int):
    n2=n
    yield n
    while n2 != 1:
        if n2%2:
            n2=n2*3+1
        else:
            n2//=2
        yield n2

# 3.
def teste_conjecture(n_max:int)->bool:
    for i in range(1,n_max+1):
        for _ in iter_syracuse(i):pass
    return True
# 4.
def temps_vol(n:int)->int:
    i=-1
    for _ in iter_syracuse(n):i+=1
    return i
# 5.
def temps_vol_liste(n_max:int)->list[int]:
    return [temps_vol(i) for i in range(1,n_max+1)]
# 6.
tvs=temps_vol_liste(10000)
tv_max=max(tvs)
print(f"le temps de vol maximum est de {tv_max} atteint par {tvs.index(tv_max)+1}")
# 7.
def altidude(n:int)->int:
    best=0
    for n2 in iter_syracuse(n):
        if n2<n:
            return best
        if best<n2:
            best=n2
    return best
alts=[altidude(i) for i in range(1,10001)]
alt_max=max(alts)
print(f"l'altitude maximum est de {alt_max} atteint par {alts.index(alt_max)+1}")
## Carré magique
# 2.
carre_mag=[[4,14,15,1],
           [9,7,6,12],
           [5,11,10,8],
           [16,2,3,13]]
# 3.
carre_pas_mag=[[4,14,15,1],
               [9,7,6,12],
               [5,11,10,8],
               [16,2,7,13]]
# 4.
type_carre_magique=list[list[int]]
def affiche_carre(carre:type_carre_magique)->None:
    [print(*l) for l in carre]
# 5.
def teste_lignes_egales(carre:type_carre_magique)->int:
    list_sums=[sum(l) for l in carre]
    if all([s==list_sums[0] for s in list_sums[1:]]):
        return list_sums[0]
    return -1
# 6.
def teste_colones_egales(carre:type_carre_magique)->int:
    list_sums=[sum(carre[n][i] for n in range(len(carre))) for i in range(len(carre))]
    if all([s==list_sums[0] for s in list_sums[1:]]):
        return list_sums[0]
    return -1
# 7.
def teste_diagonales_egales(carre:type_carre_magique)->int:
    list_sums=[sum(carre[n][n] for n in range(len(carre))), sum(carre[n][-n-1] for n in range(len(carre)))]
    if list_sums[0]==list_sums[1]:
        return list_sums[0]
    return -1
# 8.
def est_carre_magique(carre:type_carre_magique)->bool:
    list_sums = [teste_colones_egales(carre),teste_lignes_egales(carre),teste_diagonales_egales(carre)]
    if not(-1 in list_sums) and  all([s == list_sums[0] for s in list_sums[1:]]):
        return True
    return False
# 9.
def est_normal(carre:type_carre_magique)->bool:
    list_valeurs_carre=[case for ligne in carre for case in ligne]
    return all(i in list_valeurs_carre for i in range(1,(len(carre)**2)+1))
