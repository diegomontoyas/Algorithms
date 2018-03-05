# https://www.interviewbit.com/courses/programming/topics/graphs/problems/word-ladder-ii/
# 

class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return a list of list of strings
    def findLadders(self, start, end, dictV):
        if start == end: return [[start]]
        if not dictV: dictV = []

        graph = {}
        dictV = list(set(dictV))

        for word in dictV:
            graph[word] = []

        for i, word1 in enumerate(dictV):
            for word2 in dictV[i + 1:]:
                if self.oneAway(word1, word2):
                    graph[word1].append(word2)
                    graph[word2].append(word1)

        return self.bfsPaths(graph, start, end)

    def oneAway(self, w1, w2):
        distance = 0

        for i, c in enumerate(w1):
            if c != w2[i]:
                distance += 1
            if distance > 1:
                return False
        return True

    def bfsPaths(self, graph, start, end):
        from collections import deque
        visited = set()
        queue = deque([(start, [start])])
        distance = float("inf")
        result = []

        while queue:
            current, path = queue.popleft()
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor in visited: continue
                newPath = path + [neighbor]

                if neighbor == end and len(newPath) <= distance:
                    distance = len(newPath)
                    result.append(newPath)

                elif neighbor not in visited and len(newPath) < distance:
                    queue.append((neighbor, newPath))

        return result

