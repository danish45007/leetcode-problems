'''
Problem description:
Run-length encoding is a compression algorithm that allows for an integer array nums with many segments of consecutive repeated numbers to be represented by a (generally smaller) 2D array encoded. Each encoded[i] = [vali, freqi] describes the ith segment of repeated numbers in nums where vali is the value that is repeated freqi times.

For example, nums = [1,1,1,2,2,2,2,2] is represented by the run-length encoded array encoded = [[1,3],[2,5]]. Another way to read this is “three 1‘s followed by five 2‘s”.
The product of two run-length encoded arrays encoded1 and encoded2 can be calculated using the following steps:

Expand both encoded1 and encoded2 into the full arrays nums1 and nums2 respectively.
Create a new array prodNums of length nums1.length and set prodNums[i] = nums1[i] * nums2[i].
Compress prodNums into a run-length encoded array and return it.
You are given two run-length encoded arrays encoded1 and encoded2 representing full arrays nums1 and nums2 respectively. Both nums1 and nums2 have the same length. Each encoded1[i] = [vali, freqi] describes the ith segment of nums1, and each encoded2[j] = [valj, freqj] describes the jth segment of nums2.

Return the product of encoded1 and encoded2.

Note: Compression should be done such that the run-length encoded array has the minimum possible length.



Input: encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]
Output: [[6,6]]
Explanation: encoded1 expands to [1,1,1,2,2,2] and encoded2 expands to [6,6,6,3,3,3].
prodNums = [6,6,6,6,6,6], which is compressed into the run-length encoded array [[6,6]].



Input: encoded1 = [[1,3],[2,1],[3,2]], encoded2 = [[2,3],[3,3]]
Output: [[2,3],[6,1],[9,2]]
Explanation: encoded1 expands to [1,1,1,2,3,3] and encoded2 expands to [2,2,2,3,3,3].
prodNums = [2,2,2,6,9,9], which is compressed into the run-length encoded array [[2,3],[6,1],[9,2]].



'''

def solve(arr_1,arr_2):
    i,j = 0,0
    res = []
    while i < len(arr_1) and j < len(arr_2):
        num1,freq1=arr_1[i]
        num2,freq2=arr_2[j]
        product = num1*num2
        freq = min(freq1,freq2)
        if not res or product != res[-1][0]:
            res.append([product,freq])
        else:
            res[-1][1] += freq
        # subtract the prev. freq
        arr1[i][1] -= freq
        arr2[j][1] -= freq
        
        if freq1 == freq:
            i +=1
        if freq2 == freq:
            j +=1
    return res


if __name__ == "__main__":
    arr1 = [[1,3],[2,1],[3,2]]
    arr2 = [[2,3],[3,3]]
    print(solve(arr1,arr2))