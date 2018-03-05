# https://www.interviewbit.com/courses/programming/topics/arrays/problems/largest-number/
# 

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):

        def comp(n1, n2):
            a, b = str(n1), str(n2)
            return 1 if int(a+b) > int(b+a) else -1
        sortedList = sorted(A, cmp=comp, reverse=True)
        
        while len(sortedList)>1 and sortedList[0] == 0:
            del sortedList[0]
        
        return "".join(map(str, sortedList))
        
