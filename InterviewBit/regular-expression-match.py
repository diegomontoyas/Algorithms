# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/regular-expression-match/
# 

class Solution:
    # @param s : string
    # @param p : string
    # @return an integer
    def isMatch(self, s, p):
        return self._isMatch(s, p, {})
    
    def _isMatch(self, string, pattern, memo):
        if (string, pattern) in memo:
            return memo[(string, pattern)]

        if string == pattern \
                or pattern == "*" \
                or (len(string) == 1 and pattern == "?") \
                or string is None and pattern is None \
                or len(string) == 0 and len(pattern) == 0:
            return True

        if len(string) > 0 and (pattern is None or len(pattern) == 0):
            return False

        patternIndex = None
        for i, c in enumerate(pattern):
            if c != "*":
                patternIndex = i
                break

        if patternIndex is None:
            memo[(string, pattern)] = True
            return True
            
        toMatch = pattern[patternIndex]
        for strIndex, c in enumerate(string):
            if toMatch != "?" and toMatch != c:
                continue
            
            si,pi = strIndex, patternIndex
            while pi+1 < len(pattern) and si+1 < len(string) and pattern[pi+1] == string[si+1]:
                pi += 1
                si += 1

            leftMatches = self._isMatch(string[:strIndex], pattern[:patternIndex], memo)
            if not leftMatches:
                continue

            rightMatches = self._isMatch(string[si+1:], pattern[pi+1:], memo)
            if not rightMatches:
                continue

            memo[(string, pattern)] = True
            return True

        memo[(string, pattern)] = False
        return False
        
