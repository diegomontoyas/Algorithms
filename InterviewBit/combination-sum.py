# https://www.interviewbit.com/problems/combination-sum/

class Solution:
    # @param nums : list of integers
    # @param S : integer
    # @return a list of list of integers
    def combinationSum(self, nums, S):
        result = []
        self.findCombinations(sorted(list(set(nums))), S, 0, [], 0, result)
        return result

    def findCombinations(self, nums, S, index, comb, currSum, result):
        if currSum == S:
            result.append(comb)
        elif currSum < S:
            for i in range(index, len(nums)):
                newSum = currSum + nums[i]
                if newSum > S: return
                self.findCombinations(nums, S, i, comb + [nums[i]], newSum, result)

