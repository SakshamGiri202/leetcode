class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1 = {}
        t1 = {}
        # sett = set()

        for i,j in zip(s, t):
            if i in s1 and s1[i] != j:
                return False
            if j in t1 and t1[j] != i:
                return False
            s1[i] = j
            t1[j] = i

        return True