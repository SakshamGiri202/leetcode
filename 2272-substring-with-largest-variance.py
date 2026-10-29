class Solution:
    def largestVariance(self, s: str) -> int:
        result = 0
        

        for first in range(ord('a'), ord('z') +1 ):
            for second in range(ord('a'), ord('z')+1):

                if first == second:
                    continue

                if chr(first) in s and chr(second) in s:
                    firstCount = 0
                    secondCount = 0
                    pastSecond = False

                    for char in s:
                        if char == chr(first):
                            firstCount += 1
                        if char == chr(second):
                            secondCount += 1

                        if secondCount > 0:
                            result = max(result, firstCount-secondCount)
                        else:
                            if pastSecond == True:
                                result = max(result, firstCount - 1)
                        
                        if secondCount > firstCount:
                            firstCount = 0
                            secondCount = 0
                            pastSecond = True

        return result