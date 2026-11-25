class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        
        # 1st approach using bruteforce method
        # n = len(nums)
        # count = 0
        # i = 0 
        # while i < n:
        #     j = i + 1
        #     while j < n:
        #         if nums[i] - i != nums[j] -j:
        #             count += 1
        #         j += 1
        #     i += 1

        # return count

        # 2nd approach using hashmap
        n = len(nums)
        freq = {}
        totalPairs = n * (n-1)//2
        goodPairs = 0

        for idx, val in enumerate(nums):
            diff = val - idx
            goodPairs += freq.get(diff, 0)
            freq[diff] = freq.get(diff, 0) + 1

        return totalPairs - goodPairs
            
