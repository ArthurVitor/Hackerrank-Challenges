lista = []

if __name__ == '__main__':
    n = int(input(''))
    for c in range(n):
        s = input('').split()
        nums = [int(x) for x in s[1:]]
        if s[0] == 'insert':
            lista.insert(nums[0], nums[1])
        elif s[0] == 'print':
            print(lista)
        elif s[0] == 'remove':
            lista.remove(nums[0])
        elif s[0] == 'sort':
            lista = sorted(lista)
        elif s[0] == 'pop':
            lista.pop()
        elif s[0] == 'reverse':
            lista = sorted(lista, reverse=True)
        elif s[0] == 'append':
            lista.append(nums[0])
