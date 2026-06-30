def numOfStrings(patterns, word):
  res = 0
  for ele in patterns:
    if(ele in word):
      res+=1
  return res