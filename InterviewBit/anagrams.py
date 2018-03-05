# https://www.interviewbit.com/courses/programming/topics/hashing/problems/anagrams/
# 

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        lettersToIndices = {}
        
        for i, word in enumerate(A):
            letters = tuple(sorted(word))
            
            if letters in lettersToIndices:
                lettersToIndices[letters].append(i+1)
            else:
                lettersToIndices[letters] = [i+1]
        
        return lettersToIndices.values()
        
