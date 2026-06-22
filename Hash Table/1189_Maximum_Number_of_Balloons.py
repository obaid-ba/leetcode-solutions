def maxNumberOfBalloons(text):
  counter = {'b':0,'a':0,'l':0,'o':0,'n':0}
  target = "balloon"
  if(len(text)<7):
    return 0
  for ele in text:
    if  ele not in counter and ele not in target:
      continue
    counter[ele]+=1 
  res = 0
  while(True):
    if( counter['b'] > 0 and counter['a'] >0 and counter['l']>1  and counter['o']>1 and counter['n']>0  ):
      counter['b'] -=1
      counter['a'] -=1
      counter['l'] -=2
      counter['o'] -=2
      counter['n'] -=1
      res+=1
    else:
      return res
