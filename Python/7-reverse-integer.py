class Solution:
    def reverse(self, x: int) -> int:    
        negative = x < 0
        x = abs(x)
        
        result = 0
        
        while x > 0:
            end = x % 10
            x = x // 10
            
            result = result * 10 + end
            
        if negative:
            result *= -1
            
        if result > pow(2, 31)-1 or result < -1 * (pow(2, 31)):
            return 0
        
        return result
