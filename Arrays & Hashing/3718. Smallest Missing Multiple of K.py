def missingMultiple(nums, k):
    target = k 
    while(target  in nums):
        target +=k
    return target 