class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)

        # approach 1

        # carr = [0] * n
        # s = 0

        # for i in range(n):
        #     s += nums[i]
        #     carr[i] += s
        
        # for i in range(n):
        #     if i == 0:
        #         l= 0
        #     else:
        #         l = carr[i - 1]

        #     r = s - l - nums[i]
        #     if l == r:
        #         return i
        #     else:
        #         continue
        # return -1  
         

        # approach 2

        s = sum(nums)
        l = 0

        for i in range(n):
            if l == s-l-nums[i]:
                return i
            l += nums[i]

        return -1 
        
