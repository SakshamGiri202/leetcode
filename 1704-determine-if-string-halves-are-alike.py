class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a = s[:n//2]
        b = s[n//2:]

        print(a,b)
        countVowel1, countVowel2 = 0, 0

        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for char1, char2 in zip(a,b):
            if char1 in vowel:
                countVowel1 += 1
            if char2 in vowel:
                countVowel2 += 1

        if countVowel1 == countVowel2:
            return True
        else:
            return False
