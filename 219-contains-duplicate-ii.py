class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        mp = {}

        for i, v in enumerate(nums):
            if v in mp and i - mp[v] <= k:
                return True
            mp[v] = i
        

         
        
        return False