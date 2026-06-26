def maxIceCream(costs, coins):
  costs = sorted(costs)
  sumi =0
  n=0
  for i in range(len(costs)):
    if(costs[i]+sumi<= coins):
      sumi+=costs[i]
      n +=1
    else:
      break
  return n