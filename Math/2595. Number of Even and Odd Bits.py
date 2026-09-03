def evenOddBit(n):
    binary = bin(n)[2:][::-1]
    even = 0
    odd = 0
    for i in range(len(binary)):
        if(i % 2 ==0 and binary[i] == '1'):
            even+=1
        elif(i % 2 !=0 and binary[i] == '1'):
            odd+=1
    return [even, odd]