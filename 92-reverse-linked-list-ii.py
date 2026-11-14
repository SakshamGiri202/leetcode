# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        # dummy = ListNode(0, head)
        # prev = dummy

        # for _ in range(left - 1):
        #     prev = prev.next

        # curr = prev.next
        # for _ in range(right-left):
        #     temp = curr.next
        #     curr.next = temp.next
        #     temp.next = prev.next
        #     prev.next = temp
            

        # return dummy.next


        # 2nd approach 

        dummy = ListNode(0, head)
        
        leftPrev, curr = dummy, head
        for i in range(left - 1):
            leftPrev, curr = curr, curr.next

        prev = None
        for i in range(right-left+1):
            tempNext = curr.next
            curr.next = prev
            prev, curr= curr, tempNext


        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next