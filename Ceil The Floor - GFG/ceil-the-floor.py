#User function Template for python3




def getFloorAndCeil(arr, n, x):
    result = [-1,-1]
    def get_floor(N,X):
        start = 0
        end = len(N) - 1
        res = -1
        while start <= end:
            mid = start + (end-start) // 2
            if(N[mid] == X):
                return N[mid]
            if(N[mid] <= X):
                res = N[mid]
                start = mid +1
            if(N[mid] >= X):
                end = mid - 1
        return res
    def get_ceil(N,X):
        start = 0
        end = len(N) - 1
        res = -1
        while start <= end:
            mid = start + (end-start) // 2
            if(N[mid] == X):
                return N[mid]
            if(N[mid] <= X):
                start = mid +1
            if(N[mid] >= X):
                res = N[mid]
                end = mid - 1
        return res
    arr.sort()
    floor = get_floor(arr,x)
    ceil = get_ceil(arr,x)
    result[0] = floor
    result[1] = ceil
    return result
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = getFloorAndCeil(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends