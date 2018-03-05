# https://www.interviewbit.com/courses/programming/topics/hashing/problems/largest-continuous-sequence-zero-sum/
# 

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        if len(A) == 0: return []

        sums = []
        for num in A:
            lastSum = sums[-1] if sums else 0
            sums.append(lastSum + num)

        map = {}
        for i, sum in enumerate(sums):
            if sum not in map:
                map[sum] = [i]
            else:
                map[sum].append(i)

        mi, mj = 0, -1

        for i, sum in reversed(list(enumerate(sums))):
            if sum == 0 and i >= mj - mi: return A[:i + 1]

            minIndex = map[sum][0]

            if minIndex < i and (i-minIndex-1 > mj - mi or (i-minIndex-1 == mj - mi and minIndex < mi)):
                mi, mj = minIndex + 1, i

        return A[mi: mj + 1]
        
