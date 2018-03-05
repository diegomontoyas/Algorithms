// https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/interleaving-strings/
// 

public class Solution {
    public int isInterleave(String a, String b, String c) {
        return _isInterleave(a.trim(), b.trim(), c.trim(), 0, 0, new HashMap<>()) ? 1:0;
    }
    
    private boolean _isInterleave(String a, String b, String c, 
                                  int ia, int ib, HashMap<String, Boolean> memo) {
            
        String memoKey = ia+":"+ib;
        
        if(a.length() + b.length() != c.length()) return false;
        if(memo.containsKey(memoKey)) return memo.get(memoKey);
        
        for(int ic = ia+ib; ic < c.length(); ic++) {
            
            if(ia<a.length() && ib<b.length() 
            && a.charAt(ia) == b.charAt(ib) && c.charAt(ic) == a.charAt(ia)) {
                
                boolean result = _isInterleave(a, b, c, ia+1, ib, memo) 
                                 || _isInterleave(a, b, c, ia, ib+1, memo);
                memo.put(memoKey, result);
                return result;
                
            } else if (ia<a.length() && a.charAt(ia) == c.charAt(ic)){
                ia++;
            } else if (ib<b.length() && b.charAt(ib) == c.charAt(ic)){
                ib++;
            } else {
                memo.put(memoKey, false);
                return false;
            }
        }
        
        memo.put(memoKey, true);
        return true;
    }
}

