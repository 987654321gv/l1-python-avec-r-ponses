"""

"""
import random
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
