# https://www.interviewbit.com/courses/programming/topics/arrays/problems/merge-overlapping-intervals/
# 

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def overlap(a, b):
    return not ( b.start > a.end or b.end < a.start )
    
def mergeTwo(a, b):
    return Interval(min(a.start, b.start), max(a.end, b.end))

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals = sorted(intervals, key = lambda x: x.start)

        i=0
        while i < len(intervals):
            if i+1 < len(intervals) and overlap(intervals[i], intervals[i+1]):
                foundOverlap = True
                merged = mergeTwo(intervals[i], intervals[i+1])
                intervals[i] = merged
                del intervals[i+1]
            else:
                i+=1

        return intervals
                
