class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        
        n = len(nums)
        count = 0
        i = 0

        while i < n:
            j = i + 1
            while j < n:
                if nums[i] == nums[j]:
                    count += 1
                j += 1
            i += 1
            
        return count