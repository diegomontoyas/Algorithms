# https://www.interviewbit.com/courses/programming/topics/backtracking/problems/nqueens/
# 

class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        board = ["."*A for _ in xrange(A)]
        solutions = []
        self.placeQueens(board, 0, solutions)
        return solutions

    def placeQueens(self, board, row, solutions):

        def unshared_copy(inList):
            if isinstance(inList, list):
                return list(map(unshared_copy, inList))
            return inList

        for column in xrange(len(board)):

            if self.wouldBoardBePeaceful(board, (row, column)):
                # Place queen
                characters = bytearray(board[row])
                characters[column] = "Q"
                board[row] = str(characters)

                if row == len(board)-1:
                    solutions.append(unshared_copy(board))
                else:
                    self.placeQueens(board, row+1, solutions)

                # Remove queen
                characters = bytearray(board[row])
                characters[column] = "."
                board[row] = str(characters)

    def wouldBoardBePeaceful(self, board, pos):

        for i in reversed(xrange(pos[0])):
            if board[i][pos[1]] == "Q":
                return False

        def checkDiagonal(right):
            i, j = pos
            while 0 <= i < len(board) and 0 <= j < len(board):
                cell = board[i][j]

                if cell == "Q":
                    return False

                if right:
                    j += 1
                else:
                    j -= 1

                i -= 1

            return True

        if not checkDiagonal(right=True): return False
        if not checkDiagonal(right=False): return False
        return True

