def reorderSpaces(text):
    count_spa = text.count(" ")
    words = text.split()
    res= ""
    if len(words) == 1:
        return words[0] + (" " * count_spa)
    space = count_spa /(len(words)-1)
    for i in range(len(words)-1):

        res+=  words[i] + (" " * space)
        count_spa -= space
    return res+words[-1] + " "* count_spa 