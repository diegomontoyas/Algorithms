// https://leetcode.com/problems/find-median-from-data-stream
// 494 ms

public class MedianFinder {

    class TreeNode {
        int val;
        int count = 1;
        TreeNode left, right;
        
        TreeNode(int val) {
            this.val = val;
        }
        
        void insert(int v) {
            count++;
            
            if(v < val) {
                if (left != null) left.insert(v);
                else left = new TreeNode(v);
            } else {
                if (right != null) right.insert(v);
                else right = new TreeNode(v);
            }
        }
        
        double median() {
            int rightSize = right != null ? right.count : 0;
            System.out.println(count);
            return median(count, rightSize, null);
        }
        
        private double median(final Integer treeSize, int largerNumsCount, Integer partialResult) {
            if (treeSize%2 != 0 && treeSize/2 == largerNumsCount) {
                return val;
            } else if (treeSize%2 == 0 && (treeSize/2 == largerNumsCount || treeSize/2 - 1 == largerNumsCount)){
                if (partialResult != null) return (val+partialResult)/2.0;
                else partialResult = val;
            }
            
            int smallerNumsCount = treeSize-largerNumsCount-1;
            
            if (smallerNumsCount > largerNumsCount) {
                int leftRightSize = left.right != null ? left.right.count : 0;
                return left.median(treeSize, largerNumsCount+leftRightSize+1, partialResult);
            } else {
                int rightLeftSize = right.left != null ? right.left.count : 0;
                return right.median(treeSize, largerNumsCount-rightLeftSize-1, partialResult);
            }
        }
    }
    
    TreeNode root;

    /** initialize your data structure here. */
    public MedianFinder() {}
    
    public void addNum(int num) {
        if (root == null) root = new TreeNode(num);
        else root.insert(num);
    }
    
    public double findMedian() {
        return root.median();
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
