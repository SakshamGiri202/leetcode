class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        """
            1st approach - implementing hashmap 
        """
        # n = len(nums)
        # mp = {}
        # for i in range(n):
        #     mp[nums[i]] = mp.get(nums[i], 0)+1

        # for key, val in mp.items():
        #     if val >= 2:
        #         return True
        #     else:
        #         continue

        # return False


        """
            2nd approach - implementing hashset
        """

        seems = set()

        for num in nums:
            if num in seems:
                return True
            seems.add(num)
        
        return False