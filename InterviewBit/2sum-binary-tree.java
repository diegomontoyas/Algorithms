// https://www.interviewbit.com/courses/programming/topics/trees/problems/2sum-binary-tree/
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
    public int t2Sum(TreeNode A, int B) {
        if(A == null) return 0;
        
        Deque<TreeNode> leftStack = new LinkedList<>(Arrays.asList(A));
        Deque<TreeNode> rightStack = new LinkedList<>(Arrays.asList(A));
        
        int i = nextInOrder(A, Integer.MIN_VALUE, leftStack);
        int j = previousInOrder(A, -1, rightStack);
        
        while(i < j) {
            int sum = i+j;
            
            if(sum == B) {
                return 1;
            } else if(sum > B) {
                j = previousInOrder(A, j, rightStack);
            } else {
                i = nextInOrder(A, i, leftStack);
            }
        }
        
        return 0;
    }
    
    private int nextInOrder(TreeNode root, int currentVal, Deque<TreeNode> stack) {
        
        while(!stack.isEmpty()) {
            TreeNode node = stack.peekLast();

            if(node.left != null && node.left.val > currentVal) {
                stack.add(node.left);
                
            } else if (node.val > currentVal) {
                stack.pollLast();
                if (node.right != null) stack.add(node.right);
                return node.val;
            }
        }
        
        return -1;
    }
    
    private int previousInOrder(TreeNode root, int currentVal, Deque<TreeNode> stack) {
        
        while(!stack.isEmpty()) {
            TreeNode node = stack.peekLast();

            if(node.right != null && (currentVal == -1 || node.right.val < currentVal)) {
                stack.add(node.right);
                
            } else if (currentVal == -1 || node.val < currentVal) {
                stack.pollLast();
                if (node.left != null) stack.add(node.left);
                return node.val;
            }
        }
        
        return -1;
    }
}

