# https://www.interviewbit.com/courses/programming/topics/binary-search/problems/search-for-a-range/
# 

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):

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
            
        firstOccurence = binarySearch(A, B, findFirst=True)
        if firstOccurence is None: return [-1, -1]
        
        lastOccurence = binarySearch(A, B, findFirst=False)
        return [firstOccurence, lastOccurence]
         
