def findMissingElements(nums):
  arr = []
  min_nums = min(nums)
  max_nums = max(nums)
  for i in range(min_nums , max_nums):
    if(i not in nums):
      arr.append(i)
  return arr