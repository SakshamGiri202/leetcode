class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        map = {}
        for i in range(n):
            map[nums[i]] = map.get(nums[i], 0)+1

        print(map)

        for key, val in map.items():
            if val >= 2:
                return True
            else:
                continue

        return False