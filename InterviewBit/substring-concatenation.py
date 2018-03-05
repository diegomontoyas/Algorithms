# https://www.interviewbit.com/courses/programming/topics/hashing/problems/substring-concatenation/
# 

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        if not B: return []

        result = []
        wordSize = len(B[0])
        map = {}

        for word in B:
            if word in map:
                map[word] += 1
            else:
                map[word] = 1

        for displacement in xrange(wordSize):

            wordsFound = {}
            wordsFoundCount = 0

            j = displacement
            while j <= len(A) - wordSize:
                word = A[j:j + wordSize]

                invalidWord = False

                if word in map:
                    startIndex = j - wordsFoundCount * wordSize
                    firstWord = A[startIndex:startIndex + wordSize]

                    if word not in wordsFound:
                        wordsFound[word] = 1
                    elif wordsFound[word] < map[word]:
                        wordsFound[word] += 1
                    elif firstWord == word:
                        wordsFoundCount -= 1
                    else:
                        invalidWord = True

                else:
                    invalidWord = True

                if invalidWord:
                    wordsFound = {}
                    j -= wordsFoundCount * wordSize
                    wordsFoundCount = 0
                else:
                    wordsFoundCount += 1

                    if wordsFoundCount == len(B):
                        startIndex = j - (len(B) - 1) * wordSize
                        result.append(startIndex)

                        firstWord = A[startIndex:startIndex+wordSize]
                        wordsFoundCount -= 1

                        if wordsFound[firstWord] > 1:
                            wordsFound[firstWord] -= 1
                        else:
                            del wordsFound[firstWord]

                j += wordSize

        return result
            
