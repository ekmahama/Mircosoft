
def isMatch(s, p):
    m, n = len(s), len(p)
    DP = [[False, ]*(n+1) for _ in range(m+1)]
    DP[0][0] = True

    for j in range(2, n+1):
        DP[0][j] = DP[0][j-2] and p[j-1] == '*'

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == p[i-1] or p[i-1] == '?':
                DP[i][j] = DP[i-1][j-1]
            elif p[i-1] == '*':
                if j > 1 and p[j-2] == '.' or s[i-1] == p[j-2]:
                    DP[i][j] = DP[i][j-2] or DP[i-1][j]
                else:
                    DP[i][j] = DP[i][j-2]
    return DP[-1][-1]
