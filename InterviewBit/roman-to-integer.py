# https://www.interviewbit.com/courses/programming/topics/strings/problems/roman-to-integer/
# 

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        value = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = 0
        
        for i, char in enumerate(A):
            if i > 0 and value[char] > value[A[i-1]]:
                sum += (value[char] - value[A[i-1]])
                
            elif i == len(A)-1 or value[A[i+1]] <= value[char]:
                sum += value[char]
            
        return sum
