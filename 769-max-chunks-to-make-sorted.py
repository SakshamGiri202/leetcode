class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)

        chunkCount = 0
    

        suffixMin = [float('inf')] * n
        for i in range(n-2, -1, -1):
            suffixMin[i] = min(arr[i+1],suffixMin[i+1])

        preffixMax = float('-inf')
        for i in range(n):
            preffixMax = max(arr[i], preffixMax)


            if suffixMin[i] > preffixMax:
                chunkCount += 1

        return chunkCount

        