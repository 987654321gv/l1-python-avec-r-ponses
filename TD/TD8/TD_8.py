"""

"""
## Double hachage
# 1.
h_1 = lambda k: k % 13
h_2 = lambda k: 1 + (k % 12)
# 2.
h = lambda c, i: (h_1(c) + i * h_2(c)) % 13
# 3.
table: dict = {}

for c in [5, 28, 19, 15, 20, 33, 12, 17, 10]:
    i = 0
    indice = h(c, i)
    while indice in table:
        i += 1
        indice = h(c, i)

    table[indice] = c
print(table)
