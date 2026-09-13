def findEvenNumbers(digits):
    n = len(digits)
    res = set()

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            for k in range(n):
                if i == k or j == k:
                    continue

                if digits[i] == 0:
                    continue

                num = digits[i] * 100 + digits[j] * 10 + digits[k]

                if num % 2 == 0:
                    res.add(num)
    return sorted(res)