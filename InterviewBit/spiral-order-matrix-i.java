// https://www.interviewbit.com/courses/programming/topics/arrays/problems/spiral-order-matrix-i/
// 

public class Solution {
    // DO NOT MODIFY THE LIST
    public ArrayList<Integer> spiralOrder(final List<ArrayList<Integer>> a) {
         ArrayList<Integer> result = new ArrayList<Integer>();
         // Populate result;
         
         int rl = a.get(0).size()-1, lel = 0, ul= 0, lol=a.size()-1;
         
         int ac = 0, n=0;
         
         while (lel <= rl && ul<=lol && n<a.size()*a.get(0).size())
         {
             if (ac == 0)
             {
                for (int j=lel; j<=rl; j++)
                {
                    result.add(a.get(ul).get(j));
                }
                ul++;
             }
             else if (ac == 1)
             {
                 for (int j=ul; j<=lol; j++)
                {
                    result.add(a.get(j).get(rl));
                }
                rl--;
             }
             else if (ac == 2)
             {
                 for (int j=rl; j>=lel; j--)
                {
                    result.add(a.get(lol).get(j));
                }
                lol--;
             }
             else if (ac == 3)
             {
                 for (int j=lol; j>=ul; j--)
                {
                    result.add(a.get(j).get(lel));
                }
                
                lel++;
                
             }
             
             n++;
             ac = (ac+1) % 4;
         }
        
         
         return result;
    }
}

