class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        mp = {}
        res = []

        for i in nums:
            mp[i] = mp.get(i, 0) + 1


        for i in range(1,n+1):
            if i not in mp:
                res.append(i)
            elif mp.get(i) > 1:
                res.insert(0, i)

        return res
        



       