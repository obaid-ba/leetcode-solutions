def containsPattern(arr, m, k):
    count = 1
    for i in range(m, len(arr)):
        if arr[i] == arr[i - m]:
            count += 1

            if count >= m * (k - 1): 
                return True
        else:
            count = 1
    return False