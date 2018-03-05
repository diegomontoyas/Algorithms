# https://www.interviewbit.com/courses/programming/topics/strings/problems/palindrome-string/
# 

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        lower = 0 
        upper = len(A)-1
        
        while lower <= upper:
            if A[lower] == " " or not A[lower].isalnum():
                lower +=1
            elif A[upper] == " " or not A[upper].isalnum():
                upper -=1
            elif A[lower].lower() != A[upper].lower():
                return False
            else:
                lower += 1
                upper -= 1
                
        return True
        
