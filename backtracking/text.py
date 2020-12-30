def fact(n, memo={}):
    if n == 0 or n == 1:
        memo[n] = 1
        return memo[n]
    if not n in memo:
        memo[n] = n*fact(n-1)
    return memo[n]


def fact1(n):
    DP = [1 for _ in range(n+1)]
    for i in range(1, n+1):
        DP[i] = i*DP[i-1]
    return DP[n]
