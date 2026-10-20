class Solution:

    def calculateTotalHrs(self, piles:list[int], mid:int)-> int:
        
        totalHrs = sum(math.ceil(pile/mid) for pile in piles)

        return totalHrs



    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        
        ans = 0

        while l <= r:
            mid = (l+r)//2

            total_hrs  = self.calculateTotalHrs(piles, mid)

            if total_hrs <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
        