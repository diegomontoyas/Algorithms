# https://www.interviewbit.com/courses/programming/topics/heaps-and-maps/problems/distinct-numbers-in-window/
# 

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        if B <= 0 or B > len(A): return []
        
        map = {}
        window = A[:B]
        distinct = 0
        result = []
        
        for n in window:
            if n in map:
                map[n] += 1
            else:
                distinct += 1
                map[n] = 1
                
        result.append(distinct)
                
        for i in xrange(1, len(A)-B+1):
            last = A[i-1]
            distinct = result[len(result)-1]
            
            occ = map[last]
            if occ > 1:
                map[last] -= 1
            else:
                del map[last]
                distinct-=1
               
            new =  A[i+B-1]
            if new in map:
                map[new] += 1
            else:
                map[new] = 1
                distinct += 1
        
            result.append(distinct)
            
        return result
        
            
