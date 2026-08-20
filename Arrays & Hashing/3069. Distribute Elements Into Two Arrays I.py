def resultArray(nums):
    res=[nums[0]]
    arr = [nums[1]]
    for i in range(2,len(nums)):
        if(res[-1] > arr[-1]):
            res.append(nums[i])
        else:
            arr.append(nums[i])
    return res+arr