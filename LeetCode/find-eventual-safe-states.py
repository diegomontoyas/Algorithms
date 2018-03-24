# https://leetcode.com/problems/find-eventual-safe-states/
# 352 ms

class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        memo = {}
        safeNodes = []
        
        for node in range(len(graph)):
            if not self.isThereCycle(graph, node, {}, memo):
                safeNodes.append(node)
            
        return safeNodes
    
    def isThereCycle(self, graph, startNode, visited, memo):
        
        if startNode in memo:
            return memo[startNode]
        
        if startNode in visited: 
            memo[startNode] = True
            return True
        
        visited[startNode] = True
    
        for newNode in graph[startNode]:
            if self.isThereCycle(graph, newNode, visited, memo):
                memo[startNode] = True
                return True
        
        del visited[startNode]
        memo[startNode] = False
        return False

