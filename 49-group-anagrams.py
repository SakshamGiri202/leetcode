class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = defaultdict(list)

        for s in strs:
            st = "".join(sorted(s))
            mp[st].append(s)
            

        return list(mp.values())