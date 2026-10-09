class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)

        sum  = 0

        res = []

        for i in nums:
            if i % 2 == 0:
                sum += i

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                sum -= nums[idx]
            nums[idx] += val


            if nums[idx] % 2 == 0:
                sum += nums[idx]
            
            res.append(sum)

        return res
