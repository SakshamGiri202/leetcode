class Solution:

    def calculateDays(self, weights:list[int], mid:int)->int:
        days, load = 1, 0

        for i in range(len(weights)):
            if load+ weights[i] >mid:
                days += 1
                load = weights[i]
            else:
                load += weights[i]
        return days
   
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        
        while low <= high:
            mid = (low+high)//2

            daysReq = self.calculateDays(weights, mid)

            if daysReq <= days:
                high = mid - 1
            else:
                low = mid + 1

        return low

        
    
        