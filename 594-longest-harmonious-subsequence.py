class Solution:
    def findLHS(self, nums: list[int]) -> int:

        # 1st approach using hashmap
        freq = {}
        max_length = 0

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for key in freq:
            if key + 1 in freq:
                max_length = max(max_length, freq[key]+freq[key+1])

        return max_length