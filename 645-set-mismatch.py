class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        mp = {}
        res = []

        #approach 1

        # for i in nums:
        #     mp[i] = mp.get(i, 0) + 1


        # for i in range(1,n+1):
        #     if i not in mp:
        #         res.append(i)
        #     elif mp.get(i) > 1:
        #         res.insert(0, i)

        # return res
        
        #approach 2

        duplicate = -1
        missing = -1
        

        for i in range(n):
            if nums[abs(nums[i]) - 1] < 0:
                duplicate = abs(nums[i])
            else:
                nums[abs(nums[i])-1] *= -1 
            
        
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
                break
               
        return [duplicate, missing]