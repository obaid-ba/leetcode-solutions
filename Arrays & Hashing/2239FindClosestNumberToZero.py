def findClosestNumber(nums):
  return max((-abs(x), x) for x in nums)