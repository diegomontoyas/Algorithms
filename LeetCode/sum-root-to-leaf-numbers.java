// https://leetcode.com/problems/sum-root-to-leaf-numbers
// 2 ms

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
    
    class IntWrap {
        int val = 0;
    }
    
    public int sumNumbers(TreeNode root) {
        IntWrap count = new IntWrap();
        sumNumbers(root, new StringBuilder(), count);
        return count.val;
    }
    
    private void sumNumbers(TreeNode root, StringBuilder path, IntWrap count) {
        if (root == null) return;
        path.append(String.valueOf(root.val));
        
        if (root.left == null && root.right == null && path.length()!=0) {
            count.val += Integer.parseInt(path.toString());
        }
        
        sumNumbers(root.left, path, count);
        sumNumbers(root.right, path, count);
        path.deleteCharAt(path.length()-1);
    }
}
