class Solution:
    def numberOfMatches(self, n: int) -> int:

        # matches = 0

        # while n > 1:
            
        #     matches += n // 2

        #     n = (n + 1) // 2

        # return matches

        # 2st appoarch 

        count = 0

        while n > 1:
            if n % 2 == 0:
                n //= 2
                count += n
            else:
                n //=2
                count += n
                n += 1

        return count

        
