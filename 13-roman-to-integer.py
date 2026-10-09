class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {"I":1, "V": 5, "X": 10, "L":50, "C":100, "D": 500, "M":1000}
        
        sum = 0

        n = len(s)
        i = 0
    
        while i < n:
            if i < n - 1 and mp[s[i]] < mp[s[i+1]]:
                sum += mp[s[i+1]] - mp[s[i]]
                i += 2
            else:
                sum += mp[s[i]]
                i += 1
        
        return sum