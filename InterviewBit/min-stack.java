// https://www.interviewbit.com/courses/programming/topics/stacks-and-queues/problems/min-stack/
// 

class Solution {
    private class StackNode {
        final int min;
        final int val;
        
        StackNode(int val, int min) {
            this.val = val;
            this.min = min;
        }
    }
    
    private ArrayList<StackNode> stack = new ArrayList<>();
    
    public void push(int x) {
        int lastMin = stack.isEmpty() ? x : stack.get(stack.size()-1).min;
        stack.add(new StackNode(x, Math.min(lastMin, x)));
    }

    public void pop() {
        if (stack.isEmpty()) return;
        stack.remove(stack.size()-1);
    }

    public int top() {
        if (stack.isEmpty()) return -1;
        return stack.get(stack.size()-1).val;
    }

    public int getMin() {
        if (stack.isEmpty()) return -1;
        return stack.get(stack.size()-1).min;
    }
}

