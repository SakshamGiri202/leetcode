class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        """
             approach 1 using map for counting the freqency to same element and then sort it in the nums list and then return it
        """
        mp = {}

        n = len(nums)

        for i in nums:
            mp[i] = mp.get(i,0)+1


        idx = 0
        
        for i in range(3):
            for j in range(mp.get(i, 0)):
                nums[idx] = i
                idx += 1
