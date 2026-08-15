def checkZeroOnes(s):
    max_1 = 0
    max_0 = 0
    count_1 = 0
    count_0 = 0
    
    for char in s:
        if char == "1":
            count_1 += 1
            count_0 = 0
            max_1 = max(max_1, count_1)
        else: 
            count_0 += 1
            count_1 = 0
            max_0 = max(max_0, count_0)
    return max_1>max_0