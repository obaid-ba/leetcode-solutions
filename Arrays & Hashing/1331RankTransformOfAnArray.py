def arrayRankTransform(arr):
  obj = {}
  res= []
  for i,ele in enumerate(sorted(set(arr))):
    obj[ele] = i+1
  for ele in arr:
    res.append(obj[ele])
  return res