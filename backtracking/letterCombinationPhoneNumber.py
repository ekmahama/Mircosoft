def letterCombinations(digits):
    """
    Time : O(3**N * 4**M), 
    N : Number of digits in the input that maps to 3 chars
    M : Number of digits in the input that matps to 4 chars
    Space:O(3**N * 4**M)
    Since we have to keep 3**N * 4**M solutions

    """

    mapping = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']
               }
    if digits:
        return backtrak('', digits, mapping, output=[])


def backtrak(comb, digits, mapping, output=[]):
    if not digits:
        output.append(comb)
        return output
    for c in mapping[digits[0]]:
        backtrak(comb+c, digits[1:], mapping, output)
    return output


digits = "2"
r = letterCombinations(digits)
