def firstStableIndex(nums, k):
    res = 0
    n = len(nums)
    if n == 0:
        return -1
    suffix_min = [0] * n
    suffix_min[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(suffix_min[i+1] , nums[i])
    max_so_far = nums[0]
    for i in range(n):
        max_so_far = max(max_so_far , nums[i])
        if(max_so_far - suffix_min[i]<=k ):
            return i
    return -1