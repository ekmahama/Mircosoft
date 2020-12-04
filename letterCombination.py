def letterCombination(digits):

    mapping = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']
               }

    output = []

    def helper(prevComb, digits):
        if not digits:
            output.append(prevComb)
            return output
        for char in mapping[digits[0]]:
            helper(prevComb + char, digits[1:])
    if digits:
        helper('', digits)
    return output


digits = '23'
r = letterCombination(digits)
