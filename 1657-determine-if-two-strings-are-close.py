class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        n, m = len(word1), len(word2)

        if n != m:
            return False

        freq1, freq2 = [0] * 26, [0] * 26


        for i, j in zip(word1, word2):
            freq1[ord(i)- ord("a")] += 1
            freq2[ord(j)-ord("a")] += 1

        for i in range(26):
            if freq1[i] == 0 and freq2[i] != 0 or freq1[i] != 0 and freq2[i] == 0:
                return False

        freq1.sort()
        freq2.sort()

        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True 