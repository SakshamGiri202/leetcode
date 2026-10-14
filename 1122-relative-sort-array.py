class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        n = len(arr1)
        m = len(arr2)
        
        max_val = max(arr1)

        count = [0] * (max_val + 1)

        res = []


        for num in arr1:
            count[num] += 1
        
        for num in arr2:
            while count[num] > 0:
                res.append(num)
                count[num] -= 1

        for num in range(max_val+1):
            while count[num] > 0:
                res.append(num)
                count[num] -= 1

        return res