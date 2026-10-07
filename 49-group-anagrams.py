class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = {}
        res = []
        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr in mp:
                res[mp[sortedStr]].append(s)
            else:
                mp[sortedStr] = len(res)
                res.append([s])
        return res
