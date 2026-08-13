def makeEqual(words):
    n = len(words)
    count = {}
    for i in range(len(words)):
        for j in range(len(words[i])):
            if(words[i][j] not in count ):
                count[words[i][j]] =1
            else:
                count[words[i][j]] += 1
    for c in count.values():
        if c % n != 0:
            return False
    return True