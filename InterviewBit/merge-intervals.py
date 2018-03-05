# https://www.interviewbit.com/courses/programming/topics/arrays/problems/merge-intervals/
# 

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):

        if not intervals:
            return [new_interval]

        for i, current in enumerate(intervals):
            if new_interval.start < current.start:
                intervals.insert(i, new_interval)
                break
            elif i == len(intervals)-1:
                intervals.append(new_interval)
                break
            
        return self.merge(intervals)
    
    def overlap(self, a, b):
        return not ( b.start > a.end or b.end < a.start )
    
    def mergeTwo(self, a, b):
        return Interval(min(a.start, b.start), max(a.end, b.end))
        
    def merge(self, intervals):
        i=0
        while i < len(intervals):
            if i+1 < len(intervals) and self.overlap(intervals[i], intervals[i+1]):
                intervals[i] = self.mergeTwo(intervals[i], intervals[i+1])
                del intervals[i+1]
            else:
                i+=1

        return intervals
        
            
