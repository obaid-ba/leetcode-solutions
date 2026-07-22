def distributeCandies(candies, num_people):
  res = [0]* num_people 
  count =1
  while(candies > 0):
    for i in range(num_people):
      if(count < candies):
        res[i] += count 
        candies -=count
        count+=1
      else:
        res[i] += candies
        candies = 0
        break
  return res