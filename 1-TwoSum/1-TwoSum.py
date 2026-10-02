# Last updated: 10/2/2026, 10:11:22 AM
from array import *

class Solution(object):

    #brute force method (0(n2))
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    continue