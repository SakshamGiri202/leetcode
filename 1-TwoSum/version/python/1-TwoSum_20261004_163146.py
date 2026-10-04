# Last updated: 10/4/2026, 4:31:46 PM
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        temp = []
        n = len(nums)
        mp = {}
        for i in range(n):
            compliment = target - nums[i] 
            if compliment in mp:
                temp.append(mp[compliment])
                temp.append(i)
                return temp
            mp[nums[i]] = i    
            
