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
        
        seen = set()
        
        for num in nums:
            if num not in seen:
                if nums.count(num) > len(nums) // 2:
                    return num
                else:
                    seen.add(num)

