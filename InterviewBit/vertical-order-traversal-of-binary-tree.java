// https://www.interviewbit.com/courses/programming/topics/trees/problems/vertical-order-traversal-of-binary-tree/
// 

/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    
    class LinkedNode {
        LinkedNode next;
        LinkedNode prev;
        ArrayList<Integer> data = new ArrayList();
    }
    
    public ArrayList<ArrayList<Integer>> verticalOrderTraversal(TreeNode A) {
        if (A == null) return new ArrayList<>();
        
        LinkedNode head = new LinkedNode();
        
        LinkedList<TreeNode> treeNodeDeque = new LinkedList<>();
        treeNodeDeque.add(A);
        
        LinkedList<LinkedNode> linkedNodeDeque = new LinkedList<>();
        linkedNodeDeque.add(head);
        
        while (!treeNodeDeque.isEmpty()) {
            TreeNode treeNode = treeNodeDeque.pollFirst();
            LinkedNode currentResultNode = linkedNodeDeque.pollFirst();
            
            currentResultNode.data.add(treeNode.val);
        
            if (treeNode.left != null) {
                if (currentResultNode.prev == null) {
                    currentResultNode.prev = new LinkedNode();
                    head = currentResultNode.prev;
                    currentResultNode.prev.next = currentResultNode;
                }
                
                treeNodeDeque.add(treeNode.left);
                linkedNodeDeque.add(currentResultNode.prev);
            }
            
            if (treeNode.right != null) {
                if (currentResultNode.next == null) {
                    currentResultNode.next = new LinkedNode();
                    currentResultNode.next.prev = currentResultNode;
                }
                
                treeNodeDeque.add(treeNode.right);
                linkedNodeDeque.add(currentResultNode.next);
            }
        }
    
        return toArrayList(head);
    }
    
    private ArrayList<ArrayList<Integer>> toArrayList(LinkedNode head) {
        
        LinkedNode current = head;
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        
        while(current != null) {
            result.add(current.data);
            current = current.next;
        }
        
        return result;
    }
}

