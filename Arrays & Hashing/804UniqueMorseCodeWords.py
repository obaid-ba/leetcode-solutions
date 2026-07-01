def uniqueMorseRepresentations(words):
  dicti = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
  arr = []
  for i in range(len(words)):
    string = ""
    for j in range(len(words[i])):
      string+=dicti[words[i][j]]
    arr.append(string)
  return len(set(arr)) 