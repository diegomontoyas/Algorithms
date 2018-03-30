# https://leetcode.com/problems/shortest-completing-word/
# 152 ms

from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        reference = self.countLetters(licensePlate)
        minLengthWord = None
        minLength = float('inf')
        
        for word in words:
            count = self.countLetters(word)
            if self.countMatches(reference, count) and len(word) < minLength:
                minLengthWord = word
                minLength = len(word)
        
        return minLengthWord
    
    def countLetters(self, word):
        counter = Counter()
        for char in word: 
            if char.isdigit() or char == ' ': continue
            counter[char.lower()] += 1
        return counter
    
    def countMatches(self, reference, count):
        for char in reference:
            if count[char] < reference[char]: 
                return False
        
        return True
        
