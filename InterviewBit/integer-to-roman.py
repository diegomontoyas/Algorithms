# https://www.interviewbit.com/courses/programming/topics/strings/problems/integer-to-roman/
# 

class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        intToRomanDic = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        decimalValues = sorted(intToRomanDic.keys(), reverse=True)
        romanNumber = ""
    
        for i, digit in enumerate(str(A)):
            if digit == "0": continue
    
            sum = (10 ** (len(str(A))-i-1)) * int(digit)
    
            while sum > 0:
                j = 0
                while decimalValues[j] > sum and j < len(decimalValues):
                    j += 1
    
                availableDecimal = decimalValues[j]
    
                if availableDecimal * 3 >= sum and digit != "9":
                    romanNumber += intToRomanDic[availableDecimal]
                    sum -= availableDecimal
    
                else:
                    rightDecimal = decimalValues[j - 1]
    
                    j = 0
                    while j < len(decimalValues)-1 and rightDecimal - decimalValues[j] != sum:
                        j += 1
    
                    romanNumber += intToRomanDic[decimalValues[j]]
                    romanNumber += intToRomanDic[rightDecimal]
                    sum -= (rightDecimal - decimalValues[j])
    
        return romanNumber
                    
