def minSetSize(arr):
  count = Counter(arr)
  values = sorted(count.values(), reverse=True)
  ans =  0
  removed = 0
  target = len(arr) / 2
  for freq in values:
    removed += freq
    ans += 1

    if removed >= target:
        return ans