class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = {}
        count = 0

        if len(ransomNote) > len(magazine):
            return False
            
        for x in magazine:
            mp[x] = mp.get(x, 0) + 1

        for y in ransomNote:
            if y  in mp and mp[y]>0:
                mp[y] -= 1
            else:
                return False
        return True           
            
        
        