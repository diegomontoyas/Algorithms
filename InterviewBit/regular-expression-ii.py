# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/regular-expression-ii/
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
                or pattern == ".*" \
                or (len(string) == 1 and pattern == ".") \
                or (len(string) == 0 and len(pattern) == 0):
            return True

        if len(pattern or "") == 0 or (len(string or "")==0 and "*" not in pattern):
            memo[(string, pattern)] = False
            return False

        i=0  # Indices after matching equal characters
        while i < len(string) and i < len(pattern) \
                and (pattern[i] == "." or pattern[i] == string[i]):
            i += 1

        result = False

        if i == len(string) and i == len(pattern):
            result = True
        else:
            isRepeating = False
            if i<len(pattern) and (pattern[i] == "*" or (i==0 and i+1<len(pattern) and pattern[i+1] == "*")):
                isRepeating = True
                if i>0: i -= 1

            if isRepeating:
                # Match nothing of the repetition
                if self._isMatch(string[i:], pattern[i+2:], memo):
                    result = True

                elif i<len(pattern) and (pattern[i] == "." or (i<len(string) and string[i] == pattern[i])):
                    # Match1
                    if self._isMatch(string[i+1:], pattern[i+2:], memo) \
                            or self._isMatch(string[i+1:], pattern[i:], memo):  # Keep matching
                        result = True

            elif i>0 and self._isMatch(string[i:], pattern[i:], memo):
                result = True

        memo[(string, pattern)] = result
        return result

