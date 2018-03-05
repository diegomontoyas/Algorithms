// https://www.interviewbit.com/courses/programming/topics/trees/problems/least-common-ancestor/
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
    public int lca(TreeNode a, int val1, int val2) {
        Result res = _lca(a, val1, val2);
        if (res.foundBoth) return res.node;
        return -1;
    }
    
    class Result {
        boolean foundBoth;
        int node; 
        
        public Result(boolean a, int b){
            foundBoth = a; 
            node = b;
        }
    }

    private Result _lca(TreeNode a, int val1, int val2) {
        if (a == null) return new Result(false, -1);
        if (val1 == val2 && a.val == val1) return new Result(true, a.val);

        Result leftRes = _lca(a.left, val1, val2);
        Result rightRes = _lca(a.right, val1, val2);
    
        if ((leftRes.node != -1 && rightRes.node != -1)
        || ((leftRes.node != -1 || rightRes.node != -1) && (a.val == val1 || a.val == val2))) {
            // I am the lca
            return new Result(true, a.val);
        
        } else if (leftRes.node != -1) {
            // The left found it
            return new Result(leftRes.foundBoth, leftRes.node);
    
        } else if (rightRes.node != -1) {
            // The right found it
            return new Result(rightRes.foundBoth, rightRes.node);
    
        } else if (a.val == val1 || a.val == val2) {
            // Found just one
            return new Result(false, a.val);
            
        } else {
            // No one found it
            return new Result(false, -1);
        }
    }
}

