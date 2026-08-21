def balancedStringSplit(s):
    balance =0
    res=0
    for i in range(len(s)):
        if(s[i]=="L"):
            balance -=1
        else:
            balance +=1
        if(balance ==0):
            res+=1
    return res