class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        substring = ""
        if n == 1:
            return False

        for char in s:
            
            substring += char

            if len(substring) == n:
                break

            if n % len(substring) == 0:
                times = n // len(substring)
                if times * substring == s:
                    return True
        return False
            
            
               
        

       
        