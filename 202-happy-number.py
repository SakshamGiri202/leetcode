class Solution:
    def isHappy(self, n: int) -> bool:
        

        # 1st approach uing hash set and storing unique value of the n and checking it agnaist set hash

        # window = set()

        # while n != 1:
        #     str_num = str(n)
        #     n = sum(int(d)**2 for d in str_num)

        #     if n != 1 and n in window:
        #         return False
        #     else:
        #         window.add(n)
        
        # return True


        # 2nd approach 

        def get_next(i):
            str_num = str(i)
            i = sum(int(d)**2 for d in str_num)

            return i
        
        slow = fast = n 

        while slow != 1:
            slow = get_next(slow)
            fast = get_next(fast)
            fast = get_next(fast)
            if fast == slow and slow != 1:
                return False
        
        return True
