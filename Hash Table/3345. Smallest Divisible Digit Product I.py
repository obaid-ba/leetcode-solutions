def smallestNsumber(n, t):
      res=n
      while(math.prod(int(digit) for digit in str(res))% t!=0):
        res+=1
      return res