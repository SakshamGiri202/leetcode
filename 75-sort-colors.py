class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        """
             approach 1 using map for counting the freqency to same element and then sort it in the nums list and then return it
        """
        # mp = {}

        # n = len(nums)

        # for i in nums:
        #     mp[i] = mp.get(i,0)+1


        # idx = 0
        
        # for i in range(3):
        #     for j in range(mp.get(i, 0)):
        #         nums[idx] = i
        #         idx += 1

        """
                approach 2 using 3 pointer i,j and k where i for 0, j for 1 and k for 2
                when j crosses the k means array completed and exit the loop
        """
       
        i, j, k = 0, 0, len(nums)-1

        while j <= k:
            if nums[j] == 0:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1
        
