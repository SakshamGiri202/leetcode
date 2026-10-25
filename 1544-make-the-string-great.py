class Solution:
    def makeGood(self, s: str) -> str:
        result = []

        for i in range(len(s)):
          
            if result and abs(ord(result[-1]) - ord(s[i])) == 32:
                result.pop()
            else:
                result.append(s[i])

        return "".join(result)