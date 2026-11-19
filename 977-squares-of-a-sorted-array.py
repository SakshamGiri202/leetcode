class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = []
        
        for num in nums:
            tmp = num * num
            res.append(tmp)

        
        
        return sorted(res)