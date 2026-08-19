def maxNumberOfFamilies( n, reservedSeats):
    reserved = defaultdict(set)
    for r, c in reservedSeats:
        if 2 <= c <= 9:  
            reserved[r].add(c)
    ans =(n-len(reserved))*2
    for r, seats in reserved.items():
        print(r, seats)
        left = not (seats & {2, 3, 4, 5})
        middle = not (seats & {4, 5, 6, 7})
        right = not (seats & {6, 7, 8, 9})
        if(left and right):
            ans +=2
        elif(left or right or middle):
            ans +=1
    return ans