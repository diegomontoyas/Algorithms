# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/word-break/
# 

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        dic = {}
        for word in B:
            dic[word] = 1
        
        memo = {}
        wordEndIndices = [0]
        
        for j in xrange(len(A)+1):
            for wordEndIndex in reversed(wordEndIndices):
                if A[wordEndIndex:] in memo: return True
                
                possWord = A[wordEndIndex:j]
                if possWord in dic:
                    wordEndIndices.append(j)
                    memo[A[:j]] = True
                    
                    if j==len(A):
                        return True
                    break
        return False

