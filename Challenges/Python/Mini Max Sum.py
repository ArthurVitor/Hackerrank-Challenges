

def miniMaxSum(arr):
    val1, val2 = 0, 0
    temp = arr[::]
    temp[-1] = 0
    val1 = sum(temp)
    temp = arr[::]
    temp[0] = 0
    val2 = sum(temp)

    print(val1, val2)

if __name__ == '__main__':

    arr = [1,2,3,4,5]

    miniMaxSum(arr)
