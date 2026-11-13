# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1st approach using 2 pointer(totrismethod- fast and slow)
        
        # fast = head
        # slow = head
        # idx = 0

        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow:
        #         slow = head
        #         while slow != fast:
        #             slow = slow.next
        #             fast = fast.next
        #         return slow

        # return None


        # 2nd approach using burte force method by hashset
        start = head
        seen = set()

        while start:
            if start in seen:
                return start
            else:
                seen.add(start)
                start = start.next
        return None 