class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        majority = n / 2

        for key, val in freq.items():
            if val > majority:
                return key
            