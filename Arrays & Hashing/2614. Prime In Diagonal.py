def diagonalPrime( nums):
    n = len(nums)
    res = 0
    for i in range(n):
        if isPrime(nums[i][i]):
            res = max(res, nums[i][i])

        if isPrime(nums[i][n - i - 1]):
            res = max(res, nums[i][n - i - 1])
    
    return res
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True