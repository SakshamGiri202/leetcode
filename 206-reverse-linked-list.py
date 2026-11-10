# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head:ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        last = self.solve(head.next)
        head.next.next = head
        head.next = None
        return last
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # node = None

        # while head:
        #     temp = head.next
        #     head.next = node
        #     node = head
        #     head = temp

        # return node

        
        # if not head or not head.next:
        #     return head

        # new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head

        return self.solve(head)