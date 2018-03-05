// https://leetcode.com/problems/insert-delete-getrandom-o1
// 154 ms

import java.util.concurrent.ThreadLocalRandom;

public class RandomizedSet {

    private HashMap<Integer, Integer> numsToIndices = new HashMap<>();
    private ArrayList<Integer> nums = new ArrayList<>();

    /** Initialize your data structure here. */
    public RandomizedSet() {}
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if (numsToIndices.containsKey(val)) return false;
        
        nums.add(val);
        numsToIndices.put(val, nums.size()-1);
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if (!numsToIndices.containsKey(val)) return false;

        int index = numsToIndices.remove(val);
        int toMove = nums.remove(nums.size()-1);
        
        if (toMove != val) {
            nums.set(index, toMove);
            numsToIndices.put(toMove, index);
        }

        return true;
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
        return nums.get(ThreadLocalRandom.current().nextInt(0, nums.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
