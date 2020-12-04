def longestPalind(s):
    longest, right, left = 0, -1, 0

    # check for both odd and even centers
    for j in range(2):
        for i in range(len(s)):
            length, l, r = getLongestIndex(s, i, i+j)
            if length > longest:
                longest = length
                left, right = l, r

    return s[left:right+1]


def getLongestIndex(s, l, r):
    # Termination conidtion
    # 1. Index out of bounds
    # 2. substring no longer palindrome

    while l >= 0 and r < len(s) and s[l] == s[r]:
        l, r = l-1, r+1
    l, r = l+1, r-1
    # return length and end index of palindrome found so far
    return (r-l+1, l, r)


s = 'aba'
r = longestPalind(s)
