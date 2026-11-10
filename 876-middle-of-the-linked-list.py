# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:

        # approach 1st using brute force method

        # count = 0
        # temp = head
        # while temp != None:
        #     count += 1
        #     temp = temp.next

        # mid = count//2

        # temp = head
        # for _ in range(mid):
        #     temp = temp.next
        
        # return temp

        # approach 2nd using brute force

        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow
