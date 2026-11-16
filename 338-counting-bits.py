class Solution:
    def countBits(self, n: int) -> list[int]:
        
        ans = [0]

        for num in range(1, n+1):
            count = 0
            temp = num

            while temp > 0:
                rem = temp  % 2
                if rem == 1:
                    count += 1
                temp //= 2

            ans.append(count)

        return ans