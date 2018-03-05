# https://leetcode.com/problems/largest-number
# 58 ms

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        
        def comp(n1, n2):
            a, b = str(n1), str(n2)
            return 1 if int(a+b) > int(b+a) else -1
        sortedList = sorted(nums, cmp=comp, reverse=True)
        
        while len(sortedList)>1 and sortedList[0] == 0:
            del sortedList[0]
        
        return "".join(map(str, sortedList))

