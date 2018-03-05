# https://www.interviewbit.com/courses/programming/topics/strings/problems/longest-palindromic-substring/
# 

class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        longest = A[0] if A else ""
    
        # Displacement
        for i in xrange(len(A)):
            for j in xrange(i, min(i+1, len(A)-1)+1):
                if i!=j:
                    if A[i] != A[j]:
                        continue
                    elif 2>len(longest):
                        longest = A[i:j+1]
    
                for d in xrange(1, min(i+1, len(A)-j)):  # Displacement
                    substring = A[i-d:j+d+1]
                    if substring[0]==substring[-1]:
                        if len(substring) > len(longest):
                            longest = substring
                    else:
                        break
    
        return longest
        
