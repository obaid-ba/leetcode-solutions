def capitalizeTitle(title):
    words =  title.split(" ")
    res = ""
    print(words)
    for word in words: 
        if(len(word)<=2):
            word = word.lower()
        else:
            word = word.capitalize()
        res += word 
        res += " "
    return res[:-1]