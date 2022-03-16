#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    result,neg_arr = [],[]
    i,j = 0,0
    while j < len(A):
        if(A[j] < 0):
            neg_arr.append(A[j])
        if(j-i+1 < K):
            j +=1
        elif(j-i+1 == K):
            if(len(neg_arr) == 0):
                result.append(0)
            else:
                top_neg = neg_arr[0]
                result.append(top_neg)
                if(A[i] == top_neg):
                    neg_arr.pop(0)
            i +=1
            j +=1
    return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends