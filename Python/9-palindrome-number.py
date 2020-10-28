class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        start = 0
        end = len(string) - 1
        
        while start < end:
            if end < len(string) and string[start] != string[end]:
                return False
            
            start += 1
            end -= 1
            
        return True
