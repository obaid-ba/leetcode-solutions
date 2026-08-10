def smallestPalindrome(s):
    count = Counter(s)

    first = ""
    middle = ""

    for ch in sorted(count):
        first += ch * (count[ch] // 2)

        if count[ch] % 2 == 1:
            middle = ch

    return first + middle + first[::-1]
