#That provided code stub reads and integer , n, from STDIN. For all non-negative integers i < n, print i².
# 0	= 0
# 1	= 1
# 2	= 4
# 3 = 9
# 4	= 16

if __name__ == '__main__':
    n = int(input())
    nums = [print(n ** 2) for n in range(0, n)]