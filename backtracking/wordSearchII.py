class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def backtrack(board, i, j, word):
            if len(word) == 0:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if board[i][j] != word[0]:
                return False
            board[i][j] = '#'
            ret = False
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ret = backtrack(board, x+i, y+j, word[1:])
                if ret:
                    break
            board[i][j] = word[0]
            return ret
        result = []

        for word in words:
            found = False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if not backtrack(board, i, j, word):
                        continue
                    result.append(word)
                    found = True
                    break
                if found:
                    break
        return result


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
         ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
r = Solution().findWords(board, words)
print()
