# https://www.interviewbit.com/courses/programming/topics/backtracking/problems/sudoku/
# 

class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        self._solveSudoku(A)

    def _solveSudoku(self, A):
        cell = self._firstEmptyCell(A)

        if not cell:
            return True

        i, j = cell
        validNums = self._validNums(A, i, j)

        for num in validNums:
            self._replace(A, i, j, num)
            if self._solveSudoku(A):
                return True

        self._replace(A, i, j, ".")
        return False

    def _firstEmptyCell(self, A):
        for row in xrange(len(A)):
            for col in xrange(len(A)):
                if A[row][col] == ".":
                    return row, col

    def _validNums(self, A, row, col):
        dx, dy = row / 3, col / 3
        availableNums = set(map(str, range(1, 10)))

        # Square
        for i in xrange(3):
            for j in xrange(3):
                num = A[i + dx * 3][j + dy * 3]
                if num in availableNums:
                    availableNums.remove(num)

        # Row
        for num in A[row]:
            num = num
            if num in availableNums:
                availableNums.remove(num)

        # Column
        for i in xrange(len(A)):
            num = A[i][col]
            if num in availableNums:
                availableNums.remove(num)

        return availableNums

    def _replace(self, A, i, j, char):
        characters = bytearray(A[i])
        characters[j] = char
        A[i] = str(characters)

