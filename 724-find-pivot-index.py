class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        carry = 0
        s = sum(nums)
    
        for idx in range(n):
            leftSum = carry
            rightSum = s - leftSum - nums[idx]
            if leftSum == rightSum:
                return idx
            carry += nums[idx]
        
        return -1


            
