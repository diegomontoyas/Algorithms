// https://www.interviewbit.com/courses/programming/topics/graphs/problems/clone-graph/
// 

/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null) return null;
        
        UndirectedGraphNode start = new UndirectedGraphNode(node.label);
        
        IdentityHashMap<UndirectedGraphNode, Boolean> visited = new IdentityHashMap<>();
        IdentityHashMap<UndirectedGraphNode, UndirectedGraphNode> cloned = new IdentityHashMap<>();
        cloned.put(node, start);
        
        Deque<UndirectedGraphNode> queue = new ArrayDeque(Arrays.asList(node));
        
        while (!queue.isEmpty()) {
            UndirectedGraphNode origCurrent = queue.pollFirst();
            UndirectedGraphNode clonedCurrent = cloned.get(origCurrent);
            
            for (UndirectedGraphNode origNeighbor : origCurrent.neighbors) {
                if (visited.containsKey(origNeighbor)) continue;
                
                UndirectedGraphNode neighborCopy = cloned.get(origNeighbor);
                
                if (neighborCopy == null) {
                    neighborCopy = new UndirectedGraphNode(origNeighbor.label);
                    cloned.put(origNeighbor, neighborCopy);
                    queue.add(origNeighbor);
                }
                
                clonedCurrent.neighbors.add(neighborCopy);
                
                if (origCurrent != origNeighbor) {
                    neighborCopy.neighbors.add(clonedCurrent);
                }
            }
            
            visited.put(origCurrent, true);
        }
        
        return start;
    }
}

