def minimumPushes(word):
  count = Counter(word)
  values = values = sorted(count.values(), reverse=True)
  res = 0
  for i in range(len(values)):
    cost = i // 8 + 1
    res+=cost
  return res
  