class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        last = 0
        
        for char in s:
            if last < values[char]:
                result -= last * 2
            
            result += values[char]  
            last = values[char]
            
        return result
