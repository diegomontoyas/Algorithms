# https://www.interviewbit.com/courses/programming/topics/backtracking/problems/palindrome-partitioning/
# 

class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        string = A
        result = set([string]) if self.isPalindrome(string) else set()

        if len(string) == 1:
            return [string]

        for i in xrange(1, len(string)):
            part1, part2 = string[:i], string[i:]

            if self.isPalindrome(part1):
                if self.isPalindrome(part2):
                    result.add((part1, part2))

                for partitions in self.partition(string[i:]):
                    new = [part1]
                    new.extend(partitions)
                    result.add(tuple(new))

        return sorted([list(x) if isinstance(x, tuple) else [x] for x in result], cmp=self.cmp)
    
    def cmp(self, list1, list2):
        i = 0
        while i < len(list1) and i < len(list2):
            if len(list1[i]) < len(list2[i]):
                return -1
            elif len(list1[i]) > len(list2[i]):
                return 1
            else:
                i += 1
            
        return 1 if len(list1) > len(list2) else -1
    
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        return list(A) == list(reversed(A))
        
