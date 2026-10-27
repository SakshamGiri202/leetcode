from collections import Counter

class Solution:
    
    # def is_anagram(self, str1:str, str2:str)-> bool:
    #     s1 = str1.lower()
    #     s2 = str2.lower()
    #     return Counter(s1) == Counter(s2)
    
    def findAnagrams(self, s: str, p: str) -> list[int]:

        """
        1st approach that casuse tle
        1. tranvase though the s string and check for the element that are present in p also
        2. if all the p's string are present then store the current (idx - m) because  lenght of  p is m
        """
        # n, m = len(s), len(p)

        # res = []

        # if n < m:
        #     return []



        # for i in range(n-m+1):
        #     substring = s[i:i+m]
            
        #     if self.is_anagram(substring,p):
        #         res.append(i)

        # return res

        # 2nd approach using hashmap and sliding window

        n , m = len(s), len(p)

        pmap , smap= {}, {}

        res = []

        if n < m:
            return []
        for char1, char2 in zip(s,p):
            smap[char1] = smap.get(char1, 0) + 1
            pmap[char2] = pmap.get(char2, 0) + 1


        if pmap == smap:
            res.append(0)

        left = 0

        for right in range(m, n):
            smap[s[right]] = smap.get(s[right], 0) + 1

            smap[s[left]] -= 1

            if smap[s[left]] == 0:
                del smap[s[left]]

            left += 1


            if pmap == smap:
                res.append(left)

        return res

        
