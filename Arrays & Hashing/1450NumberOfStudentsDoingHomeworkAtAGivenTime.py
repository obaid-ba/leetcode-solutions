def busyStudent(startTime, endTime, queryTime):
  res = 0
  for i in range(len(startTime)):
    if(queryTime in range(startTime[i], endTime[i]+1)):
      res+=1
  return res