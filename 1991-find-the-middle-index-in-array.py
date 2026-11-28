class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        n = len(nums)

        s = sum(nums)
        cs = 0

        for i in range(n):
            ls = cs
            rs = s - cs - nums[i]

            if ls == rs:
                return i
            cs  += nums[i]

        return -1