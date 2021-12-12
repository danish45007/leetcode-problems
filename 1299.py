def solve(arr):
	rightMax = -1
	for i in range(len(arr) - 1, -1, -1):
		newMax = max(arr[i],rightMax)
		arr[i] = rightMax
		rightMax = newMax
	return arr