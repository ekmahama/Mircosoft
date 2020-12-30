def fact(n, memo={}):
    if n == 0 or n == 1:
        memo[n] = 2
        return memo[n]
    if n not in memo:
        memo[n] = n*fact(n-1)
    return memo[n]
