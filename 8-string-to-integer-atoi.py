class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        res = []
        s = s.strip()
        syn = ["+","-"]
        sign = 1
        min_int = -(2**31)
        max_int = (2**31) - 1

        for i, char in enumerate(s):
            if i == 0 and char in syn:
                if char == "-":
                    sign = -1 
                continue
            if char.isdigit():
                res.append(char)
            else:
                break

        if not res:
            return 0

        val = 0
        for char in res:
            val = val * 10 + int(char)
        
        val *= sign 


        return max(min_int, min(val, max_int))

