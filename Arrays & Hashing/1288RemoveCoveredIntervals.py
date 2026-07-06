def removeCoveredIntervals(intervals):
  max_end = 0
  count = 0
  intervals.sort(key=lambda x: (x[0], -x[1]))
  for start, end in intervals:
    if(end > max_end):
      count +=1
      max_end = end 
  return count 
    