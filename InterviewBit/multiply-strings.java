// https://www.interviewbit.com/courses/programming/topics/strings/problems/multiply-strings/
// 

public class Solution {
    public String multiply(String a, String b) {
        if(a.equals("0") || b.equals("0")) return "0";

        String largest = a.length() > b.length() ? a : b;
        String smallest = a.length() <= b.length() ? a : b;

        ArrayList<ArrayList<Long>> sumLines = new ArrayList<>();
        for(int i=0; i<smallest.length(); i++) sumLines.add(new ArrayList<>());

        for (int i=smallest.length()-1; i>=0; i--) {
            long carry = 0;
            long num1 = Character.getNumericValue(smallest.charAt(i));
            ArrayList<Long> currentSumLine = sumLines.get(smallest.length()-1-i);

            long partialMult = 0;

            for (int j=largest.length()-1; j>=0; j--) {
                long num2 = Character.getNumericValue(largest.charAt(j));

                partialMult = (num1*num2) + carry;
                carry = partialMult/10;

                currentSumLine.add(partialMult%10);
            }

            if (carry > 0) currentSumLine.add(carry);
        }

        StringBuilder result = new StringBuilder();
        long carry = 0;

        for(int i = 0; i< sumLines.get(sumLines.size() - 1).size()+sumLines.size()-1; i++) {
            long columnSum = carry;

            for(int lineIndex=0; lineIndex<sumLines.size(); lineIndex++) {
                ArrayList<Long> line = sumLines.get(lineIndex);
                int indexWithinLine = i-lineIndex;

                if(indexWithinLine < 0) break;

                if(indexWithinLine < line.size()) {
                    columnSum += line.get(indexWithinLine);
                }
            }

            carry = columnSum/10;
            result.append(String.valueOf(columnSum%10));
        }

        if (carry > 0) result.append(carry);
        result = result.reverse();
        while(result.charAt(0) == '0') result.deleteCharAt(0);

        return result.toString();
    }
}

