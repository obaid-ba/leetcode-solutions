def firstStableIndex(nums, k):
    res = 0
    n = len(nums)
    if n == 0:
        return -1
    for i in range(n):
        this =max(nums[0:i+1]) - min(nums[i:n])
        if(this<=k ):
            return i
    return -1