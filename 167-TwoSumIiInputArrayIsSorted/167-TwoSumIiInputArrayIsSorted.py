# Last updated: 10/4/2026, 11:29:13 PM
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        j = n - 1
        for i in range(n):
                while(i < j):
                    if numbers[i] + numbers[j] < target:
                        i += 1
                    elif numbers[i] + numbers[j] > target:
                        j -= 1
                    elif numbers[i] + numbers[j] == target:
                        return [i+1, j+1]