def reformatNumber(number):
  number = "".join(re.findall(r"\d", number))
  res= ""
  n =len(number)
  if( n% 3 == 1):
    last_text = number[-4:]
    number = number[:-4]
    res =  "-".join(number[i : i + 3] for i in range(0, n, 3))[:-1]
    res +=  "-".join(last_text[i : i + 2] for i in range(0, len(last_text),2))
  elif(n % 3 == 2):
    last_text = number[-2:]
    number = number[:-2]
    res =  "-".join(number[i : i + 3] for i in range(0, n, 3))
    res += last_text
  else:
    res =  "-".join(number[i : i + 3] for i in range(0, n, 3))
  return res