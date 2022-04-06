def partition_k_equal_sum_subsets(nums,k):
    _sum = sum(nums)
    _max = max(nums)
    n = len(nums)
    used = [False] * n
    target_sum = _sum // k
    if(_sum % k != 0 or _max > _sum):
        return False
    def back_track(i,k,sub_set_sum):
        if k == 0:
            return True
        if target_sum == sub_set_sum:
            return back_track(0,k-1,0)
        for j in range(i,n):
            if not used[j] or (nums[j] + sub_set_sum == target_sum):
                used[j] = True
                if(back_track(j+1,k,nums[j]+sub_set_sum)):
                    return True
                used[j] = False
        return False
            
    return back_track(0,k,0)
    


if __name__ == "__main__":
    print(partition_k_equal_sum_subsets([4,3,2,3,5,2,1],4))