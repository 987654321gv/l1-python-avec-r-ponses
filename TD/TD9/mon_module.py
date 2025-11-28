"""

"""


def get_min(liste: list[int]) -> tuple[int, int]:
    assert len(liste)
    res = (float('inf'), 0)
    for i in range(len(liste)):
        if res[0] > liste[i]:
            res = (liste[i], i)
    return res


def get_max(liste: list[int]) -> tuple[int, int]:
    assert len(liste)
    res = (float('-inf'), 0)
    for i in range(len(liste)):
        if res[0] < liste[i]:
            res = (liste[i], i)
    return res


def get_moy(liste: list[int]) -> int:
    res = 0
    for e in liste:
        res += e
    return res
