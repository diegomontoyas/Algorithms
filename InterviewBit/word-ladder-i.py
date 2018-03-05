# https://www.interviewbit.com/courses/programming/topics/graphs/problems/word-ladder-i/
# 

from collections import deque

class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return an integer
    def ladderLength(self, start, end, dictV):
        if start == end: return 1
        if not dictV: dictV = []
        
        graph = {}
        dictV.extend([start, end])
        
        for word in dictV:
            graph[word] = []
            
        for i, word1 in enumerate(dictV):
            for word2 in dictV[i+1:]:
                if self.oneAway(word1, word2):
                    graph[word1].append(word2)
                    graph[word2].append(word1)
        
        return self.bfsDistance(graph, start, end)
                
    def oneAway(self, w1, w2):
        distance = 0
        
        for i, c in enumerate(w1):
            if c != w2[i]:
                distance += 1
            if distance > 1:
                return False
        return True
        
    def bfsDistance(self, graph, start, end):
        visited = set()
        queue = deque([(start, 1)])

        while queue:
            current, distance = queue.popleft()
            visited.add(current)
            
            for neighbor in graph[current]:
                if neighbor == end:
                    return distance+1
                
                if neighbor not in visited:
                    queue.append((neighbor, distance+1))
                    
        return 0

