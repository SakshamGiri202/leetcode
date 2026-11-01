class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        
        n = len(code)
        res = [0] * n
        # 1st approach  use brute force
        # if code == 0:
        #     return res

        # for i in range(n):
        #         if k > 0:
        #             for j in range(i+1, i+1+k):
        #                 res[i] += code[j%n]
        #         elif k < 0:
        #             for j in range(i-1, i-1-abs(k), -1):
        #                 res[i] += code[j%n]
        # return res
            
        # 2nd approach using sliding window

        start = 1 if k > 0 else n + k
        end = k if k > 0 else n - 1

        wSum = sum(code[i % n] for i in range(start, end+1))

        for i in range(n):
            res[i] = wSum 
            wSum -= code[(start + i) % n]
            wSum += code[(end + i + 1) % n]

        return res