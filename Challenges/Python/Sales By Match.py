def sockMerchant(n, ar):
    cofs = []
    for c in set(ar):
        cofs.append(ar.count(c))
    return sum([i//2 for i in cofs])

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
result = sockMerchant(n, ar)