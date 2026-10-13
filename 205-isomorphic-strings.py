class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
       
        # 1st approach using hash map
        # if len(s) != len(t):
        #     return False

        # s1 = {}
        # t1 = {}
        # # sett = set()

        # for i,j in zip(s, t):
        #     if i in s1 and s1[i] != j:
        #         return False
        #     if j in t1 and t1[j] != i:
        #         return False
        #     s1[i] = j
        #     t1[j] = i

        # return True

        # 2nd approach using hash set

        if len(s) != len(t):
            return False

        mp = {}
        sett = set()

        for i, j in zip(s, t):
            if i not in mp:
                if j in sett:
                    return False
                else:
                    mp[i] = j
                    sett.add(j)
            elif mp[i] != j:
                return False
        
        return True





