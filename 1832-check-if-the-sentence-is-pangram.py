class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
         
        # arr = [0]* 26
        # for char in sentence:
        #     idx = ord(char) - ord('a')
        #     arr[idx] = 1

        # if sum(arr) == 26:
        #     return True
        # else: 
        #     return False

        return len(set(sentence)) == 26