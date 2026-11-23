class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        sortArray = sorted(arr)

        diff = sortArray[1] - sortArray[0]

        for i in range(2, len(sortArray)):
            if sortArray[i] - sortArray[i-1] != diff:
                return False

        return True
             

