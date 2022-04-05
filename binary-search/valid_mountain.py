def valid_mountain_array(arr):
    l,r = 0,len(arr)-1
    while l < len(arr) - 1 and arr[l+1] > arr[l]:
        l += 1
    while r > 1  and arr[r-1] > arr[r]:
        r -= 1
    if(l == r and l+1 != len(arr)):
        return True
    else:
        return False


if __name__ == "__main__":
    print(valid_mountain_array([9,8,7,6,5,4,3,2,1,0]))