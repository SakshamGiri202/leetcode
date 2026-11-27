class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        mp = {}

        res = []

        if nums is None and nums == 1:
            return res

        for num in nums:
            mp[num] = mp.get(num, 0) + 1


        for key, val in mp.items():
            if val == 2:
                res.append(key)

        return res