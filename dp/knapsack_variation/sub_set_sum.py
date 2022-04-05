def sub_set_sum(arr,_sum):
    size = len(arr)
    # matrix initialization size*_sum
    t = [[False for j in range(_sum+1)] for i in range(size+1)]
    # base init for 0th row and 0th col
    for i in range(size+1):
        t[i][0] = True
    for j in range(1,_sum+1):
        t[0][j] = False
    for i in range(size+1):
        for j in range(_sum+1):
            if arr[i-1] <= j:
                  t[i][j] = ((t[i-1][j]) or t[i-1][j-arr[i-1]])
            else:
                 t[i][j] = (t[i-1][j])
    return t[size][_sum]

if __name__ == "__main__":
    print(sub_set_sum([1,3,4,5,6],2))