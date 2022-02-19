import math

def productExceptSelf(nums):
    solution = []
    temp_arr = nums
    for num in nums:
        temp_arr.remove(num)
        solution.append(math.prod(temp_arr))
        temp_arr = nums
        
  
    return solution
    
if __name__ == '__main__':
    print(productExceptSelf([1,2,3,4]))