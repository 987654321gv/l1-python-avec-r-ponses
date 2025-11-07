"""

"""



def intput(prompt:str="")->int:return int(input(prompt))
def lintput(prompt:str="")->list[int]:return list(map(input(prompt).split(),int))
## Revoir les notions vues en cours
# 1.
m:int=intput("nombre de lignes:")
_n:int=intput("nombre de colones")
matrice:list[list[int]]=[lintput(f"ligne n°{i+1}:") for i in range(m)]
i:int=intput("premiere ligne à échanger:")
j:int=intput("deuxième ligne à échanger:")
matrice[i],matrice[j]=matrice[j],matrice[i]
[print(*l) for l in matrice]
# 2.
n:int=intput()

matrice=[[2 if y+x+1>n else (1 if y+x+1==n else 0) for y in range(n)]for x in range(n)]
[print(*l) for l in matrice]
# 3.
entree=input()
print(entree[2])
print(entree[1:])
print(entree[::-2])
print(entree[:-2])
# 4.
entree=input()
print("".join(entree[i] for i in range(len(entree)) if i%3))
# 5.
entree=lintput()
print(len(set(entree)))
# 6.
entree1=lintput()
entree2=lintput()
print(len(set(entree1)&set(entree2)))
# 7.
nb_regions=intput("nombre de régions:")
res=[input().split() for _ in range(nb_regions)]
res_tuples=[(" ".join(x[:-1]),int(x[-1])) for x in res]
dict_res={}
for nom,score in res_tuples:
    dict_res[nom]=dict_res.get(nom,0)+score
print(dict_res)
## Ecrire un programme plus complexe
# 1.
def getfrequence(texte)->dict[str,int]:
    dict_res={}
    for l in texte:
        dict_res[l] = dict_res.get(l, 0) + 1
    return dict_res
# 2.
entree=input().split()
dict_res={}
list_res=[]
for l in entree:
    dict_res[l] = dict_res.get(l, 0) + 1
    list_res.append(dict_res[l]-1)
print(*list_res)
[print(f"{l} : {dict_res[l]}") for l in dict_res]
