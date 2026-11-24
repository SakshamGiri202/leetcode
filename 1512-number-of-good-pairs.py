class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        
        # 1st approach using stimulation/ bruteforce method
        # n = len(nums)
        # count = 0
        # i = 0

        # while i < n:
        #     j = i + 1
        #     while j < n:
        #         if nums[i] == nums[j]:
        #             count += 1
        #         j += 1
        #     i += 1
            
        # return count

        # 2nd appoarch using hashmap

        count = 0
        freq = {}

        for num in nums:
            
            count += freq.get(num, 0)
            freq[num] = freq.get(num, 0) + 1

        return count