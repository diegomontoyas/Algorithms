// https://www.interviewbit.com/courses/programming/topics/trees/problems/min-depth-of-binary-tree/
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
    
    class IntWrap { 
        int val = Integer.MAX_VALUE;
    }
    
    public int minDepth(TreeNode a) {
        if (a == null) return 0;
        
        IntWrap response = new IntWrap();
        minDepth(a, 1, response);
        return response.val;
    }
    
    private void minDepth(TreeNode root, int depth, IntWrap minDepth) {
        if (root == null) return;
        
        if (root.left == null && root.right == null) {
            minDepth.val = Math.min(minDepth.val, depth);
        }
        
        minDepth(root.left, depth+1, minDepth);
        minDepth(root.right, depth+1, minDepth);
    }
}

