
def productExceptSelf(nums):
    output = [-1]*len(nums)
    product = 1
    right_product = 1
    # getting the left side product
    output[0] = product
    for i in range(1,len(nums)):
        product *= nums[i-1]
        output[i] = product
    
    for i in range(len(nums)-1,-1,-1):
        output[i] *= right_product
        right_product *= nums[i]
    return output
        
    
if __name__ == '__main__':
    print(productExceptSelf([4,3,2,1]))