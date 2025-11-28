"""ceci est un module permettant de (en partie) remplacer mypy. écrivez "@type_force()" devant la définition d'une
fonction afin de forcer ses arguments et la valeur retournée à être du type que vous avez précisé
"""


def type_force():
    def wrap1(f):
        def wrapper(*args, **kwargs):
            for i in range(len(args)):
                if f.__code__.co_varnames[i] in f.__annotations__:
                    assert isinstance(args[i], f.__annotations__[f.__code__.co_varnames[i]])
            for kwa in kwargs:
                if kwa in f.__annotations__:
                    assert isinstance(kwargs[kwa], f.__annotations__[kwa])

            res = f(*args, **kwargs)
            if "return" in f.__annotations__:
                assert isinstance(res, f.__annotations__["return"])
            return res

        return wrapper

    return wrap1
