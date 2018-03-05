// https://leetcode.com/problems/subtree-of-another-tree
// 28 ms

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if(areEqual(s, t)) {
            return true;
        } else if(s != null && t != null) {
            return isSubtree(s.left, t) || isSubtree(s.right, t);
        } else {
            return false;
        }
    }
    
    private boolean areEqual(TreeNode s, TreeNode t) {
        if(s == null && t == null) return true;
        if(s == null || t == null) return false;

        return s.val == t.val && areEqual(s.left, t.left) && areEqual(s.right, t.right);
    }
}
