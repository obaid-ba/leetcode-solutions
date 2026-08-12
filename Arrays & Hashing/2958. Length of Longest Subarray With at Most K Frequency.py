def maxSubarrayLength(nums, k):
    stock = {}
    left =0
    res =0 
    for right in range(len(nums)):
        stock[nums[right]] = stock.get(nums[right], 0) + 1
        while(stock[nums[right]] > k):
            stock[nums[left]] -=1
            left +=1
        res =max(res, right-left+1)
    return res 