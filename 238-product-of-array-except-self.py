class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # n = len(nums)
        # res = [0] * n

        # prefix = [1] * n 
        # suffix = [1] * n

        # for i in range(1,n):
        #     prefix[i] = prefix[i-1] * nums[i-1]

        # for i in range(n-2, -1, -1):
        #     suffix[i] = suffix[i+1] * nums[i+1]

        # res = [prefix[i] * suffix[i] for i in range(n)]
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]



        return res