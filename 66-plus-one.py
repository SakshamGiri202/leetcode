class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        # 1st approach using bruteforce
        s = ''

        for digit in digits:
            s += str(digit)

        sum = int(s) + 1

        return list(map(int, str(sum)))