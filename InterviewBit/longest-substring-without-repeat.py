# https://www.interviewbit.com/courses/programming/topics/hashing/problems/longest-substring-without-repeat/
# 

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        
        lettersToIndices = {}
        longestLength = currentStartIndex =0
        
        for i, char in enumerate(A):
            
            if char not in lettersToIndices:
                lettersToIndices[char] = i
            else:
                longestLength = max(longestLength, i-currentStartIndex)
                endIndex = lettersToIndices[char]
                
                lettersToIndices[char] = i
                for toDel in A[currentStartIndex : endIndex]:
                    del lettersToIndices[toDel]
                
                currentStartIndex = endIndex+1
        
        longestLength = max(longestLength, len(A)-currentStartIndex)
        return longestLength
        
