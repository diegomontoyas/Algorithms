// https://www.interviewbit.com/courses/programming/topics/heaps-and-maps/problems/merge-k-sorted-lists/
// 

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode mergeKLists(ArrayList<ListNode> a) {
        ListNode head = new ListNode(-1);
        ListNode current = head;
        
        TreeMap<Integer, ArrayList<Integer>> treeMap = new TreeMap();
        
        for (int i=0; i<a.size(); i++) {
            int value = a.get(i).val;
            addDup(treeMap, value, i);
        }
        
        while (treeMap.size() != 0) {
            
            int min = treeMap.firstEntry().getKey();
            ArrayList<Integer> listIndices = treeMap.firstEntry().getValue();
            
            treeMap.remove(min);
            
            for (int listIndex: listIndices) {
                ListNode minNode = a.get(listIndex);
                a.set(listIndex, minNode.next);
                current.next = minNode;
                current = current.next;
                
               if (minNode.next != null) {
                    int value = a.get(listIndex).val;
                    addDup(treeMap, value, listIndex);
               }
            }
        }
        
        return head.next;
    }
    
    private void addDup(TreeMap<Integer, ArrayList<Integer>> treeMap, int key, int value) {
        
        if (treeMap.containsKey(key)) {
            treeMap.get(key).add(value);
        } else {
            ArrayList al = new ArrayList();
            al.add(value);
            treeMap.put(key, al);
        }
    }
}

