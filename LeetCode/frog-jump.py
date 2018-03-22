# https://leetcode.com/problems/frog-jump/description/
# 112 ms

class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        stonesDic = {}
        for stone in stones: 
            stonesDic[stone] = True
            
        return self._canCross(stonesDic, stones[-1], stones[0], 1, {})
        
    def _canCross(self, stones, lastStone, currentPos, jumpLength, memo):
                
        key = str(currentPos) + ":" + str(jumpLength)
        if key in memo: return memo[key]
        
        if jumpLength <= 0: return False 
        if currentPos not in stones: return False
        if currentPos == lastStone: return True
        
        # Recursion
        result = (currentPos != 0 and self._canCross(stones, lastStone, currentPos+jumpLength+1, jumpLength+1, memo)) \
                or self._canCross(stones, lastStone, currentPos+jumpLength, jumpLength, memo) \
                or self._canCross(stones, lastStone, currentPos+jumpLength-1, jumpLength-1, memo)
                                
        memo[key] = result
        return result

