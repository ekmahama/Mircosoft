"""
Given n pairs of parentheses, write a function to 
generate all combinations of well-formed parentheses.
"""


def generateParenthesis(n):
    result = []

    def backtrack(cur='', left=0, right=0):
        # when do we put our result into the output
        # if len(cur)==2*n
        if len(cur) == 2*n:
            result.append(cur)
            return
        if left < n:
            backtrack(cur+'(', left+1, right)
        if right < left:
            backtrack(cur+')', left, right+1)
    backtrack()
    return result


n = 2
res = generateParenthesis(n)
