# https://leetcode.com/problems/insert-interval
# 132 ms

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        if not intervals:
            return [newInterval]

        for i, current in enumerate(intervals):
            if newInterval.start < current.start:
                intervals.insert(i, newInterval)
                break
            elif i == len(intervals)-1:
                intervals.append(newInterval)
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

