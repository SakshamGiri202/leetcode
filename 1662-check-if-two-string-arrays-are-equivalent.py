class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        w1 = "".join(word1)
        w2 = "".join(word2)

        if w1 == w2:
            return True
        else:
            return False