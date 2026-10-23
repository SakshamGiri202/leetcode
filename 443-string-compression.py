class Solution:
    def compress(self, chars: list[str]) -> int:
        idx, count = 0, 0
        n = len(chars)
        curr_char = chars[0]

        for i in range(n):
            if curr_char == chars[i]:
                count += 1
            else:
                chars[idx] = curr_char
                idx += 1

                if count > 1:
                    for c in str(count):
                        chars[idx] = c
                        idx += 1
                
                curr_char = chars[i]
                count = 1

        chars[idx] = curr_char
        idx += 1

        if count >1:
            for c in str(count):
                chars[idx] = c
                idx += 1
                

        return idx
                

        

                    
       