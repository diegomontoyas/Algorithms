# https://www.interviewbit.com/courses/programming/topics/greedy/problems/gas-station/
# 

class Solution:
    # @param gas : tuple of integers
    # @param cost : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        i = 0
        j = (i+1) % len(gas)
        fuel = gas[i] - cost[i]
        
        while j != i:
            
            while fuel < 0 and ((j==0 and i<len(gas)-1) or (j>0 and i<j)):
                fuel -= gas[i] - cost[i]
                i+=1
            
            fuel += gas[j] - cost[j]
            j = (j+1) % len(gas)
        
        return i if fuel >= 0 else -1
