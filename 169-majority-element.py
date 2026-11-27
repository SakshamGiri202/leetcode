class Solution:
    def majorityElement(self, nums: list[int]) -> int:
       
        # 1st approach using hashmap
        # n = len(nums)
        # freq = {}
        
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        # majority = n / 2

        # for key, val in freq.items():
        #     if val > majority:
        #         return key
            

        # 2nd approach using set hashmap
        
        # seen = set()
        
        # for num in nums:
        #     if num not in seen:
        #         if nums.count(num) > len(nums) // 2:
        #             return num
        #         else:
        #             seen.add(num)

        # 3nd approach using boyer and moore voting

        n = len(nums)
        count = 0
        maj = nums[0]
        for i in range(n):
            if count == 0:
                maj = nums[i]
                count = 1
            elif nums[i] == maj:
                count += 1
            else:
                count -= 1
        
        return maj
            

