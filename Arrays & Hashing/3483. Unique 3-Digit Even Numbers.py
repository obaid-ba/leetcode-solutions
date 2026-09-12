def totalNumbers(digits):
    res = 0
    useit = set()
    n = len(digits)
    for i in range(n):
        for j in range( n):
            if( i == j ):
                continue
            for k in range(n):
                if(k == j or k == i):
                    continue
                num = int(str(digits[i]) + str(digits[j]) + str(digits[k]))
                if(num % 2 ==0 and num not in useit and len(str(num))==3):
                    res+=1
                    useit.add(int(str(digits[i]) + str(digits[j]) + str(digits[k])))
    return res