# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/word-break-ii/
# 

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, A, B):
        result = []
        dic = {}
        for word in B:
            dic[word] = 1
        
        self._findSentences(A.strip(), dic, 0, "", result)
        return sorted(result)
        
    def _findSentences(self, string, dic, startIndex, sentenceSoFar, results):
        #Look through the string
        for i in xrange(startIndex, len(string)+1):
            possWord = string[startIndex:i]
            
            if possWord in dic:
                if i < len(string):
                    #We found a word, lets branch
                    self._findSentences(string, dic, i, sentenceSoFar + " " + possWord, results)
                else:
                    #We finished the sentence
                    results.append((sentenceSoFar + " " + possWord).strip())
                    
                    
