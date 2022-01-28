import datetime

square = lambda x: x**2
print(square(5)) # 25

# Opravdu anonymni funkce.
print((lambda x: x**2)(5))

# NEFUNGUJE
# Moznost vytvorit ve volani jine funkce jako parametr.
# dates = [datetime.date(year, 1, 1) for year in range(2000, 2020)]
# dates.sort(cmp=lambda x, y: cmp(x.isoweekday(), y.isoweekday()))

# Dalsi podobne pouziti.
# map(lambda d: d.isoformat(), dates)