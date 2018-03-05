// https://www.interviewbit.com/courses/programming/topics/heaps-and-maps/problems/magician-and-chocolates/
// 

import java.math.BigInteger;

public class Solution {
    public int nchoc(int A, ArrayList<Integer> B) {

        BigInteger chocolatesEaten = BigInteger.ZERO;

        TreeMap<Integer, Integer> treeMap = new TreeMap<>();

        for (int i=0; i<B.size(); i++) {
            int value = B.get(i);
            if (treeMap.containsKey(value)) {
                treeMap.put(value, treeMap.get(value)+1);
            } else {
                treeMap.put(value, 1);
            }
        }

        for (int t=0; t<A; t++) {

            int largestBagSize = treeMap.lastKey();
            int numberOfBags = treeMap.get(largestBagSize);

            if (numberOfBags > 1) {
                treeMap.put(largestBagSize, numberOfBags-1);
            } else {
                treeMap.remove(largestBagSize);
            }

            if (largestBagSize == 0) {
                break;
            }

            chocolatesEaten = chocolatesEaten.add(BigInteger.valueOf(largestBagSize));

            int newSize = largestBagSize/2;

            if (treeMap.containsKey(newSize)) {
                treeMap.put(newSize, treeMap.get(newSize)+1);
            } else {
                treeMap.put(newSize, 1);
            }
        }

        return (chocolatesEaten.mod(BigInteger.valueOf((long) (Math.pow(10,9)+7)))).intValue();
    }
}

