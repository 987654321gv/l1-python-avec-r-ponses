"""

"""

## exercices sur les variables
# 1.
a=1+1
print(a)
# 2.
a+=1
print(a)
# 3.
a,b=5,2
print(a,b)
# 4.
a,b=b,a
print(a,b)
# 5.
print("a vaut", a, "et b vaut", b)
# 6.
a = "hello world"
print(a,type(a))

## exercices sur les types de donées
# 1.
"""
5       :int
5.0     :float
"5"     :int
-5      :int
5 / 2   :float
5 // 2  :int
5 == 2  :bool
5 = 2   : error ????????????????????
"""
# 2.
"""
(5, 2)  :tuple
[5, 2]  :list
{5, 2}  :set
"""
# 3.
x=0
print(f'le type de {x} est {type(x)}')
## exercices sur le type numérique entier
# 1.
v=1
# 2.
print(f'{v}={v // 11}x11+{v%11}')
# 3.
"""
3 * (10 / 3)    : 10.0
3 * (10 // 3)   : 9
(3 * 10) // 3   : 10
"""
# 5.
"""
3 * 10 / 3    : 10.0
3 * 10 // 3   : 10
"""
# 6.
a=1
print(a%2==0)
# 7.
print(2**256, len(str(2**256)))
# 8.
print(str(a)[-1])
print(str(a)[-2])
## exercices sur les nombres flottants
# 1.
"supérieure"
# 2.
x=0.5
x*=2**30
x=int(x)
x/=2**30
print(x)
# 3.
x=0.1
x*=2**30
x=int(x)
x/=2**30
print(x)
# 4.
"1.0"

## exercices sur les chaines de caractères
# 1.
a="hello"
b="world"
print(a+b)
print(b+a)
# 2.
print(a,b)
# 3.
"""
a*3     : hellohellohello
(a+b)*2 : helloworldhelloworld
"""
# 4.
print(a.upper())
x=1
# 5.
"non"
# 6.
"ordre alphabetico-numérique"

## exercices sur les conversions
# 1.
a='64'
"""
a*2 :6464
"""
# 2.
print(int(a)*2)
# 3.
s = input("Tape quelquechose au clavier")
# 4.
print(int(input("Tape quelquechose au clavier"))*2)
# 5.
print(f'tu auras {int(input("entre ton age:"))+20} dans 20 ans')
## Exercices supplémentaires
# 1.
"""
f               :oui mais pas recomandé
l               :oui mais pas recomandé
f2              :oui mais pas recomandé
2f              :non
totolehero      :oui mais pas recomandé
toto_le_hero    :oui
import          :non
toto2-le-retour :non
"""
# 2.
import math
print(f"la racine de votre nombre est : {math.sqrt(int(input('choisissez un nombre :')))}")
# 3.
print("a"*250)
print("b"*250+"a")
print("b"*250+"a"+"b"*100)
print("bonjour\n"*50)
# 4.
"""
3 + 4 * 6               :27
3 * 4 / 6 + 6           :8.0
2 * 3 / 12 * 8 / 4      :1.0
10 * ( 1 + 7 * 3 )      :220
20 - 2 / 6 + 3          :22.666666666666668
( 20 - 2 ) / ( 6 + 3 )  :2.0
10 + 15 % 2 + 4.3       :15.3
3 * 4 / 6 + 6           :8.0
"""
# 5.
a,b=int(input("nombre 1:")),int(input("nombre 2:"))
Somme=a+b
Quotient=a/b
print(f"La somme de {a} et {b} est {Somme} et le quotient de {a} sur {b} est {Quotient}")
"quatre variables utilisées"
"deux variables supprimable"
"0 variables supprimée au min"
a,b=int(input("nombre 1:")),int(input("nombre 2:"))
print(f"La somme de {a} et {b} est {a+b} et le quotient de {a} sur {b} est {a/b}")
# 6.
PI=math.pi
Ray=10
DM=Ray*2
PR=Ray*PI
SR=PI*Ray**2
print(f"Le cercle de rayon {Ray} a pour diamètre {DM}, pour périmètre{PR} et pour surface {SR}")
