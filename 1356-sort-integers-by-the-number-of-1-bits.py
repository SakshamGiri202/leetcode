from collections import defaultdict

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:

        n = len(arr)
        groups = defaultdict(list)
        sorted_arr = []
        for num in arr:
            count = num.bit_count()
            groups[count].append(num)
        


        for count in sorted(groups.keys()):
            if count in groups:
                groups[count].sort()
                sorted_arr.extend(groups[count])


       
        # sorted_arr = sorted(arr, key=lambda x: (x.bit_count(), x))

        return sorted_arr


        
        