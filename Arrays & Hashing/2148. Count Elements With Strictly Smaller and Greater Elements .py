def countElements(nums):
    minimum = min(nums)
    maximum = max(nums)
    res = 0

    for num in nums:
        if minimum < num < maximum:
            res += 1

            return res