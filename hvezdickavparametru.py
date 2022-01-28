def f(first, second, *rest):
    print(first, second, rest)

f(*range(1, 6)) #1 2 (3, 4, 5)

params = {'first': 1, 'second': 2}
f(**params)

# dict(params, **{'first': 0, 'third': 3})