def validate(arr):
    als = []
    sec = sorted(list(set([x[1] for x in arr])), reverse=True)
    low = sec[-1 if sec.count(sec[-1]) > 1 else -2]
    for c in arr:
        if c[1] == low:
            als.append(c[0])

    return sorted(als)


teste = validate([['beta', 37.21], ['chi', 37.21], ['cleber', 37.20], ['alpha', 41], ['teste', 39]])
# teste = validate([['beta', 20], ['chi', 50], ['alpha', 50]])
# print([x for x in teste.values()].count(50.0))
print(teste)
