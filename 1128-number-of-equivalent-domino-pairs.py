from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        n = len(dominoes)
        count = 0


        # 1st approach - tle 
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]:
        #             count += 1
        #         elif dominoes[i][0] == dominoes[j][1] and dominoes[j][0] == dominoes[i][1]:
        #             count += 1
        #         else:
        #             continue
        # return count


        # 2nd approach 

        totals_pairs = 0
        counts = defaultdict(int)
        
        for a,b in dominoes:

            key = (a,b) if a <= b else (b,a)

            totals_pairs += counts[key]
            counts[key] += 1

        return totals_pairs