def swap_case(s):
    s = s(str)
    mud = []
    for c in s:
        if c.isupper() == True:
            mud.append(c.lower())
        else:
            mud.append(c.upper())
    mud = ''.join(mud)
    return mud

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)