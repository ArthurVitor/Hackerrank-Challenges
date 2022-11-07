     #
    ##
   ###
  ####
 #####
######

def staircase(n):
    space = n
    for c in range(1, n+1):
        print(' '*space, '#'*c)
        space -= 1


if __name__ == '__main__':
    n = 6

    staircase(n)
