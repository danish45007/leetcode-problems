"""
	Quick sort works recursively on left half and right half of the pivot and place the smaller element on the left and larger
	on the right unitil size of input if not less than of equal to 1
"""

def quick_sort(sequence):
    # base case of recursision 
    if len(sequence) <= 1:
        return sequence
    # pivot the last element of sequence
    pivot = sequence.pop()
    smaller_than_pivot = []
    greater_than_pivot = []
    for num in sequence:
        if num < pivot:
            smaller_than_pivot.append(num)
        else:
            greater_than_pivot.append(num)
    # recursive call on the left and right and concatenate pivot
    return quick_sort(smaller_than_pivot) + [pivot] + quick_sort(greater_than_pivot)



if __name__ == "__main__":
    print(quick_sort([5,3,2,1,4]))