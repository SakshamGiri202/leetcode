class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        mp = {}
        for i in range(n):
            mp[nums[i]] = mp.get(nums[i], 0)+1

        for key, val in mp.items():
            if val >= 2:
                return True
            else:
                continue

        return False