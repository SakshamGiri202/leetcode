class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:


        # 1st approach without any built-in method

        # n = len(nums)

        # if n == 1: return True

        #  # check if this is increasing
        # for i in range(1, n):
        #     if nums[i] < nums[i-1]:
        #         break
        #     if i == n - 1:
        #         return True

        # # check if this is decreasing
        # for i in range(1, n):
        #     if nums[i] > nums[i-1]:
        #         break
        #     if i == n-1:
        #         return True
        
        # return False

        # 2nd approach with built-in method

        if nums == sorted(nums):
            return True
        if nums==sorted(nums, reverse=True):
            return True
        return False
            

        
