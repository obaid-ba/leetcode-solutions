def checkDivisibility(n):
    n= str(n)
    sum1 = 0
    sum2 = 1
    for i in range(len(n)):
        sum1+=int(n[i])
        sum2*=int(n[i])
    return int(n) % (sum1+sum2) ==0