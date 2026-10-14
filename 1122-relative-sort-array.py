class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
       
        result = []
        
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    result.append(arr1[j])
                    arr1[j] = -1
        
        arr1.sort()
        
        for num in arr1:
            if num != -1:
                result.append(num)
                
        return result

       
       
        # 2nd approach using counting sort
        # n = len(arr1)
        # m = len(arr2)
        
        # max_val = max(arr1)

        # count = [0] * (max_val + 1)

        # res = []


        # for num in arr1:
        #     count[num] += 1
        
        # for num in arr2:
        #     while count[num] > 0:
        #         res.append(num)
        #         count[num] -= 1

        # for num in range(max_val+1):
        #     while count[num] > 0:
        #         res.append(num)
        #         count[num] -= 1

        # return res