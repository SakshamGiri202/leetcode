class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:

        mp = {}

        for i in arr:
            mp[i] = mp.get(i, 0) + 1

        print(mp)

        seen = set()

        for i in mp.values():
            
            if i in seen:
                return False
            seen.add(i)
        
        return True