class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:

        n = len(arr)
        mp = {}

        sorted_arr = []
        for i in range(n):
            num = arr[i]
            count = num.bit_count()
            mp[arr[i]] = count

       
        sorted_arr = sorted(arr, key=lambda x: (x.bit_count(), x))

        return sorted_arr


        
        