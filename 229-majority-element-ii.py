class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        
        # 1st approach using set hashmap
        # seen = set()
        
        # for num in nums:
        #     if len(seen) == 2:
        #         break
        #     if num not in seen:
        #         if nums.count(num) > len(nums)// 3:
        #             seen.add(num)

        # return list(seen)

        freq = {}
        threshold = len(nums) // 3
        

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        res = []

        for key, val in freq.items():
            if val > threshold:
                res.append(key)
            if len(res) == 2:
                break
        return res

        