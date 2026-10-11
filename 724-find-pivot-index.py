class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        carr = [0] * n
        s = 0

        for i in range(n):
            s += nums[i]
            carr[i] += s
        
        for i in range(n):
            if i == 0:
                l= 0
            else:
                l = carr[i - 1]
                
            r = s - l - nums[i]
            if l == r:
                return i
            else:
                continue
        return -1  
         
        
