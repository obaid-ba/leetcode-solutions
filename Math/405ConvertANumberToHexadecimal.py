def toHex(num):
  if num == 0:
    return "0"
  if num < 0:
    num += 2**32
  h = "0123456789abcdef"
  res = ""
  while num > 0:
    last  =  num % 16 
    res = str(h[last]) +res 
    num //=16
  return  res 