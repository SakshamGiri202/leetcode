class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}
        
        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1

        for idx, val in enumerate(s):
            if mp[val] == 1:
                return idx
                
        
        return -1