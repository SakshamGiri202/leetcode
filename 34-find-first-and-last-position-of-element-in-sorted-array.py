class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findBound(isfirst:bool) -> int:
            l, r = 0, len(nums) - 1
            bound = -1

            while l <= r:
                m = (r+l)//2
                if target == nums[m]:
                    bound = m
                    if isfirst:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return bound

        first = findBound(isfirst=True)

            
        if target == -1:
            return [-1, -1]

        last = findBound(isfirst=False) 
        
        return [first, last]