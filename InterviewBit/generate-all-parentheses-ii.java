// https://www.interviewbit.com/courses/programming/topics/backtracking/problems/generate-all-parentheses-ii/
// 

public class Solution {
    public ArrayList<String> generateParenthesis(int a) {
        
        ArrayList<String> result = new ArrayList<>();
        _generateParentheses(a, 0, 0, "", result);
        return result;
    }
    
    private void _generateParentheses(int n, int opened, int closed, 
                                      String current, ArrayList<String> results) {

        if (n == opened) {
            String result = current;
            for (int i=closed; i<n; i++) {
                result += ")";
            }
            
            results.add(result);
            return;
        }
        
        _generateParentheses(n, opened+1, closed, current+"(", results);
        
        if (closed < opened) {
            _generateParentheses(n, opened, closed+1, current+")", results);
        }
    }
}

