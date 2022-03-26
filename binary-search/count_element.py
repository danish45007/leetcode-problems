def count_element(nums,target):
    
	def first_occur(start,end,nums,target):
		res = -1
		while start <= end:
			mid = start + (end - start) // 2
			if(nums[mid] == target):
				res = mid
				end = mid - 1
			if(nums[mid] < target):
				start = mid + 1
			if(nums[mid] > target):
				end = mid - 1
		return res
        
	def last_occur(start,end,nums,target):
		res = -1
		while start <= end:
			mid = (start + end) // 2
			if(nums[mid] == target):
				res = mid
				start = mid + 1
			if(nums[mid] < target):
				start = mid + 1
			if(nums[mid] > target):
				end = mid - 1
		return res
        
	s = 0
	e = len(nums)-1
	first = first_occur(s,e,nums,target)
	last = last_occur(s,e,nums,target)
	return last - first + 1

if __name__ == "__main__":
    print(count_element([1,2,3,4,4,4,4,5,6,6,7],6))