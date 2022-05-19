#The included code stub will read an integer, n, from STDIN
#Without using any string methods, try to print the following:
#123...n
#Example:
#n = 5
#12345

if __name__ == '__main__':
    n = int(input().strip())
    nums = [print(f'{n}', end='') for n in range(1, n+1)]
