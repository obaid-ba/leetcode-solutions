def convertTime(current, correct):
    hour_1 = int(current[0:2]) * 60  + int(current[3:5])
    hour_2 = int(correct[0:2]) * 60 + int(correct[3:5])
    between  = hour_2 - hour_1 
    count = 0
    for i in [60, 15, 5, 1]:
        count += between // i
        between -= (between // i) * i
    return count 