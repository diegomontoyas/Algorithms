// https://www.interviewbit.com/courses/programming/topics/linked-lists/problems/add-two-numbers-as-lists/
// 

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode a, ListNode b) {
        ListNode resultHead = new ListNode(0);
        ListNode resultCurrent = resultHead;
        ListNode c1 = a, c2 = b;
    
        int carry = 0;
    
        while(c1 != null || c2 != null) {
            int num1 = c1 != null ? c1.val : 0;
            int num2 = c2 != null ? c2.val : 0;
            int sum = num1 + num2 + carry;
    
            resultCurrent.next = new ListNode(sum%10);
            resultCurrent = resultCurrent.next;
            
            carry = sum >= 10 ? 1 : 0;
            
            if(c1 != null) c1 = c1.next;
            if(c2 != null) c2 = c2.next;
        }
        
        if(carry != 0) {
            resultCurrent.next = new ListNode(carry);
        }
    
        return resultHead.next;
    }
}

