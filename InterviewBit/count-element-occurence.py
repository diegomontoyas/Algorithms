# https://www.interviewbit.com/courses/programming/topics/binary-search/problems/count-element-occurence/
# 

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        
        def binarySearch(alist, item, findFirst):
            first = 0
            last = len(alist)-1
            result = None

            while first<=last:
                midpoint = (first + last)//2
                if alist[midpoint] == item:
                    result = midpoint
                    
                    if findFirst:
                        last = midpoint-1
                    else:
                        first = midpoint+1
                else:
                    if item < alist[midpoint]:
                        last = midpoint-1
                    else:
                        first = midpoint+1
    
            return result
           
        indexA = binarySearch(A, B, findFirst=True)
        if indexA is None: return 0
        indexB = binarySearch(A, B, findFirst=False)
        if indexB is None: return 0
        
        return indexB-indexA+1

