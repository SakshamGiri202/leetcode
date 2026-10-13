class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        """
        brute force approach where time limit execceds out...
        """
        # n = len(s)
        # word_length = len(words[0])
        # nums_word = len(words)
        # substring_length = word_length * nums_word
        # starting_index = []

        # def check(i):
        #     for j in range(i, i+substring_length, word_length):
        #         word = s[j:j+word_length]
        #         if word not in word_count: return False
        #         elif word_count[word] == 1: del word_count[word]
        #         else: word_count[word] -= 1
        #     return True
        # for i in range(n-substring_length+1):
        #     word_count = {}
        #     for w in words:
        #         if w not in word_count: word_count[w] = 1
        #         else: word_count[w] += 1
        #     if check(i):
        #         starting_index.append(i)
        # return starting_index
        
        """
            sliding window approach
        """

        n = len(s)
        word_length = len(words[0])
        nums_word = len(words)
        word_count = Counter(words)

        starting_index = []

        for i in range(word_length):
            left, right = i, i
            seen = defaultdict(int)
            word_used = 0
            
            while right + word_length <= n:
                word = s[right:right+word_length]
                right += word_length
                if word in word_count:
                    seen[word] += 1
                    word_used += 1

                    while seen[word] > word_count[word]:
                        leftmost_word = s[left:left+word_length]
                        seen[leftmost_word] -= 1
                        if seen[leftmost_word] == 0:
                            del seen[leftmost_word]
                        word_used -= 1
                        left += word_length

                    if word_used == nums_word:
                        starting_index.append(left)
                else:
                    seen.clear()
                    word_used = 0
                    left = right
        return starting_index