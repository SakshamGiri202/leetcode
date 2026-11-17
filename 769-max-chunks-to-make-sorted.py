class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)

        chunkCount = 0

        # 1st approach 
        # suffixMin = [float('inf')] * n
        # for i in range(n-2, -1, -1):
        #     suffixMin[i] = min(arr[i+1],suffixMin[i+1])

        # preffixMax = float('-inf')
        # for i in range(n):
        #     preffixMax = max(arr[i], preffixMax)


        #     if suffixMin[i] > preffixMax:
        #         chunkCount += 1

        # 2nd approach
        # prevMax = 0
        # for idx, x in enumerate(arr):
        #     prevMax = max(prevMax, x)
        #     if prevMax == idx:
        #         chunkCount += 1

        # 3rd approach

        sorted_array = 0
        unsorted_array = 0
        for i, x in enumerate(arr):
            sorted_array +=  i
            unsorted_array += x
            if(unsorted_array - sorted_array == 0):
                chunkCount += 1 

        return chunkCount

        