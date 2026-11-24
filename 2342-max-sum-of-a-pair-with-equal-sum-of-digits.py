class Solution:
    def digitSum(self, num:int) -> int:
        s = str(num)
        sum = 0
        for ch in s:
            sum += int(ch) 
        return sum

    def maximumSum(self, nums: list[int]) -> int:

        # 1st approach using bruteforce method
        n = len(nums)
        maxSum = -1

        maxD = [0]*100


        for num in nums:
            d = self.digitSum(num)
            if maxD[d] > 0:
                maxSum = max(maxSum, maxD[d] + num)
            maxD[d] = max(maxD[d], num)
            
        return maxSum

        # 2st approach using hashmap 

        
                    