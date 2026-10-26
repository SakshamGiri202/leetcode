class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        k = len(strs[0])

        # first_characters = [s[0] for s in strings if s]

        # s == "".join(sorted(s))

        delete_count = 0

        for i in range(k):
            for j in range(1,n):
                if strs[j][i] < strs[j-1][i]:
                    delete_count += 1
                    break
        
        return delete_count





