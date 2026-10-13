class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # 1st approach 
        # words = s.split(" ")

        # if len(pattern) != len(): return False

        # char_to_word = {}
        # word_to_char = {}

        # for char, word in zip(pattern, words):
        #     if char in char_to_word and char_to_word[char] != word:
        #         return False
            
        #     if word in word_to_char and word_to_char[word] != char:
        #         return False
            
        #     char_to_word[char] = word
        #     word_to_char[word] = char

        # return True


        # 2nd approac

        words = s.split(" ")
        
        if len(pattern) != len(words): return False

        letter_to_word = {}

        sett = set()

        for i in range(len(pattern)):
            if pattern[i] not in letter_to_word:
                if words[i] in sett:
                    return False
                else:
                    letter_to_word[pattern[i]] = words[i]
                    sett.add(words[i])
            elif letter_to_word[pattern[i]] != words[i]:
                return False
        return True
    