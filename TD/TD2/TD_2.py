"""

"""
### Premiers exercices avec les structures conditionnelles
## Exercice 1
# 1.
num1 = 15
num2 = 5
if num1 % num2 == 0 or num2 % num1 == 0:
    print("Factors!")
# 2.
num1 = 15
num2 = 5
if num1 % num2 == 0 or num2 % num1 == 0:
    print("Factors!")
else:
    print("Not factors!")
## Exercice 2
state = "Georgia"
dic_messages_per_state = {"New Jersey": "School isn't cancelled.", "North Carolina": "School is postponed.",
                          "Georgia": "School is cancelled!"}
print(dic_messages_per_state.get(state, "School's status is unknown"))
## Exercice 3
list_chinese_zodiac_signs = ["monkey", "rooster", "dog", "pig", "rat", "ox", "tiger", "rabbit", "dragon", "snake",
                             "horse", "sheep"]
print(f'your chinese zodiac sign is {list_chinese_zodiac_signs[int(input("when were you born?")) % 12]}')
## Exercice 4
temperature = -3.7
celsius = True
if celsius:
    if temperature < 0:
        print("Freezing")
    else:
        print("Not freezing")
else:
    if temperature < 32:
        print("Freezing")
    else:
        print("Not freezing")
# Solution 2
if celsius and temperature < 0:
    print("Freezing")
elif temperature < 32:
    print("Freezing")
else:
    print("Not freezing")
# Solution 3
if (not celsius and temperature < 32) or temperature < 0:
    print("Freezing")
else:
    print("Not freezing")
## Exercice 5
A = 2025
if A % 400 == 0 or (A % 4 == 0 and not A % 100 == 0):
    print("bissextile!")
else:
    print("non bissextile!")
## Exercice 6
if int(input("votre nombre:")) % 5 == 0:
    print("hello")
else:
    print("bye")
## Exercice 7
n1 = int(input("premier nombre:"))
n2 = int(input("second nombre:"))
dic_operations = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y}
print(dic_operations[input("votre opération:")](n1, n2))
## Exercice 8
age = 35
sex = "F"
salaire = 700
if age >= 30:
    salaire += 100
if sex == "F":
    salaire += 50
if age < 18 or age > 40:
    print("donner l’ âge approprié")
else:
    print(f"le salaire est de {salaire}")
## Exercice 9
nbs = [int(input(f"nombre{n + 1}:")) for n in range(3)]
nbs.sort()
print(nbs[1])
## Exercice 10
nbs = [int(input(f"coté{n + 1}:")) for n in range(3)]
print(sum(nbs) > 2 * max(nbs))
### Premiers exercices avec les structures itératives
## Exercice 11
# 1.
print(*range(1, 11))
# 2.
print(*range(1, 21, 2))
# Solution 2
print(*(x for x in range(1, 21) if x % 2 == 0))
## Exercice 12
# 1.
n = int(input("conbien de nombres entrerez vous?"))
nbs = [int(input(f"nombre{i + 1}:")) for i in range(n)]
print(sum(nbs) / n)
# 2.
nbs = []
n = 0
while n != -1:
    n = int(input())
    nbs.append(n)
nbs.pop()
print(sum(nbs) / len(nbs))
## Exercice 13
n = int(input())
res = 1
for i in range(n):
    res *= i + 1
print(res)
# Solution 2
n = int(input())
res = 1
i = 1
while i < n:
    i += 1
    res *= i
print(res)
### Pour aller plus loin
## Excercice 14
sets = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],
        [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31],
        [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31],
        [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31],
        [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]]
res = 0
for s in sets:
    if input(f'votre date de naissance est elle parmi :{s} (O/N)') == 'O':
        res += s[0]
print(f'vous êtes né le {res}')
## Excercice 15
import random

n = int(input("votre nombre:"))
n_random = random.randint(0, 99)
if n == n_random:
    print("vous avez gagné 10 000€")
set_n = set(str(n))
set_n_random = set(str(n_random))
if n < 10:
    set_n.add('0')
if n_random < 10:
    set_n_random.add('0')
elif set_n == set_n_random:
    print("vous avez gagné 3 000€")
else:
    for e_set_n in set_n:
        if e_set_n in set_n_random:
            print("vous avez gagné 1 000€")
## Exercice 16
n = int(input())
assert 10 <= n <= 20
print(int(str(n)[0]) + int(str(n)[1]))
## Exercice 17
# 1.
n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
while input("que vaut abs(number1 - number2)?") != str(abs(n1 - n2)): pass
# 2.
list_i = []
for _ in range(5):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    i = 1
    while input("que vaut abs(number1 - number2)?") != str(abs(n1 - n2)): i += 1
    list_i.append(i)
print(f'vous avez pris {sum(list_i) / 5} essais en moyenne')
## Exercice 18
phrase = input()
print(phrase.count(" ") + 1)
### Pour s'entraîner
## Exercice 19
my_input = "zoophysiology"
if "ooo" in my_input:
    print("I like going to the zoo!")
elif "oo" in my_input:
    print("I like studying birds! I want to become an ornithologist!")
elif "o" in my_input:
    print("I like studying fish! I want to become an ichthyologist!")
else:
    print("I miss going to the zoo!")
## Exercice 20
team_1 = "UK"
team_2 = "France"
team_1_score = 100
team_2_score = 130
if team_1_score > team_2_score:
    print(f'{team_1} beat {team_2} by {team_1_score - team_2_score}')
elif team_1_score < team_2_score:
    print(f'{team_1} beat {team_2} by {team_1_score - team_2_score}')
else:
    print(f'{team_1} played {team_2} and it was a tie')
# Solution 2
team_1 = "UK"
team_2 = "France"
team_1_score = 100
team_2_score = 130
margin = team_1_score - team_2_score
winner = team_1 if margin > 0 else team_2
loser = team_2 if margin > 0 else team_1
if margin == 0:
    print(f'{team_1} played {team_2} and it was a tie')
else:
    print(f'{winner} beat {loser} by {abs(margin)}')
## Exercice 21
weight = int(input())
height = int(input())
pound_kg_ratio = 0.45359237
inch_meter_ratio = 0.0254
weight *= pound_kg_ratio
height *= inch_meter_ratio
IMC = weight / (height ** 2)
print(f'IMC:{IMC:.2f}')

if IMC < 18.5:
    print("Underweight")
elif IMC < 25:
    print("Normal")
elif IMC < 30:
    print("Overweight")
else:
    print("Obese")

## Exercice 22
n = 6
for i in range(n):
    print('*' * (i + 1))
## Exercice 23
n = 6
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)
## Exercice 24
n = int(input())
i = 1
while n ** i <= 1_000_000:
    i += 1
print(n ** (i - 1))
# Solution 2
import math

print(n ** math.floor(math.log(1_000_000, n)))

#### Suite (TD_3)
### Premiers exercices avec les structures itératives
## Exercice 1
import time

list_i = []
depart = time.time()
for _ in range(5):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    i = 1
    while input(f"que vaut {n1} - {n2}?") != str((n1 - n2)): i += 1
    list_i.append(i)
print(f'vous avez pris {sum(list_i) / 5} essais en moyenne')
print(f'le test a duré {int(time.time() - depart)} secondes')
## Exercice 2
list_i = []
depart = time.time()
user_want_to_continue = True
while user_want_to_continue:
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    i = 1
    while input(f"que vaut {n1} - {n2}?") != str((n1 - n2)): i += 1
    list_i.append(i)
    user_want_to_continue = input('voulez vous continuer? (Y/N)') == 'Y'
print(f'vous avez pris {sum(list_i) / len(list_i)} essais en moyenne')
print(f'le test a duré {int(time.time() - depart)} secondes')
## Exercice 3
l = [30 * x for x in range(4, 34)]
[print(*l[i:i + 10]) for i in range(0, len(l), 10)]
# Solution 2
l = [x for x in range(100, 1001) if x % 5 == 0 and x % 6 == 0]
[print(*l[i:i + 10]) for i in range(0, len(l), 10)]
## Exercice 4
user_wins = 0
computer_wins = 0
while 3 not in (user_wins, computer_wins):
    n = random.randint(0, 2)
    n2 = int(input())
    if n - n2 in [1, -2]:
        user_wins += 1
    if n - n2 in [2, -1]:
        computer_wins += 1
    print(f'{user_wins}-{computer_wins}')
## Exercice 5
# 1.
password = input()
if len(password) < 6 or len(password) > 16:
    print("not valid")
else:
    mandatory_sets = {{chr(x) for x in range(ord('a'), ord('a') + 26)},
                      {chr(x) for x in range(ord('A'), ord('A') + 26)},
                      {str(x) for x in range(10)},
                      {'$', '#', '@'}}
    if all(any(e in password for e in mandatory_set) for mandatory_set in mandatory_sets):
        print("valid")
    else:
        print("not valid")
# 2.
import re

password = input()
if len(password) < 6 or len(password) > 16:
    print("not valid")
else:
    mandatory_regexes = {'[a-z]',
                         '[A-Z]',
                         '[0-9]',
                         '[$#@]'}
    if all(re.search(mandatory_regex, password) for mandatory_regex in mandatory_regexes):
        print("valid")
    else:
        print("not valid")


## Exercice 6
def codage(mot: str, x: int):
    dic_decalage = {chr(i + ord('a')): chr(((i + x) % 26) + ord('a')) for i in range(26)}
    return ''.join(dic_decalage[c] for c in mot)


def decodage(mot: str, x: int):
    return codage(mot, 26 - x)
