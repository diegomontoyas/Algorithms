# https://www.interviewbit.com/courses/programming/topics/trees/problems/shortest-unique-prefix/
# 

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        counter = {}
        uniquePrefixes = [None]*len(A)
        
        n=1
        prefSize = 1
        while len(counter) < n:
            n = 0
            counter = {}

            for i, word in enumerate(A):
                if uniquePrefixes[i] is not None: continue
                n+=1
                
                pref = word[:prefSize]       
                
                if pref in counter:
                    counter[pref].append(i)
                    
                    for j in counter[pref]:
                        uniquePrefixes[j] = None
                else:
                    counter[pref] = [i]
                    uniquePrefixes[i] = pref
                    
            prefSize += 1
            
        return uniquePrefixes
            
