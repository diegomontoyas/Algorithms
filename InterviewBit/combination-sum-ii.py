# https://www.interviewbit.com/courses/programming/topics/backtracking/problems/combination-sum-ii/
# 

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        if len(A) == 0: return []

        A.sort()
        i = 0
        while i < len(A) and A[i] <= B:
            i += 1

        solutions = []
        self.subsets(numbers=A[:i], numsTaken=[], target=B, solutions=solutions, sumSoFar=0)
        return solutions

    def subsets(self, numbers, numsTaken, target, solutions, sumSoFar):

        for i, num in enumerate(numbers):
            if sumSoFar + num > target:
                break

            if i > 0 and numbers[i-1] == num:
                continue

            if sumSoFar + num == target:
                solutions.append(numsTaken + [num])
            else:
                self.subsets(numbers[i + 1:], numsTaken + [num], target, solutions, sumSoFar + num)
            
        
