def getMax(array):
    array = sorted(array)
    for c in array[-1:]:
        print(c)


if __name__ == '__main__':
    n = int(input())
    arr = map(getMax, input().split())
    for c in arr:
        print(c)
