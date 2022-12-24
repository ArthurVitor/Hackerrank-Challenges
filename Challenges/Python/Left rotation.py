##################################### Solution using nested for loops ###################################
# res = []
# x = 1
# y = 1
# z = 1
# n = 2
#
# for X in range(0, x+1):
#     for Y in range(0, y+1):
#         for Z in range(0, z+1):
#             res.append([X, Y, Z])
#
# rer = []
# for i in res:
#     if sum(i) != n:
#         rer.append(i)

################################# Solution using list comprehensions ###################################
x = 1
y = 1
z = 1
n = 2

perms = [[X, Y, Z] for X in range(0, x+1) for Y in range(0, y+1) for Z in range(0, z+1)]
res = [arr for arr in perms if sum(arr) != n]
print(res)