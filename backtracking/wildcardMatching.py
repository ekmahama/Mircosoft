
def isMatch(s, p):
    p = removeDuplicateStar(p)
    return helper(s, p)


def removeDuplicateStar(p):
    if p == '':
        return p
    res = p[0]
    for c in p[1:]:
        if c != '*' or (c == '*' and res[-1] != '*'):
            res += c
    return res


def helper(s, p):
    """
    Time: O(SP)
    Space: O(SP)
    """
    m, n = len(s), len(p)
    lookup = [[False, ]*(n+1) for _ in range(m+1)]
    # If s =='' and p =='', it is a match
    lookup[0][0] = True

    # * at index zero matches an empty string as well
    if p and p[0] == '*':
        lookup[0][1] = True

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == p[j-1] or p[j-1] == '?':
                lookup[i][j] = lookup[i-1][j-1]
            # * matches 0 or more characters
            elif p[j-1] == '*':
                lookup[i][j] = lookup[i][j-1] or lookup[i-1][j]
    return lookup[m][n]


s = "aa"
p = "*"
r = isMatch(s, p)
print()

# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         m, n = len(s), len(p)
#         i, j = 0, 0
#         star, match = -1, 0
#         while i<m:
#             if j<n and (s[i]==p[j] or p[j]=='?'):
#                 i += 1
#                 j += 1
#             elif j<n and p[j]=='*':
#                 star = j
#                 match = i
#                 j += 1
#             elif star>=0:
#                 j = star+1
#                 match += 1
#                 i = match
#             else:
#                 return False
#         while j<n and p[j]=='*': j += 1
#         return j==n
