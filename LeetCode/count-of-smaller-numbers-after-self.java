// https://leetcode.com/problems/count-of-smaller-numbers-after-self
// 16 ms

public class Solution {
    
    class Counter {
        int count = 0;
    }
    
    class TreeNode {
        int val;
        int count = 1;
        TreeNode left, right;
        
        TreeNode(int val) {
            this.val = val;
        }
        
        int insert(int v) {
            Counter c = new Counter();
            insert(v, c);
            return c.count;
        }

        private void insert(int v, Counter counter) {
            count++;
            
            if(v <= val) {
                if (left != null) left.insert(v, counter);
                else left = new TreeNode(v);
            } else {
                counter.count += (left != null ? left.count+1 : 1);
                
                if (right != null) right.insert(v, counter);
                else right = new TreeNode(v);
            }
        }
    }
    
    public List<Integer> countSmaller(int[] nums) {
        LinkedList<Integer> result = new LinkedList<>();
        
        if (nums.length == 0) return result;
        
        TreeNode tree = new TreeNode(nums[nums.length-1]);
        result.add(0);
        
        for(int i=nums.length-2; i>=0; i--) {
            result.addFirst(tree.insert(nums[i]));
        }
        
        return result;
    }
}
