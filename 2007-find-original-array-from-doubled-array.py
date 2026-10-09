class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        n = len(changed)

        if n % 2 != 0:
            return []
        mp = {}
        res = []
        changed.sort()

        for i in changed:
            mp[i] = mp.get(i, 0) + 1
        
        for i in range(n):
            checker = changed[i] * 2
            if mp[changed[i]] == 0:
                continue

            if  mp.get(checker, 0) == 0:
                return []

            
            res.append(changed[i])
            mp[changed[i]] -= 1
            mp[checker] -= 1
            
            
        
        return res


        