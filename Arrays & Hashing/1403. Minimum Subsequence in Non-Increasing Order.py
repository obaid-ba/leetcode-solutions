def minSubsequence( nums):
  nums.sort()
  arr= []
  res = 0
  target =sum(nums) //2
  while res <= target:
    res+= nums[-1]
    arr.append(nums[-1])
    nums.pop(-1)
  return arr
